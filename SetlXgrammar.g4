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
	returns[stmnt]:
  // assignmentOther ';' {$stmnt = $assignmentOther.assign }
	/*/ */ assignmentDirect ';' {$stmnt = $assignmentDirect.assign }
	| expr[False] ';' {$stmnt = $expr.ex};

/* 
assignmentOther
	returns[assign]:
	assignable[False]
  (
		'+=' e = expr[False] {$assign = SumAssignment($assignable.a, $e.ex) }
		| '-=' e = expr[False] {$assign = DifferenceAssignment($assignable.a, $e.ex) }
		| '*=' e = expr[False] {$assign = ProductAssignment($assignable.a, $e.ex) }
		| '/=' e = expr[False] {$assign = QuotientAssignment($assignable.a, $e.ex) }
		| '\\=' e = expr[False] {$assign = IntegerDivisionAssignment($assignable.a, $e.ex) }
		| '%=' e = expr[False] {$assign = ModuloAssignment($assignable.a, $e.ex) }
	);
*/

assignmentDirect
	returns[Assignment assign]:
	assignable[False] ':=' (
		assignmentDirect {$assign = Assignment($assignable.a, $assignmentDirect.assign)
			}
		| exprContent[False] {$assign = Assignment($assignable.a, $exprContent.ex)}
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
	returns[AssignableVariable v]:
	ID {$v = AssignableVariable($ID.text) };


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

exprContent [enableIgnore]
  returns[ex]:
  // TODO : lambdaProcedure          { operators.add(new ProcedureConstructor($lambdaProcedure.lp)); }
  implication[$enableIgnore] {$ex = $implication.i}
  /* TODO  (
      '<==>' implication[$enableIgnore, $operators] { operators.add(BooleanEqual.BE);     }
    | '<!=>' implication[$enableIgnore, $operators] { operators.add(BooleanNotEqual.BNE); }
    )?*/
  ;


implication [enableIgnore]
  returns[i]: 
  disjunction[$enableIgnore] {$i = $disjunction.d}
    /* TODO (
      { FragmentList<AOperator> innerOperators = new FragmentList<AOperator>(); }
      '=>' implication[$enableIgnore, innerOperators] { operators.add(new Implication(new OperatorExpression(innerOperators))); }
    )?*/
  ;

disjunction [enableIgnore]
  returns[d]: 
  conjunction[$enableIgnore] {$d = $conjunction.c}
  /* TODO (
      { FragmentList<AOperator> innerOperators = new FragmentList<AOperator>(); }
      '||' conjunction[$enableIgnore, innerOperators] { operators.add(new Disjunction(new OperatorExpression(innerOperators))); }
    )*
    */
  ;

conjunction [enableIgnore]
  returns[c]: 
  comparison[$enableIgnore] {$c = $comparison.c}
  /* TODO (
      { FragmentList<AOperator> innerOperators = new FragmentList<AOperator>(); }
      '&&' comparison[$enableIgnore, innerOperators] { operators.add(new Conjunction(new OperatorExpression(innerOperators))); }
    )*
    */
  ;

comparison [enableIgnore]
  returns[c]: 
  s1 = setlxSum[$enableIgnore] {$c = $s1.s }
    (
        '=='    s2 = setlxSum[$enableIgnore] {$c = Equal($s1.s,$s2.s) }
      | '!='    s2 = setlxSum[$enableIgnore] {$c = NotEqual($s1.s,$s2.s) }
      | '<'     s2 = setlxSum[$enableIgnore] {$c = LessThan($s1.s,$s2.s) }
      | '<='    s2 = setlxSum[$enableIgnore] {$c = LessOrEqual($s1.s,$s2.s) }
      | '>'     s2 = setlxSum[$enableIgnore] {$c = GreaterThan($s1.s,$s2.s) }
      | '>='    s2 = setlxSum[$enableIgnore] {$c = GreaterOrEqual($s1.s,$s2.s) }
      | 'in'    s2 = setlxSum[$enableIgnore] {$c = In($s1.s,$s2.s) }
      | 'notin' s2 = setlxSum[$enableIgnore] {$c = NotIn($s1.s,$s2.s) }
    )?
  ;

setlxSum [enableIgnore]
  returns[s]:
  p1 = product[$enableIgnore] {$s = $p1.p}
    (
        '+' p2 = product[$enableIgnore] {$s = Sum($p1.p,$p2.p) }
      | '-' p2 = product[$enableIgnore] {$s = Difference($p1.p,$p2.p) }
    )*
  ;

product [enableIgnore]
  returns[p]:
  r1 = setlxReduce[$enableIgnore] {$p = $r1.r}
  /* TODO (
        '*'  setlxReduce[$enableIgnore, $operators] { operators.add(Product.P);           }
      | '/'  setlxReduce[$enableIgnore, $operators] { operators.add(Quotient.Q);          }
      | '\\' setlxReduce[$enableIgnore, $operators] { operators.add(IntegerDivision.ID);  }
      | '%'  setlxReduce[$enableIgnore, $operators] { operators.add(Modulo.M);            }
      | '><' setlxReduce[$enableIgnore, $operators] { operators.add(CartesianProduct.CP); }
    )*
    */
  ;

setlxReduce [enableIgnore]
  returns[r]:
  p1 = prefixOperation[$enableIgnore] {$r =$p1.p}
  /* TODO  (
        '+/' prefixOperation[$enableIgnore, $operators] { operators.add(SumOfMembersBinary.SOMB    ); }
      | '*\(remove this backslash)/' prefixOperation[$enableIgnore, $operators] { operators.add(ProductOfMembersBinary.POMB); }
    )*
  */
  ;

prefixOperation [enableIgnore]
  returns[p]:
  factor[$enableIgnore] {$p = $factor.f}
  /* TODO  (
      '**' prefixOperation[$enableIgnore, $operators] { operators.add(Power.P);              }
    )?
  | '+/' prefixOperation[$enableIgnore, $operators]   { operators.add(SumOfMembers.SOM);     }
  | '*\(remove this backslash)/' prefixOperation[$enableIgnore, $operators]   { operators.add(ProductOfMembers.POM); }
  | '#'  prefixOperation[$enableIgnore, $operators]   { operators.add(Cardinality.C);        }
  | '-'  prefixOperation[$enableIgnore, $operators]   { operators.add(Minus.M);              }
  */
  ;

factor [enableIgnore]
  returns[f]:
  /* TODO '!' factor[$enableIgnore, $operators] { operators.add(Not.N); }
  | TERM '(' termArguments[$operators] ')'
    { operators.add(new TermConstructor($TERM.text, $termArguments.args.size())); }
  | 'forall' '(' iteratorChain[$enableIgnore] '|' condition ')'
    { operators.add(new Forall($iteratorChain.ic, $condition.cnd)); }
  | 'exists' '(' iteratorChain[$enableIgnore] '|' condition ')'
    { operators.add(new Exists($iteratorChain.ic, $condition.cnd)); }
  */(
      '(' exprContent[$enableIgnore] ')' {$f = $exprContent.ex }
      // TODO | procedure                        {$f = $procedure.p }
      | variable                         {$f = $variable.v }
    )
    (
        '.' variable                    {$f = MemberAccess($f,$variable.v) }
        | call[$enableIgnore]           {$f = $call.c }
    )*
    (
      '!'                              {$f = Factorial($f) }
    )?
  |
  value[$enableIgnore]  {$f = $value.v }
    (
      '!' {$f = Factorial($value.v) }
    )?
  ;

call[enableIgnore]
	returns[c]:
	'(' callParameters[$enableIgnore] ')' {$c = Call($callParameters.params, $callParameters.ex) };
	/* TODO | '[' collectionAccessParams[$enableIgnore] ']' {$c = CollectionAccess($collectionAccessParams.params) 
	//	}
	| '{' expr[$enableIgnore] '}' {$c = CollectMap($expr.ex)                             };
  */

callParameters[enableIgnore]
	returns[ params, ex]
	@init {
$params                                       = []
$ex                                           = None
    }:
	exprList[$enableIgnore] {$params = $exprList.exprs}
  /* TODO unpack parameters(
		',' '*' exprContent[False] {$ex = OperatorExpression(listArgumentOperators)}
	)?
	| '*' exprContent[False] {$ex = OperatorExpression(listArgumentOperators)}
	*/
  | /* epsilon */;

value [enableIgnore]
  returns[v]:
  /* TODO '[' (collectionBuilder[$enableIgnore] { cb = $collectionBuilder.cb; } )? ']'
                          {$v = new SetListConstructor(CollectionType.LIST, cb);  }
  | '{' (collectionBuilder[$enableIgnore] { cb = $collectionBuilder.cb; } )? '}'
                          {$v = new SetListConstructor(CollectionType.SET, cb);   }
  |*/ STRING               {$v = SetlXString($STRING.text) }
  | LITERAL              {$v = SetlXLiteral($LITERAL.text) }
  // TODO | matrix               {$v = new ValueOperator($matrix.m);                     }
  // TODO | vector               {$v = new ValueOperator($vector.v);                     }
  | atomicValue          {$v = $atomicValue.av }
  | {$enableIgnore}? '_' {$v = VariableIgnore() }
  ;

atomicValue
	returns[Value av]:
	NUMBER {$av = SetlXFraction($NUMBER.text) }
	| DOUBLE {$av = float($DOUBLE.text) }
	| 'om' {$av = SetlXOm() }
	| 'True' {$av = TRUE }
	| 'False' {$av = FALSE };

variable
	returns[Variable v]: ID {$v = Variable($ID.text) };

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
TERM: ('@' | '@@@') ID;
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