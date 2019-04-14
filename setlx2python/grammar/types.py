from collections import namedtuple as nt
AssignableCollectionAccess = nt('AssignableCollectionAccess',['assignable', 'exprs'])
AssignableIgnore = nt('AssignableIgnore',[])
AssignableList = nt('AssignableList',['assignables'])
AssignableMember = nt('AssignableMember',['parent', 'member'])
AssignableVariable = nt('AssignableVariable',['id'])
Assignment = nt('Assignment',['assignables', 'right_hand_side'])
AssignmentOther = nt('AssignmentOther',['assignable', 'right_hand_side', 'operator'])
Backtrack = nt('Backtrack',[])
BinOperator = nt('BinOperator',['left', 'right', 'operator'])
Block = nt('Block',['stmnts'])
BooleanEqual = nt('BooleanEqual',['left', 'right'])
BooleanNotEqual = nt('BooleanNotEqual',['left', 'right'])
CachedProcedure = nt('CachedProcedure',['params', 'block'])
Cardinality = nt('Cardinality',['expr'])
CartesianProduct = nt('CartesianProduct',['left', 'right'])
Check = nt('Check',['check_block','backtack_block'])
ClassConstructor = nt('ClassConstructor',['id', 'params', 'block', 'static_block'])
Closure = nt('Closure',['params','block'])
CollectionAccess = nt('CollectionAccess',['params','callable'])
CollectMap = nt("CollectMap",["expr","callable"])
Compare = nt('Compare',['left', 'right', 'operator'])
Condition = nt('Condition',['expression'])
Conjunction = nt('Conjunction',['left', 'right'])
Difference = nt('Difference',['left', 'right'])
DifferenceAssignment = nt('DifferenceAssignment',['assignable', 'right_hand_side'])
Disjunction = nt('Disjunction',['left', 'right'])
DoWhile = nt('DoWhile',['condition', 'block'])
Equal = nt('Equal',['left', 'right'])
Exists = nt('Exists',['iter_chain', 'condition'])
Exit = nt('Exit',[])
ExplicitList = nt('ExplicitList',['exprs'])
ExplicitListWithRest = nt('ExplicitListWithRest',['exprs','rest'])
Factorial = nt('Factorial',['expr'])
Forall = nt('Forall',['iter_chain', 'condition'])
FunctionCall = nt('FunctionCall',['params','callable'])
GreaterOrEqual = nt('GreaterOrEqual',['left', 'right'])
GreaterThan = nt('GreaterThan',['left', 'right'])
IfThen = nt('IfThen',['condition', 'block', 'else_list'])
IfThenBranch = nt('IfThenBranch',['condition', 'block', 'orelse'])
Implication = nt('Implication',['left', 'right'])
SetlXIn = nt("SetlXIn",['left', 'right'])
InfixOperator = nt('InfixOperator',['left', 'right'])
IntegerDivision = nt('IntegerDivision',['left', 'right'])
IntegerDivisionAssignment = nt('IntegerDivisionAssignment',['assignable', 'right_hand_side'])
LambdaClosure = nt('LambdaClosure',['params', 'expr'])
LambdaProcedure = nt('LambdaProcedure',['params', 'expr'])
LessOrEqual = nt('LessOrEqual',['left', 'right'])
LessThan = nt('LessThan',['left', 'right'])
ListParameter = nt('ListParameter',['id'])
ListRange = nt('ListRange',['start', 'end'])
Match = nt('Match',[])
MemberAccess = nt('MemberAccess',['parent', 'child'])
Minus = nt('Minus',['expr'])
Modulo = nt('Modulo',['left', 'right'])
ModuloAssignment = nt('ModuloAssignment',['assignable', 'right_hand_side'])
NotEqual = nt('NotEqual',['left', 'right'])
NotIn = nt('NotIn',['left', 'right'])
OperatorExpression = nt('OperatorExpression',['expr'])
Parameter = nt('Parameter',['id', 'default'])
Power = nt('Power',['base','exponent'])
PrefixOperator = nt('PrefixOperator',['expr', 'py_target_type'])
Procedure = nt('Procedure',['params', 'block'])
ProcedureDefinition = nt('ProcedureDefinition',['procedure', 'name'])
Product = nt('Product',['left', 'right'])
ProductAssignment = nt('ProductAssignment',['assignable', 'right_hand_side'])
ProductOfMembers = nt('ProductOfMembers',['expr'])
ProductOfMembersBinary = nt('ProductOfMembersBinary',['left', 'right'])
Quotient = nt('Quotient',['left', 'right'])
QuotientAssignment = nt('QuotientAssignment',['assignable', 'right_hand_side'])
Range = nt('Range',['start', 'step', 'end'])
ReadWriteParameter = nt('ReadWriteParameter',['id'])
Scan = nt('Scan',[])
SetListConstructor = nt('SetListConstructor',['collection'])
SetlIteration = nt('SetlIteration',['expr', 'iter_chain', 'condition'])
SetlIterator = nt('SetlIterator',['assignable', 'expression'])
SetlMatrix = nt('SetlMatrix',['vectors'])
SetlVector = nt('SetlVector',['values'])
SetlXAssert = nt('SetlXAssert',['condition', 'expr'])
SetlXBreak = nt('SetlXBreak',[])
SetlXContinue = nt('SetlXContinue',[])
SetlXDouble = nt('SetlXDouble',['value'])
SetlXFalse = nt('SetlXFalse',[])
SetlXFraction = nt('SetlXFraction',["number"])
SetlXList = nt('SetlXList',['cb'])
SetlXLiteral = nt('SetlXLiteral',['value'])
SetlXNot = nt('SetlXNot',['expr'])
SetlXOm = nt('SetlXOm',[])
SetlXReturn = nt('SetlXReturn',['expression'])
SetlXString = nt('SetlXString',['string'])
SetlXTrue = nt('SetlXTrue',[])
SetlXWhile = nt('SetlXWhile',['condition', 'block'])
SetlXFor = nt('SetlXFor',['iteratorChain', 'condition', 'block'])
Sum = nt('Sum',['left', 'right'])
SumAssignment = nt('SumAssignment',['assignable', 'right_hand_side'])
SumOfMembers = nt('SumOfMembers',['expr'])
SumOfMembersBinary = nt('SumOfMembersBinary',['left', 'right'])
Switch = nt('Switch',['case_list', 'default_branch'])
Term = nt('Term',[])
TryCatch = nt('TryCatch',['block', 'try_list'])
TryCatchBranch = nt('TryCatchBranch',['variable', 'block'])
TryCatchLngBranch = nt('TryCatchLngBranch',['variable','block'])
TryCatchUsrBranch = nt('TryCatchUsrBranch',['variable','block'])
Variable = nt('Variable',['id'])
VariableIgnore = nt('VariableIgnore',[])
WithLevel = nt('WithLevel',['level', 'code'])