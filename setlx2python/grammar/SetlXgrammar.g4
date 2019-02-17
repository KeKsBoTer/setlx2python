grammar SetlXgrammar;

@parser::header {
from .types import *
}

block
	returns[Block blk]
	@init {
stmnts = []
    }: (statement {stmnts.append($statement.stmnt)})* {$blk = Block(stmnts)};

statement
	returns[stmnt]
	@init {
else_list = []
caseList = []
tryList = []
expression = None
condition = None
static = None
    }:
	'class' ID '(' procedureParameters[True] ')' '{' b1 = block (
		'static' '{' b2 = block '}' {static = $b2.blk}
	)? '}' {$stmnt = ClassConstructor($ID.text, $procedureParameters.paramList, $b1.blk, static)}
	|'if' '(' c1 = condition ')' '{' b1 = block '}' (
		'else' 'if' '(' c2 = condition ')' '{' b2 = block '}' {else_list.append(IfThenBranch($c2.cnd,$b2.blk,[])) 
			}
	)* ('else' '{' b3 = block '}' {else_list.append($b3.blk) })? {$stmnt = IfThen($c1.cnd,$b1.blk,else_list) 
		}
	| 'switch' '{' (
		'case' c1 = condition ':' b1 = block {caseList.append(($c1.cnd, $b1.blk)) }
	)* ('default' ':' b2 = block)? '}' {$stmnt = Switch(caseList,$b2.blk) }
	//| match 
	//| scan 
	| 'for' '(' iteratorChain[False] (
		'|' condition {condition = $condition.cnd}
	)? ')' '{' block '}' {$stmnt = SetlXFor($iteratorChain.ic, condition, $block.blk) }
	| 'while' '(' condition ')' '{' block '}' {$stmnt = SetlXWhile($condition.cnd, $block.blk) }
	| 'do' '{' block '}' 'while' '(' condition ')' ';' {$stmnt = DoWhile($condition.cnd, $block.blk) 
		}
	| 'try' '{' b1 = block '}' /*(
		'catchLng' '(' v1 = assignableVariable ')' '{' b2 = block '}' {tryList.append( TryCatchLngBranch($v1.v, $b2.blk))         
			}
		| 'catchUsr' '(' v1 = assignableVariable ')' '{' b2 = block '}' {tryList.append( TryCatchUsrBranch($v1.v, $b2.blk))         
			}
	)**/ (
		'catch' '(' v2 = assignableVariable ')' '{' b3 = block '}' {tryList.append(TryCatchBranch($v2.v, $b3.blk))         
			}
	)? {$stmnt = TryCatch($b1.blk, tryList) }
	/*| 'check' '{' b1 = block '}' (
		'afterBacktrack' '{' b2 = block {block = $b2.blk} '}'
	)? {$stmnt = Check($b1.blk, block)                         }
	*/
	| 'backtrack' ';' {$stmnt = Backtrack() }
	| 'break' ';' {$stmnt = SetlXBreak() }
	| 'continue' ';' {$stmnt = SetlXContinue() }
	| 'exit' ';' {$stmnt = Exit() }
	| 'return' (expr[False] {expression = $expr.ex })? ';' {$stmnt = SetlXReturn(expression) }
	| 'assert' '(' condition ',' expr[False] ')' ';' {$stmnt = SetlXAssert($condition.cnd, $expr.ex)}
	| assignmentOther ';' {$stmnt = $assignmentOther.assign }
	| assignment ';' {$stmnt = $assignment.assign }
	| expr[False] ';' {$stmnt = $expr.ex};

assignmentOther
	returns[assign]:
	assignable[False] (
		'+=' e = expr[False] {$assign = SumAssignment($assignable.a, $e.ex) }
		| '-=' e = expr[False] {$assign = DifferenceAssignment($assignable.a, $e.ex) }
		| '*=' e = expr[False] {$assign = ProductAssignment($assignable.a, $e.ex) }
		| '/=' e = expr[False] {$assign = QuotientAssignment($assignable.a, $e.ex) }
		| '\\=' e = expr[False] {$assign = IntegerDivisionAssignment($assignable.a, $e.ex) }
		| '%=' e = expr[False] {$assign = ModuloAssignment($assignable.a, $e.ex) }
	);

assignment
	returns[assign]:
	// special case for transpiler: name := procedure(){...}
	variable ':=' procedure[$variable.v.id] {$assign = $procedure.pd }
	| assignmentDirect {$assign = $assignmentDirect.assign };

assignmentDirect
	returns[assign]:
	assignable[False] ':=' (
		assignmentDirect {$assign = Assignment([$assignable.a]+$assignmentDirect.assign.assignables, $assignmentDirect.assign.right_hand_side) }
		| exprContent[False] {$assign = Assignment([$assignable.a], $exprContent.ex) }
	);

assignable[enableIgnore]
	returns[a]:
	assignableVariable {$a = $assignableVariable.v} (
		'.' variable {$a = AssignableMember($a, $variable.v)}
		| '[' exprList[False] ']' {$a = AssignableCollectionAccess($a, $exprList.exprs)}
	)*
	| '[' assignmentList ']' {$a = AssignableList($assignmentList.al)}
	| {$enableIgnore}? '_' {$a = AssignableIgnore()};

assignableVariable
	returns[v]: ID {$v = Variable($ID.text) };

expr[enableIgnore]
	returns[ex]:
	exprContent[$enableIgnore] {$ex = $exprContent.ex };

exprList[enableIgnore]
	returns[exprs]
	@init {
$exprs = []
    }:
	exprContent[$enableIgnore] {$exprs.append($exprContent.ex)} (
		',' exprContent[$enableIgnore] {$exprs.append($exprContent.ex)}
	)*;

exprContent[enableIgnore]
	returns[ex]:
	lambdaProcedure  {$ex = $lambdaProcedure.lp }
	|implication[$enableIgnore] {$ex = $implication.i} (
		'<==>' implication[$enableIgnore] {$ex = BooleanEqual($ex,$implication.i) }
		| '<!=>' implication[$enableIgnore] {$ex = BooleanNotEqual($ex,$implication.i) }
	)?;

lambdaProcedure
	returns[lp]:
	lambdaParameters (
		// TODO '|->' expr[False] {$lp = LambdaProcedure($lambdaParameters.paramList, $expr.ex) }
		/* |*/ '|=>' expr[False] {$lp = LambdaClosure($lambdaParameters.paramList, $expr.ex)   }
	);

lambdaParameters
	returns[paramList]
	@init {
$paramList = []
    }:
	variable {$paramList.append(Parameter($variable.v.id, None, False)) }
	| '[' (
		v1 = variable {$paramList.append(Parameter($v1.v.id, None, False))} (
			',' v2 = variable {$paramList.append(Parameter($v2.v.id, None, False))}
		)*
	)? ']';

implication[enableIgnore]
	returns[i]:
	disjunction[$enableIgnore] {$i = $disjunction.d} (
		'=>' implication[$enableIgnore] {$i = Implication($i, $implication.i) }
	)?;

disjunction[enableIgnore]
	returns[d]:
	conjunction[$enableIgnore] {$d = $conjunction.c} (
		'||' conjunction[$enableIgnore] {$d = Disjunction($d, $conjunction.c) }
	)*;

conjunction[enableIgnore]
	returns[c]:
	comparison[$enableIgnore] {$c = $comparison.c} (
		'&&' comparison[$enableIgnore] {$c = Conjunction($c, $comparison.c) }
	)*;

comparison[enableIgnore]
	returns[c]:
	s1 = setlxSum[$enableIgnore] {$c = $s1.s } (
		'==' s2 = setlxSum[$enableIgnore] {$c = Equal($s1.s,$s2.s) }
		| '!=' s2 = setlxSum[$enableIgnore] {$c = NotEqual($s1.s,$s2.s) }
		| '<' s2 = setlxSum[$enableIgnore] {$c = LessThan($s1.s,$s2.s) }
		| '<=' s2 = setlxSum[$enableIgnore] {$c = LessOrEqual($s1.s,$s2.s) }
		| '>' s2 = setlxSum[$enableIgnore] {$c = GreaterThan($s1.s,$s2.s) }
		| '>=' s2 = setlxSum[$enableIgnore] {$c = GreaterOrEqual($s1.s,$s2.s) }
		| 'in' s2 = setlxSum[$enableIgnore] {$c = SetlXIn($s1.s,$s2.s) }
		| 'notin' s2 = setlxSum[$enableIgnore] {$c = NotIn($s1.s,$s2.s) }
	)?;

setlxSum[enableIgnore]
	returns[s]:
	p1 = product[$enableIgnore] {$s = $p1.p} (
		'+' p2 = product[$enableIgnore] {$s = Sum($p1.p,$p2.p) }
		| '-' p2 = product[$enableIgnore] {$s = Difference($p1.p,$p2.p) }
	)*;

product[enableIgnore]
	returns[p]:
	r1 = setlxReduce[$enableIgnore] {$p = $r1.r} (
		'*' r2 = setlxReduce[$enableIgnore] {$p = Product($p,$r2.r) }
		| '/' r2 = setlxReduce[$enableIgnore] {$p = Quotient($p,$r2.r) }
		| '\\' r2 = setlxReduce[$enableIgnore] {$p = IntegerDivision($p,$r2.r) }
		| '%' r2 = setlxReduce[$enableIgnore] {$p = Modulo($p,$r2.r) }
		| '><' r2 = setlxReduce[$enableIgnore] {$p = CartesianProduct($p,$r2.r) }
	)*;

setlxReduce[enableIgnore]
	returns[r]:
	p1 = prefixOperation[$enableIgnore] {$r = $p1.p} (
		// TODO what does this do??
		'+/' p2 = prefixOperation[$enableIgnore] {$r = SumOfMembersBinary($r,$p2.p) }
		| '*/' p2 = prefixOperation[$enableIgnore] {$r = ProductOfMembersBinary($r,$p2.p) }
	)*;

prefixOperation[enableIgnore]
	returns[p]:
	factor[$enableIgnore] {$p = $factor.f} (
		'**' prefixOperation[$enableIgnore] {$p = Power($p,$prefixOperation.p) }
	)?
	| '+/' prefixOperation[$enableIgnore] {$p = SumOfMembers($prefixOperation.p) }
	| '*/' prefixOperation[$enableIgnore] {$p = ProductOfMembers($prefixOperation.p) }
	| '#' prefixOperation[$enableIgnore] {$p = Cardinality($prefixOperation.p) }
	| '-' prefixOperation[$enableIgnore] {$p = Minus($prefixOperation.p)};

factor[enableIgnore]
	returns[f]:
	'!' factor[$enableIgnore] {$f = SetlXNot($factor.f) }
	//| TERM '(' termArguments[$operators] ')' {operators.append(TermConstructor($TERM.text,
	// $termArguments.args.size())) }
	| 'forall' '(' iteratorChain[$enableIgnore] '|' condition ')' {$f = Forall($iteratorChain.ic,$condition.cnd)
		}
	| 'exists' '(' iteratorChain[$enableIgnore] '|' condition ')' {$f = Exists($iteratorChain.ic,$condition.cnd)
		}
	| (
		'(' exprContent[$enableIgnore] ')' {$f = $exprContent.ex }
		| procedure[None] {$f = $procedure.pd }
		| variable {$f = $variable.v }
	) (
		'.' variable {$f = MemberAccess($f,$variable.v) }
		| call[$enableIgnore,$f] {$f = $call.c }
	)* ('!' {$f = Factorial($f) })?
	| value[$enableIgnore] {$f = $value.v } (
		'!' {$f = Factorial($value.v) }
	)?;

procedure[name]
	returns[pd]:
	'procedure' '(' procedureParameters[True] ')' '{' block '}' {$pd = Procedure($procedureParameters.paramList, $block.blk,$name,None) 
		}
	| 'cachedProcedure' '(' procedureParameters[False] ')' '{' block '}' {$pd = CachedProcedure($procedureParameters.paramList, $block.blk,$name) 
		}
	| 'closure' '(' procedureParameters[True] ')' '{' block '}' {$pd = Closure($procedureParameters.paramList, $block.blk) 
		};

procedureParameters[enableRw]
	returns[paramList]
	@init {
$paramList = []
    }:
	pp1 = procedureParameter[$enableRw] {$paramList.append($pp1.param) } (
		',' pp2 = procedureParameter[$enableRw] {$paramList.append($pp2.param) }
	)* (
		',' dp1 = procedureDefaultParameter {$paramList.append($dp1.param) }
	)* (
		',' lp1 = procedureListParameter {$paramList.append($lp1.param) } 
	)?
	| dp2 = procedureDefaultParameter {$paramList.append($dp2.param) } (
		',' dp3 = procedureDefaultParameter {$paramList.append($dp3.param) }
	)* (
		',' lp2 = procedureListParameter {$paramList.append($lp2.param) }
	)?
	| lp3 = procedureListParameter {$paramList.append($lp3.param) }
	| /* epsilon */;

procedureParameter[enableRw]
	returns[param]:
	{$enableRw}? 'rw' assignableVariable {$param = ReadWriteParameter($assignableVariable.v.id) }
	| variable {$param = Parameter($variable.v.id, None, False) };

procedureDefaultParameter
	returns[param]:
	assignableVariable ':=' expr[False] {$param = Parameter($assignableVariable.v.id, $expr.ex, False) };

procedureListParameter
	returns[param]:
	'*' variable {$param = ListParameter($variable.v.id) };

call[enableIgnore,callable]
	returns[c]:
	'(' callParameters[$enableIgnore] ')' {$c = FunctionCall($callParameters.params,$callable) 
		}
	| '[' collectionAccessParams[$enableIgnore] ']' {$c = CollectionAccess($collectionAccessParams.p,$callable) }
    | '{' expr[$enableIgnore] '}' {$c = CollectMap($expr.ex,$callable) }; 

collectionAccessParams[enableIgnore]
	returns[p]
	@init {
params = []
    }:
	e1 = expr[$enableIgnore] (
		RANGE_SIGN (
			e2 = expr[$enableIgnore] {$p = ListRange($e1.ex,$e2.ex) }
			| {$p = ListRange($e1.ex,None) }
		)
		| (',' e3 = expr[False] {params.append($e3.ex) })+ {$p = params }
		| {$p = $e1.ex }
	)
	| RANGE_SIGN expr[$enableIgnore] {$p = ListRange(None,$expr.ex) };

callParameters[enableIgnore]
	returns[params]
	@init {
$params = []
    }:
	exprList[$enableIgnore] {$params = $exprList.exprs} (
		 ',' '*' exprContent[False] {$params.append(OperatorExpression($exprContent.ex))}
    )?
	| '*' exprContent[False] {$params = [OperatorExpression($exprContent.ex)]}
	| /* epsilon */;

value[enableIgnore]
	returns[v]
	@init {
cb = None
    }:
	'[' (
		collectionBuilder[$enableIgnore] {cb = $collectionBuilder.cb; }
	)? ']' {$v = SetlXList(cb) }
	| '{' (
		collectionBuilder[$enableIgnore] {cb = $collectionBuilder.cb; }
	)? '}' {$v = SetListConstructor(cb) }
	| STRING {$v = SetlXString($STRING.text) }
	| LITERAL {$v = SetlXLiteral($LITERAL.text) }
	// TODO | matrix {$v = new ValueOperator($matrix.m); }
	// TODO | vector {$v = new ValueOperator($vector.v); }
	| atomicValue {$v = $atomicValue.av }
	| {$enableIgnore}? '_' {$v = VariableIgnore() };

collectionBuilder[enableIgnore]
	returns[cb]
	@init {
exprs = []
    }:
	e1 = expr[$enableIgnore] (
		',' e2 = expr[$enableIgnore] (
			RANGE_SIGN e3 = expr[$enableIgnore] {$cb = Range($e1.ex, $e2.ex, $e3.ex) }
			| {exprs.append($e1.ex); exprs.append($e2.ex) } (
				',' e3 = expr[$enableIgnore] {exprs.append($e3.ex) }
			)* (
				'|' e4 = expr[False] {$cb = ExplicitListWithRest(exprs, $e4.ex) }
				| /* epsilon */ {$cb = ExplicitList(exprs)         }
			)
		)
		| RANGE_SIGN e3 = expr[$enableIgnore] {$cb = Range($e1.ex, None, $e3.ex) }
		| {exprs.append($e1.ex) } (
			'|' e2 = expr[False] {$cb = ExplicitListWithRest(exprs, $e2.ex) }
			| /* epsilon */ {$cb = ExplicitList(exprs)         }
		)
		| ':' iteratorChain[$enableIgnore] (
			'|' c1 = condition {$cb = SetlIteration($e1.ex, $iteratorChain.ic, $c1.cnd) }
			| /* epsilon */ {$cb = SetlIteration($e1.ex, $iteratorChain.ic, None) }
		)
	);

iteratorChain[enableIgnore]
	returns[ic]
	@init {
$ic = []
    }:
	i1 = iterator[$enableIgnore] {$ic.append($i1.iter)} (
		',' i2 = iterator[$enableIgnore] {$ic.append($i2.iter) }
	)*;

iterator[enableIgnore]
	returns[iter]:
	assignable[True] 'in' expr[$enableIgnore] {$iter = SetlIterator($assignable.a, $expr.ex) };

atomicValue
	returns[Value av]:
	NUMBER {$av = SetlXFraction($NUMBER.text) }
	| DOUBLE {$av = SetlXDouble($DOUBLE.text) }
	| 'om' {$av = SetlXOm() }
	| 'true' {$av = SetlXTrue() }
	| 'false' {$av = SetlXFalse() };

variable
	returns[Variable v]: ID {$v = Variable($ID.text) };

condition
	returns[cnd]:
	expr[False] {$cnd = Condition($expr.ex) };

assignmentList
	returns[al]
	@init {
$al = []
    }:
	a1 = assignable[True] {$al.append($a1.a) } (
		',' a2 = assignable[True] {$al.append($a2.a) }
	)*;

ID: ('a' .. 'z' | 'A' .. 'Z') (
		'a' .. 'z'
		| 'A' .. 'Z'
		| '_'
		| '0' .. '9'
	)*;
// TERM: ('@' | '@@@') ID;
NUMBER: '0' | ('1' .. '9') ('0' .. '9')*;
DOUBLE:
	NUMBER? '.' ('0' .. '9')+ (
		('e' | 'E') ('+' | '-')? ('0' .. '9')+
	)?;
RANGE_SIGN: '..';
STRING: '"' ('\\' . | ~('"' | '\\'))* '"';
LITERAL: '\'' ('\'\'' | ~('\''))* '\'';

LINE_COMMENT: '//' ~('\n' | '\r')* -> skip;
MULTI_COMMENT:
	'/*' (~('*') | '*'+ ~('*' | '/'))* '*'+ '/' -> skip;
WS: (' ' | '\t' | '\n' | '\r')+ -> skip;

REMAINDER: .;