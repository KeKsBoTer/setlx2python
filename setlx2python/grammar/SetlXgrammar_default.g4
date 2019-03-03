grammar SetlXgrammar;

@parser::header {

from grammar.setlx.types import *
from grammar.setlx.statements import *
from grammar.setlx.assignments import *
from grammar.setlx.operators import *
from grammar.setlx.conditions import *

}

@parser::members {
}

block
	returns[blk]
	@init {
stmnts = []

    }: (
		statement {if $statement.stmnt != None: stmnts.append($statement.stmnt)}
	)* {$blk = Block(stmnts)};

statement
	returns[stmnt]
	@init {
ifList     = []
caseList   = []
matchList  = []
tryList    = []
condition  = None
block      = None
expression = None
    }:
	'class' ID '(' procedureParameters[True] ')' '{' b1 = block (
		'static' '{' b2 = block '}' {block = $b2.blk}
	)? '}' {$stmnt = ClassConstructor($ID.text, SetlClass($procedureParameters.paramList, $b1.blk, block))
		}
	| 'if' '(' c1 = condition ')' '{' b1 = block '}' {ifList.append( IfThenBranch($c1.cnd, $b1.blk))             
		} (
		'else' 'if' '(' c2 = condition ')' '{' b2 = block '}' {ifList.append( IfThenElseIfBranch($c2.cnd, $b2.blk))       
			}
	)* (
		'else' '{' b3 = block '}' {ifList.append( IfThenElseBranch($b3.blk))                  }
	)? {$stmnt = IfThen(ifList) }
	| 'switch' '{' (
		'case' c1 = condition ':' b1 = block {caseList.append( SwitchCaseBranch($c1.cnd, $b1.blk))       
			}
	)* (
		'default' ':' b2 = block {caseList.append( SwitchDefaultBranch($b2.blk))             }
	)? '}' {$stmnt = Switch(caseList) }
	/*| match {$stmnt = $match.m;                                          }*/
	| scan {$stmnt = $scan.s;                                           }
	| 'for' '(' iteratorChain[False] (
		'|' condition {condition = $condition.cnd;}
	)? ')' '{' block '}' {$stmnt = For($iteratorChain.ic, condition, $block.blk) }
	| 'while' '(' condition ')' '{' block '}' {$stmnt = While($condition.cnd, $block.blk)             
		}
	| 'do' '{' block '}' 'while' '(' condition ')' ';' {$stmnt = DoWhile($condition.cnd, $block.blk)           
		}
	| 'try' '{' b1 = block '}' (
		'catchLng' '(' v1 = assignableVariable ')' '{' b2 = block '}' {tryList.append( TryCatchLngBranch($v1.v, $b2.blk))         
			}
		| 'catchUsr' '(' v1 = assignableVariable ')' '{' b2 = block '}' {tryList.append( TryCatchUsrBranch($v1.v, $b2.blk))         
			}
	)* (
		'catch' '(' v2 = assignableVariable ')' '{' b3 = block '}' {tryList.append(TryCatchBranch($v2.v, $b3.blk))         
			}
	)? {$stmnt = TryCatch($b1.blk, tryList) }
	| 'check' '{' b1 = block '}' (
		'afterBacktrack' '{' b2 = block {block = $b2.blk} '}'
	)? {$stmnt = Check($b1.blk, block)                         }
	| 'backtrack' ';' {$stmnt = Backtrack.BT                                     }
	| 'break' ';' {$stmnt = Break.B                                           }
	| 'continue' ';' {$stmnt = Continue.C                                       }
	| 'exit' ';' {$stmnt = Exit.E                                            }
	| 'return' (expr[False] {expression = $expr.ex; })? ';' {$stmnt = Return(expression)                            
		}
	| 'assert' '(' condition ',' expr[False] ')' ';' {$stmnt = None if setlXstate.areAssertsDisabled() else Assert($condition.cnd, $expr.ex)
		}
	| assignmentOther ';' {$stmnt = $assignmentOther.assign }
	| assignmentDirect ';' {$stmnt = $assignmentDirect.assign }
	| expr[False] ';' {$stmnt = $expr.ex};
/*
 match
 returns[m]
 @init {
 matchList = []
 condition = None
 }:
 'match' '(' expr[False] ')' '{'
 (
 'case' exprList[True, None] (
 '|' c1 = condition {condition = $c1.cnd}
 )? ':' b1 = block
 {matchList.append(MatchCaseBranch($exprList.exprs, condition, $b1.blk))}{condition = None}
 |
 regexBranch {matchList.append($regexBranch.rb)}
 )+ (
 'default' ':' b4 = block {matchList.append(
 MatchDefaultBranch($b4.blk))}
 )? '}' {$m = Match($expr.ex, matchList)};
 */
scan
	returns[Scan s]
	@init {
scanList  = []
posVar    = None
    }:
	'scan' '(' expr[False] ')' (
		'using' assignableVariable {posVar = $assignableVariable.v}
	)? '{' (regexBranch {scanList.append($regexBranch.rb)})+ (
		'default' ':' block {scanList.append( MatchDefaultBranch($block.blk)) }
	)? '}' {$s = Scan($expr.ex, posVar, scanList)} {posVar = None};

regexBranch
	returns[MatchRegexBranch rb]
	@init {
assignTo = None
condition = None
    }:
	'regex' pattern = expr[False] (
		'as' assign = expr[True] {assignTo = $assign.ex}
	)? ('|' condition {condition = $condition.cnd})? ':' block {$rb = MatchRegexBranch(setlXstate, $pattern.ex, assignTo, condition, $block.blk)
		} {assignTo = None} {condition = None};

assignableVariable
	returns[AssignableVariable v]:
	ID {$v = AssignableVariable($ID.text) };

variable
	returns[Variable v]: ID {$v = Variable($ID.text) };

condition
	returns[Condition cnd]:
	expr[False] {$cnd = Condition($expr.ex) };

exprList[ enableIgnore,  operators]
	returns[ exprs]
	@init {
$exprs = []
expressionOperators = []
    }:
	exprContent[$enableIgnore, expressionOperators] {
$exprs.append(OperatorExpression(expressionOperators))
if operators != None:
	operators.extend(expressionOperators)
expressionOperators = []
} 	(
		',' exprContent[$enableIgnore, expressionOperators] {
$exprs.append(OperatorExpression(expressionOperators))
if operators != None:
	operators.extend(expressionOperators)
expressionOperators = []
}
	)*;

assignmentOther
	returns[Statement assign]:
	assignable[False] (
		'+=' e = expr[False] {$assign = SumAssignment($assignable.a, $e.ex) }
		| '-=' e = expr[False] {$assign = DifferenceAssignment($assignable.a, $e.ex) }
		| '*=' e = expr[False] {$assign = ProductAssignment($assignable.a, $e.ex) }
		| '/=' e = expr[False] {$assign = QuotientAssignment($assignable.a, $e.ex) }
		| '\\=' e = expr[False] {$assign = IntegerDivisionAssignment($assignable.a, $e.ex) }
		| '%=' e = expr[False] {$assign = ModuloAssignment($assignable.a, $e.ex) }
	);

assignmentDirect
	returns[OperatorExpression assign]
	@init {
operators = []
    }:
	assignmentDirectContent[operators] {$assign = OperatorExpression(operators) };

assignmentDirectContent[operators]
	returns[Assignment assign]
	@init{
content = None
	}:
	assignable[False] ':=' (
		assignmentDirectContent[operators] {content = $assignmentDirectContent.assign}
		| exprContent[False, operators] {content = $exprContent.ex}
	) {assign = Assignment($assignable.a, content)};

assignable[ enableIgnore]
	returns[AAssignableExpression a]:
	assignableVariable {$a = $assignableVariable.v} (
		'.' variable {$a = AssignableMember($a, $variable.v)}
		| '[' exprList[False, None] ']' {$a = AssignableCollectionAccess($a, $exprList.exprs)}
	)*
	| '[' assignmentList ']' {$a = AssignableList($assignmentList.al)}
	| {$enableIgnore}? '_' {$a = AssignableIgnore.AI};

assignmentList
	returns[ al]
	@init {
$al = []
    }:
	a1 = assignable[True] {$al.append($a1.a) } (
		',' a2 = assignable[True] {$al.append($a2.a) }
	)*;

expr[ enableIgnore]
	returns[OperatorExpression ex]
	@init {
operators = []
    }:
	exprContent[$enableIgnore, operators] {$ex = OperatorExpression(operators) };

exprContent[ enableIgnore,  operators]
	returns[ex]:
	lambdaProcedure {operators.append(ProcedureConstructor($lambdaProcedure.lp)) }
	| implication[$enableIgnore, $operators] (
		'<==>' implication[$enableIgnore, $operators] {operators.append(BooleanEqual.BE)     }
		| '<!=>' implication[$enableIgnore, $operators] {operators.append(BooleanNotEqual.BNE) }
	)?;

lambdaProcedure
	returns[Procedure lp]:
	lambdaParameters (
		'|->' expr[False] {$lp = LambdaProcedure($lambdaParameters.paramList, $expr.ex) }
		| '|=>' expr[False] {$lp = LambdaClosure($lambdaParameters.paramList, $expr.ex)   }
	);

lambdaParameters
	returns[ParameterList paramList]
	@init {
$paramList = ParameterList()
    }:
	variable {$paramList.append(Parameter($variable.v.ID)) }
	| '[' (
		v1 = variable {$paramList.append( Parameter($v1.v.ID))} (
			',' v2 = variable {$paramList.append( Parameter($v2.v.ID))}
		)*
	)? ']';

implication[ enableIgnore,  operators]:
	disjunction[$enableIgnore, $operators] (
		{innerOperators = []} '=>' implication[$enableIgnore, innerOperators] {operators.append(Implication(OperatorExpression(innerOperators))) 
			}
	)?;

disjunction[ enableIgnore,  operators]:
	conjunction[$enableIgnore, $operators] (
		{innerOperators = [] } '||' conjunction[$enableIgnore, innerOperators] {operators.append(Disjunction(OperatorExpression(innerOperators))) 
			}
	)*;

conjunction[ enableIgnore,  operators]:
	comparison[$enableIgnore, $operators] (
		{innerOperators = []} '&&' comparison[$enableIgnore, innerOperators] {operators.append(Conjunction(OperatorExpression(innerOperators))) 
			}
	)*;

comparison[ enableIgnore,  operators]:
	setlxsum[$enableIgnore, $operators] (
		'==' setlxsum[$enableIgnore, $operators] {operators.append(Equals.E) }
		| '!=' setlxsum[$enableIgnore, $operators] {operators.append(NotEqual.NE) }
		| '<' setlxsum[$enableIgnore, $operators] {operators.append(LessThan.LT) }
		| '<=' setlxsum[$enableIgnore, $operators] {operators.append(LessOrEqual.LOE) }
		| '>' setlxsum[$enableIgnore, $operators] {operators.append(GreaterThan.GT) }
		| '>=' setlxsum[$enableIgnore, $operators] {operators.append(GreaterOrEqual.GOE) }
		| 'in' setlxsum[$enableIgnore, $operators] {operators.append(In.I) }
		| 'notin' setlxsum[$enableIgnore, $operators] {operators.append(NotIn.NI) }
	)?;

setlxsum[ enableIgnore,  operators]:
	product[$enableIgnore, $operators] (
		'+' product[$enableIgnore, $operators] {operators.append(Sum.S)        }
		| '-' product[$enableIgnore, $operators] {operators.append(Difference.D) }
	)*;

product[ enableIgnore,  operators]:
	setlxreduce[$enableIgnore, $operators] (
		'*' setlxreduce[$enableIgnore, $operators] {operators.append(Product.P)           }
		| '/' setlxreduce[$enableIgnore, $operators] {operators.append(Quotient.Q)          }
		| '\\' setlxreduce[$enableIgnore, $operators] {operators.append(IntegerDivision.ID)  }
		| '%' setlxreduce[$enableIgnore, $operators] {operators.append(Modulo.M)            }
		| '><' setlxreduce[$enableIgnore, $operators] {operators.append(CartesianProduct.CP) }
	)*;

setlxreduce[ enableIgnore,  operators]:
	p1 = prefixOperation[$enableIgnore, $operators] (
		'+/' prefixOperation[$enableIgnore, $operators] {operators.append(SumOfMembersBinary.SOMB    ) 
			}
		| '*/' prefixOperation[$enableIgnore, $operators] {operators.append(ProductOfMembersBinary.POMB) 
			}
	)*;

prefixOperation[ enableIgnore,  operators]:
	factor[$enableIgnore, $operators] (
		'**' prefixOperation[$enableIgnore, $operators] {operators.append(Power.P)              }
	)?
	| '+/' prefixOperation[$enableIgnore, $operators] {operators.append(SumOfMembers.SOM)     }
	| '*/' prefixOperation[$enableIgnore, $operators] {operators.append(ProductOfMembers.POM) }
	| '#' prefixOperation[$enableIgnore, $operators] {operators.append(Cardinality.C)        }
	| '-' prefixOperation[$enableIgnore, $operators] {operators.append(Minus.M)              };

factor[ enableIgnore,  operators]:
	'!' factor[$enableIgnore, $operators] {operators.append(Not.N) }
	| TERM '(' termArguments[$operators] ')' {operators.append(TermConstructor($TERM.text, $termArguments.args.size())) 
		}
	| 'forall' '(' iteratorChain[$enableIgnore] '|' condition ')' {operators.append(Forall($iteratorChain.ic, $condition.cnd)) 
		}
	| 'exists' '(' iteratorChain[$enableIgnore] '|' condition ')' {operators.append(Exists($iteratorChain.ic, $condition.cnd)) 
		}
	| (
		'(' exprContent[$enableIgnore, $operators] ')'
		| procedure {operators.append( ProcedureConstructor($procedure.pd)) }
		| variable {operators.append($variable.v)                             }
	) (
		'.' variable {operators.append(MemberAccess($variable.v))           }
		| call[$enableIgnore, $operators] {operators.append($call.c)                                 
			}
	)* (
		'!' {operators.append(Factorial.F)                             }
	)?
	| value[$enableIgnore] {operators.append($value.v)                                } (
		'!' {operators.append(Factorial.F)                             }
	)?;

termArguments[ operators]
	returns[ args]:
	exprList[True, $operators] {$args = $exprList.exprs                       }
	| /* epsilon */ {$args = [] };

procedure
	returns[Procedure pd]:
	'procedure' '(' procedureParameters[True] ')' '{' block '}' {$pd = Procedure($procedureParameters.paramList, $block.blk)       
		}
	| 'cachedProcedure' '(' procedureParameters[False] ')' '{' block '}' {$pd = CachedProcedure($procedureParameters.paramList, $block.blk) 
		}
	| 'closure' '(' procedureParameters[True] ')' '{' block '}' {$pd = Closure($procedureParameters.paramList, $block.blk)         
		};

procedureParameters[ enableRw]
	returns[ParameterList paramList]
	@init {
$paramList = ParameterList()
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

procedureParameter[ enableRw]
	returns[ParameterDefinition param]:
	{$enableRw}? 'rw' assignableVariable {$param = ReadWriteParameter($assignableVariable.v.ID) 
		}
	| variable {$param = Parameter($variable.v.ID)  };

procedureDefaultParameter
	returns[Parameter param]:
	assignableVariable ':=' expr[False] {$param = Parameter($assignableVariable.v.ID, $expr.ex) 
		};

procedureListParameter
	returns[ListParameter param]:
	'*' variable {$param = ListParameter($variable.v.ID) };

call[ enableIgnore,  operators]
	returns[AOperator c]:
	'(' callParameters[$enableIgnore] ')' {$c = Call($callParameters.params, $callParameters.ex) 
		}
	| '[' collectionAccessParams[$enableIgnore] ']' {$c = CollectionAccess($collectionAccessParams.params) 
		}
	| '{' expr[$enableIgnore] '}' {$c = CollectMap($expr.ex)                             };

callParameters[ enableIgnore]
	returns[ params, OperatorExpression ex]
	@init {
$params                                       = []
$ex                                           = None
listArgumentOperators = []
ops = []
    }:
	exprList[$enableIgnore, ops] {$params = $exprList.exprs} (
		',' '*' exprContent[False, listArgumentOperators] {
$ex     = OperatorExpression(listArgumentOperators)
	}
	)?
	| '*' exprContent[False, listArgumentOperators] {
$ex     = OperatorExpression(listArgumentOperators)
		}
	| /* epsilon */;

collectionAccessParams[ enableIgnore]
	returns[ params]
	@init {
$params = []
    }:
	e1 = expr[$enableIgnore] {$params.append($e1.ex)                             } (
		RANGE_SIGN {$params.append(CollectionAccessRangeDummy.CARD_OE) } (
			e2 = expr[$enableIgnore] {$params.append($e2.ex)                             }
		)?
		| (
			',' e3 = expr[False] {$params.append($e3.ex)                             }
		)+
	)?
	| RANGE_SIGN {$params.append(CollectionAccessRangeDummy.CARD_OE) } expr[$enableIgnore] {$params.append($expr.ex)                           
		};

value[ enableIgnore]
	returns[AZeroOperator v]
	@init {
cb = None
    }:
	'[' (
		collectionBuilder[$enableIgnore] {cb = $collectionBuilder.cb }
	)? ']' {$v = SetListConstructor(CollectionType.LIST, cb)  }
	| '{' (
		collectionBuilder[$enableIgnore] {cb = $collectionBuilder.cb }
	)? '}' {$v = SetListConstructor(CollectionType.SET, cb)   }
	| STRING {$v = String($STRING.text)  }
	| LITERAL {$v = Literal($LITERAL.text)            }
	| matrix {$v = ValueOperator($matrix.m)                     }
	| vector {$v = ValueOperator($vector.v)                     }
	| atomicValue {$v = ValueOperator($atomicValue.av)               }
	| {$enableIgnore}? '_' {$v = VariableIgnore.VI                            };

collectionBuilder[ enableIgnore]
	returns[CollectionBuilder cb]
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
			| /* epsilon */ {$cb = SetlIteration($e1.ex, $iteratorChain.ic, None   ) }
		)
	);

iteratorChain[ enableIgnore]
	returns[SetlIterator ic]:
	i1 = iterator[$enableIgnore] {$ic = $i1.iter} (
		',' i2 = iterator[$enableIgnore] {$ic.append($i2.iter) }
	)*;

iterator[ enableIgnore]
	returns[SetlIterator iter]:
	assignable[True] 'in' expr[$enableIgnore] {$iter = SetlIterator($assignable.a, $expr.ex) };

matrix
	returns[SetlMatrix m]
	@init {
vectors = []
    }:
	'<<' (vector {vectors.append($vector.v)       })+ '>>' {$m = SetlMatrix(setlXstate, vectors) };

vector
	returns[SetlVector v]
	@init {
doubles  = []
negative = "";
dbl      = 0.0;
    }:
	'<<' (
		('-' {negative = "-" } | /* epsilon */ {negative = ""  }) (
			n1 = NUMBER {dbl = float(negative + $n1.text)     }
			| DOUBLE {dbl = float(negative + $DOUBLE.text) }
		) ('/' n2 = NUMBER {dbl /= float(negative + $n2.text) })? {doubles.append(dbl) }
	)+ '>>' {$v = SetlVector(doubles) };

atomicValue
	returns[Value av]:
	NUMBER {$av = SetlXFraction($NUMBER.text)    }
	| DOUBLE {$av = float($DOUBLE.text)       }
	| 'om' {$av = None;                     }
	| 'True' {$av = TRUE;                     }
	| 'False' {$av = FALSE;                    };

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

/*
 * This is the desperate attempt at counting mismatched characters as errors
 instead of the lexers
 * default behavior of emitting an error message,
 consuming the character and continuing without
 * counting it as an error.
 
 Using this rule all unknown characters are added to the token stream
 * and the parser will stumble over them, reporting "mismatched input".
 
 Matching any character
 * here works, because the lexer matches rules in order.
 */

REMAINDER: .;

