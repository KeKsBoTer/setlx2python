grammar SetlXgrammar;

@parser::header {
from grammar.setlx.block import *
from grammar.setlx.statements import *
from grammar.setlx.types import *
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
expression = None
condition = None
    }:
	'if' '(' c1 = condition ')' '{' b1 = block '}' (
		'else' 'if' '(' c2 = condition ')' '{' b2 = block '}' {else_list.append(IfThenBranch($c2.cnd,$b2.blk)) }
	)* (
		'else' '{' b3 = block '}' {else_list.append($b3.blk) }
	)? {$stmnt = IfThen($c1.cnd,$b1.blk,else_list) }
	| 'for' '(' iteratorChain[False] (
		'|' condition {condition = $condition.cnd}
	)? ')' '{' block '}' {$stmnt = For($iteratorChain.ic, condition, $block.blk) }
	| 'while' '(' condition ')' '{' block '}' {$stmnt = While($condition.cnd, $block.blk) }
	| 'do' '{' block '}' 'while' '(' condition ')' ';' {$stmnt = DoWhile($condition.cnd, $block.blk) 
		}
	| 'backtrack' ';' {$stmnt = Backtrack() }
	| 'break' ';' {$stmnt = Break() }
	| 'continue' ';' {$stmnt = Continue() }
	| 'exit' ';' {$stmnt = Exit() }
	| 'return' (expr[False] {expression = $expr.ex })? ';' {$stmnt = Return(expression) }
	| assignmentOther ';' {$stmnt = $assignmentOther.assign }
	| assignmentDirect ';' {$stmnt = $assignmentDirect.assign }
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

assignmentDirect
	returns[assign]:
	// special case for transpiler: name := procedure(){...}
	variable ':=' procedure {
$procedure.pd.name = $variable.v.id
$assign = $procedure.pd
    }
	| assignable[False] ':=' (
		assignmentDirect {$assign = Assignment($assignable.a, $assignmentDirect.assign) }
		| exprContent[False] {$assign = Assignment($assignable.a, $exprContent.ex) }
	);

assignable[enableIgnore]
	returns[a]:
	assignableVariable {$a = $assignableVariable.v} (
		'.' variable {$a = AssignableMember($a, $variable.v)}
		| '[' exprList[False] ']' {$a = AssignableCollectionAccess($a)}
	)*
	| '[' assignmentList ']' {$a = AssignableList($assignmentList.al)}
	| {$enableIgnore}? '_' {$a = AssignableIgnore()};

assignableVariable
	returns[v]: ID {$v = AssignableVariable($ID.text) };

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
	// TODO : lambdaProcedure          { operators.add(new ProcedureConstructor($lambdaProcedure.lp)); }
	implication[$enableIgnore] {$ex = $implication.i} (
		'<==>' implication[$enableIgnore] {$ex = BooleanEqual($ex,$implication.i) }
		| '<!=>' implication[$enableIgnore] {$ex = BooleanNotEqual($ex,$implication.i) }
	)?;

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
		| 'in' s2 = setlxSum[$enableIgnore] {$c = In($s1.s,$s2.s) }
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
		// TODO | '><' setlxReduce[$enableIgnore] { operators.add(CartesianProduct.CP); }
	)*;

setlxReduce[enableIgnore]
	returns[r]:
	p1 = prefixOperation[$enableIgnore] {$r =$p1.p}
	/* TODO ( '+/' prefixOperation[$enableIgnore, $operators] {
	 operators.add(SumOfMembersBinary.SOMB ); } | '*\(remove this backslash)/'
	 prefixOperation[$enableIgnore, $operators] { operators.add(ProductOfMembersBinary.POMB); } )*
	 */;

prefixOperation[enableIgnore]
	returns[p]:
	factor[$enableIgnore] {$p = $factor.f} (
		'**' prefixOperation[$enableIgnore] {$p = Power($p,$prefixOperation.p) }
	)?
	//| '+/' prefixOperation[$enableIgnore, $operators] { operators.add(SumOfMembers.SOM); } |
	// '*\(remove this backslash)/' prefixOperation[$enableIgnore, $operators] {
	// operators.add(ProductOfMembers.POM); } | '#' prefixOperation[$enableIgnore, $operators] {
	// operators.add(Cardinality.C); }
	| '-' prefixOperation[$enableIgnore] {$p = Minus($prefixOperation.p)};

factor[enableIgnore]
	returns[f]:
	'!' factor[$enableIgnore] {$f = Not($factor.f) }
	/* TODO | TERM '(' termArguments[$operators] ')' { operators.add(new TermConstructor($TERM.text,
	 $termArguments.args.size())); } | 'forall' '(' iteratorChain[$enableIgnore] '|' condition ')' {
	 operators.add(new Forall($iteratorChain.ic, $condition.cnd)); } | 'exists' '('
	 iteratorChain[$enableIgnore] '|' condition ')' { operators.add(new Exists($iteratorChain.ic,
	 $condition.cnd)); }
	 */
	| (
		'(' exprContent[$enableIgnore] ')' {$f = $exprContent.ex }
		| procedure {$f = $procedure.pd }
		| variable {$f = $variable.v }
	) (
		'.' variable {$f = MemberAccess($f,$variable.v) }
		| call[$enableIgnore] {
$call.c.callable = $f
$f = $call.c
        }
	)* ('!' {$f = Factorial($f) })?
	| value[$enableIgnore] {$f = $value.v } (
		'!' {$f = Factorial($value.v) }
	)?;

procedure
	returns[pd]:
	'procedure' '(' procedureParameters[True] ')' '{' block '}' {$pd = Procedure($procedureParameters.paramList, $block.blk) 
		}
	/* TODO| 'cachedProcedure' '(' procedureParameters[False] ')' '{' block '}' {$pd =
	 CachedProcedure($procedureParameters.paramList, $block.blk) } | 'closure' '('
	 procedureParameters[True] ')' '{' block '}' {$pd = Closure($procedureParameters.paramList,
	 $block.blk) }
	 */;

procedureParameters[enableRw]
	returns[paramList]
	@init {
$paramList = []
    }:
	pp1 = procedureParameter[$enableRw] {$paramList.append($pp1.param) } (
		',' pp2 = procedureParameter[$enableRw] {$paramList.append($pp2.param) }
	)* (
		',' dp1 = procedureDefaultParameter {$paramList.append($dp1.param) }
	)*
	/* TODO ( ',' lp1 = procedureListParameter {$paramList.append($lp1.param) } )?
	 */
	| dp2 = procedureDefaultParameter {$paramList.append($dp2.param) } (
		',' dp3 = procedureDefaultParameter {$paramList.append($dp3.param) }
	)*
	/* TODO( ',' lp2 = procedureListParameter {$paramList.append($lp2.param) } )?
	 */
	//| lp3 = procedureListParameter {$paramList.append($lp3.param) }
	| /* epsilon */;

procedureParameter[enableRw]
	returns[param]:
	// TODO {$enableRw}? 'rw' assignableVariable {$param =
	// ReadWriteParameter($assignableVariable.v.ID) } \
	variable {$param = Parameter($variable.v.id) };

procedureDefaultParameter
	returns[param]:
	assignableVariable ':=' expr[False] {$param = Parameter($assignableVariable.v.id, $expr.ex) };

call[enableIgnore]
	returns[c]:
	'(' callParameters[$enableIgnore] ')' {$c = FunctionCall($callParameters.params, $callParameters.ex) 
		}
	| '[' collectionAccessParams[$enableIgnore] ']' {$c = CollectionAccess($collectionAccessParams.p)
		};
/* TODO | '{' expr[$enableIgnore] '}' {$c = CollectMap($expr.ex) };
 */

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
	returns[ params, ex]
	@init {
$params = []
$ex = None
    }:
	exprList[$enableIgnore] {$params = $exprList.exprs}
	/* TODO unpack parameters( ',' '*' exprContent[False] {$ex =
	 OperatorExpression(listArgumentOperators)} )? | '*' exprContent[False] {$ex =
	 OperatorExpression(listArgumentOperators)}
	 */
	| /* epsilon */;

value[enableIgnore]
	returns[v]
	@init {
cb = None
    }:
	'[' (
		collectionBuilder[$enableIgnore] {cb = $collectionBuilder.cb; }
	)? ']' {$v = SetlXList(cb) }
	/* TODO | '{' (collectionBuilder[$enableIgnore] { cb = $collectionBuilder.cb; } )? '}' {$v = new
	 SetListConstructor(CollectionType.SET, cb); }
	 */
	| STRING {$v = SetlXString($STRING.text) }
	| LITERAL {$v = SetlXLiteral($LITERAL.text) }
	// TODO | matrix {$v = new ValueOperator($matrix.m); } TODO | vector {$v = new
	// ValueOperator($vector.v); }
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
	| DOUBLE {$av = float($DOUBLE.text) }
	| 'om' {$av = SetlXOm() }
	| 'True' {$av = SetlXTrue() }
	| 'False' {$av = SetlXFalse() };

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