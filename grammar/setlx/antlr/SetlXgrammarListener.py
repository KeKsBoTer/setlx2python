# Generated from SetlXgrammar.g4 by ANTLR 4.7.1
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .SetlXgrammarParser import SetlXgrammarParser
else:
    from SetlXgrammarParser import SetlXgrammarParser

from grammar.setlx.block import *
from grammar.setlx.statements import *
from grammar.setlx.types import *


# This class defines a complete listener for a parse tree produced by SetlXgrammarParser.
class SetlXgrammarListener(ParseTreeListener):

    # Enter a parse tree produced by SetlXgrammarParser#block.
    def enterBlock(self, ctx:SetlXgrammarParser.BlockContext):
        pass

    # Exit a parse tree produced by SetlXgrammarParser#block.
    def exitBlock(self, ctx:SetlXgrammarParser.BlockContext):
        pass


    # Enter a parse tree produced by SetlXgrammarParser#statement.
    def enterStatement(self, ctx:SetlXgrammarParser.StatementContext):
        pass

    # Exit a parse tree produced by SetlXgrammarParser#statement.
    def exitStatement(self, ctx:SetlXgrammarParser.StatementContext):
        pass


    # Enter a parse tree produced by SetlXgrammarParser#assignmentDirect.
    def enterAssignmentDirect(self, ctx:SetlXgrammarParser.AssignmentDirectContext):
        pass

    # Exit a parse tree produced by SetlXgrammarParser#assignmentDirect.
    def exitAssignmentDirect(self, ctx:SetlXgrammarParser.AssignmentDirectContext):
        pass


    # Enter a parse tree produced by SetlXgrammarParser#assignable.
    def enterAssignable(self, ctx:SetlXgrammarParser.AssignableContext):
        pass

    # Exit a parse tree produced by SetlXgrammarParser#assignable.
    def exitAssignable(self, ctx:SetlXgrammarParser.AssignableContext):
        pass


    # Enter a parse tree produced by SetlXgrammarParser#assignableVariable.
    def enterAssignableVariable(self, ctx:SetlXgrammarParser.AssignableVariableContext):
        pass

    # Exit a parse tree produced by SetlXgrammarParser#assignableVariable.
    def exitAssignableVariable(self, ctx:SetlXgrammarParser.AssignableVariableContext):
        pass


    # Enter a parse tree produced by SetlXgrammarParser#expr.
    def enterExpr(self, ctx:SetlXgrammarParser.ExprContext):
        pass

    # Exit a parse tree produced by SetlXgrammarParser#expr.
    def exitExpr(self, ctx:SetlXgrammarParser.ExprContext):
        pass


    # Enter a parse tree produced by SetlXgrammarParser#exprList.
    def enterExprList(self, ctx:SetlXgrammarParser.ExprListContext):
        pass

    # Exit a parse tree produced by SetlXgrammarParser#exprList.
    def exitExprList(self, ctx:SetlXgrammarParser.ExprListContext):
        pass


    # Enter a parse tree produced by SetlXgrammarParser#exprContent.
    def enterExprContent(self, ctx:SetlXgrammarParser.ExprContentContext):
        pass

    # Exit a parse tree produced by SetlXgrammarParser#exprContent.
    def exitExprContent(self, ctx:SetlXgrammarParser.ExprContentContext):
        pass


    # Enter a parse tree produced by SetlXgrammarParser#implication.
    def enterImplication(self, ctx:SetlXgrammarParser.ImplicationContext):
        pass

    # Exit a parse tree produced by SetlXgrammarParser#implication.
    def exitImplication(self, ctx:SetlXgrammarParser.ImplicationContext):
        pass


    # Enter a parse tree produced by SetlXgrammarParser#disjunction.
    def enterDisjunction(self, ctx:SetlXgrammarParser.DisjunctionContext):
        pass

    # Exit a parse tree produced by SetlXgrammarParser#disjunction.
    def exitDisjunction(self, ctx:SetlXgrammarParser.DisjunctionContext):
        pass


    # Enter a parse tree produced by SetlXgrammarParser#conjunction.
    def enterConjunction(self, ctx:SetlXgrammarParser.ConjunctionContext):
        pass

    # Exit a parse tree produced by SetlXgrammarParser#conjunction.
    def exitConjunction(self, ctx:SetlXgrammarParser.ConjunctionContext):
        pass


    # Enter a parse tree produced by SetlXgrammarParser#comparison.
    def enterComparison(self, ctx:SetlXgrammarParser.ComparisonContext):
        pass

    # Exit a parse tree produced by SetlXgrammarParser#comparison.
    def exitComparison(self, ctx:SetlXgrammarParser.ComparisonContext):
        pass


    # Enter a parse tree produced by SetlXgrammarParser#setlxSum.
    def enterSetlxSum(self, ctx:SetlXgrammarParser.SetlxSumContext):
        pass

    # Exit a parse tree produced by SetlXgrammarParser#setlxSum.
    def exitSetlxSum(self, ctx:SetlXgrammarParser.SetlxSumContext):
        pass


    # Enter a parse tree produced by SetlXgrammarParser#product.
    def enterProduct(self, ctx:SetlXgrammarParser.ProductContext):
        pass

    # Exit a parse tree produced by SetlXgrammarParser#product.
    def exitProduct(self, ctx:SetlXgrammarParser.ProductContext):
        pass


    # Enter a parse tree produced by SetlXgrammarParser#setlxReduce.
    def enterSetlxReduce(self, ctx:SetlXgrammarParser.SetlxReduceContext):
        pass

    # Exit a parse tree produced by SetlXgrammarParser#setlxReduce.
    def exitSetlxReduce(self, ctx:SetlXgrammarParser.SetlxReduceContext):
        pass


    # Enter a parse tree produced by SetlXgrammarParser#prefixOperation.
    def enterPrefixOperation(self, ctx:SetlXgrammarParser.PrefixOperationContext):
        pass

    # Exit a parse tree produced by SetlXgrammarParser#prefixOperation.
    def exitPrefixOperation(self, ctx:SetlXgrammarParser.PrefixOperationContext):
        pass


    # Enter a parse tree produced by SetlXgrammarParser#factor.
    def enterFactor(self, ctx:SetlXgrammarParser.FactorContext):
        pass

    # Exit a parse tree produced by SetlXgrammarParser#factor.
    def exitFactor(self, ctx:SetlXgrammarParser.FactorContext):
        pass


    # Enter a parse tree produced by SetlXgrammarParser#call.
    def enterCall(self, ctx:SetlXgrammarParser.CallContext):
        pass

    # Exit a parse tree produced by SetlXgrammarParser#call.
    def exitCall(self, ctx:SetlXgrammarParser.CallContext):
        pass


    # Enter a parse tree produced by SetlXgrammarParser#callParameters.
    def enterCallParameters(self, ctx:SetlXgrammarParser.CallParametersContext):
        pass

    # Exit a parse tree produced by SetlXgrammarParser#callParameters.
    def exitCallParameters(self, ctx:SetlXgrammarParser.CallParametersContext):
        pass


    # Enter a parse tree produced by SetlXgrammarParser#value.
    def enterValue(self, ctx:SetlXgrammarParser.ValueContext):
        pass

    # Exit a parse tree produced by SetlXgrammarParser#value.
    def exitValue(self, ctx:SetlXgrammarParser.ValueContext):
        pass


    # Enter a parse tree produced by SetlXgrammarParser#atomicValue.
    def enterAtomicValue(self, ctx:SetlXgrammarParser.AtomicValueContext):
        pass

    # Exit a parse tree produced by SetlXgrammarParser#atomicValue.
    def exitAtomicValue(self, ctx:SetlXgrammarParser.AtomicValueContext):
        pass


    # Enter a parse tree produced by SetlXgrammarParser#variable.
    def enterVariable(self, ctx:SetlXgrammarParser.VariableContext):
        pass

    # Exit a parse tree produced by SetlXgrammarParser#variable.
    def exitVariable(self, ctx:SetlXgrammarParser.VariableContext):
        pass


    # Enter a parse tree produced by SetlXgrammarParser#assignmentList.
    def enterAssignmentList(self, ctx:SetlXgrammarParser.AssignmentListContext):
        pass

    # Exit a parse tree produced by SetlXgrammarParser#assignmentList.
    def exitAssignmentList(self, ctx:SetlXgrammarParser.AssignmentListContext):
        pass


