# Generated from SetlXgrammar.g4 by ANTLR 4.7.1
# encoding: utf-8
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys


from grammar.setlx.block import *
from grammar.setlx.statements import *
from grammar.setlx.types import *

def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3#")
        buf.write("\u0115\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\3\2")
        buf.write("\3\2\3\2\7\2\64\n\2\f\2\16\2\67\13\2\3\2\3\2\3\3\3\3\3")
        buf.write("\3\3\3\3\3\3\3\3\3\3\3\5\3C\n\3\3\4\3\4\3\4\3\4\3\4\3")
        buf.write("\4\3\4\3\4\5\4M\n\4\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3")
        buf.write("\5\3\5\3\5\7\5Z\n\5\f\5\16\5]\13\5\3\5\3\5\3\5\3\5\3\5")
        buf.write("\3\5\3\5\3\5\5\5g\n\5\3\6\3\6\3\6\3\7\3\7\3\7\3\b\3\b")
        buf.write("\3\b\3\b\3\b\3\b\7\bu\n\b\f\b\16\bx\13\b\3\t\3\t\3\t\3")
        buf.write("\n\3\n\3\n\3\13\3\13\3\13\3\f\3\f\3\f\3\r\3\r\3\r\3\r")
        buf.write("\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3")
        buf.write("\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r")
        buf.write("\3\r\3\r\3\r\5\r\u00a8\n\r\3\16\3\16\3\16\3\16\3\16\3")
        buf.write("\16\3\16\3\16\3\16\3\16\7\16\u00b4\n\16\f\16\16\16\u00b7")
        buf.write("\13\16\3\17\3\17\3\17\3\20\3\20\3\20\3\21\3\21\3\21\3")
        buf.write("\22\3\22\3\22\3\22\3\22\3\22\3\22\3\22\5\22\u00ca\n\22")
        buf.write("\3\22\3\22\3\22\3\22\3\22\3\22\3\22\7\22\u00d3\n\22\f")
        buf.write("\22\16\22\u00d6\13\22\3\22\3\22\5\22\u00da\n\22\3\22\3")
        buf.write("\22\3\22\3\22\5\22\u00e0\n\22\5\22\u00e2\n\22\3\23\3\23")
        buf.write("\3\23\3\23\3\23\3\24\3\24\3\24\3\24\5\24\u00ed\n\24\3")
        buf.write("\25\3\25\3\25\3\25\3\25\3\25\3\25\3\25\3\25\3\25\5\25")
        buf.write("\u00f9\n\25\3\26\3\26\3\26\3\26\3\26\3\26\3\26\3\26\3")
        buf.write("\26\3\26\5\26\u0105\n\26\3\27\3\27\3\27\3\30\3\30\3\30")
        buf.write("\3\30\3\30\3\30\7\30\u0110\n\30\f\30\16\30\u0113\13\30")
        buf.write("\3\30\2\2\31\2\4\6\b\n\f\16\20\22\24\26\30\32\34\36 \"")
        buf.write("$&(*,.\2\2\2\u011e\2\65\3\2\2\2\4B\3\2\2\2\6D\3\2\2\2")
        buf.write("\bf\3\2\2\2\nh\3\2\2\2\fk\3\2\2\2\16n\3\2\2\2\20y\3\2")
        buf.write("\2\2\22|\3\2\2\2\24\177\3\2\2\2\26\u0082\3\2\2\2\30\u0085")
        buf.write("\3\2\2\2\32\u00a9\3\2\2\2\34\u00b8\3\2\2\2\36\u00bb\3")
        buf.write("\2\2\2 \u00be\3\2\2\2\"\u00e1\3\2\2\2$\u00e3\3\2\2\2&")
        buf.write("\u00ec\3\2\2\2(\u00f8\3\2\2\2*\u0104\3\2\2\2,\u0106\3")
        buf.write("\2\2\2.\u0109\3\2\2\2\60\61\5\4\3\2\61\62\b\2\1\2\62\64")
        buf.write("\3\2\2\2\63\60\3\2\2\2\64\67\3\2\2\2\65\63\3\2\2\2\65")
        buf.write("\66\3\2\2\2\668\3\2\2\2\67\65\3\2\2\289\b\2\1\29\3\3\2")
        buf.write("\2\2:;\5\6\4\2;<\7\3\2\2<=\b\3\1\2=C\3\2\2\2>?\5\f\7\2")
        buf.write("?@\7\3\2\2@A\b\3\1\2AC\3\2\2\2B:\3\2\2\2B>\3\2\2\2C\5")
        buf.write("\3\2\2\2DE\5\b\5\2EL\7\4\2\2FG\5\6\4\2GH\b\4\1\2HM\3\2")
        buf.write("\2\2IJ\5\20\t\2JK\b\4\1\2KM\3\2\2\2LF\3\2\2\2LI\3\2\2")
        buf.write("\2M\7\3\2\2\2NO\5\n\6\2O[\b\5\1\2PQ\7\5\2\2QR\5,\27\2")
        buf.write("RS\b\5\1\2SZ\3\2\2\2TU\7\6\2\2UV\5\16\b\2VW\7\7\2\2WX")
        buf.write("\b\5\1\2XZ\3\2\2\2YP\3\2\2\2YT\3\2\2\2Z]\3\2\2\2[Y\3\2")
        buf.write("\2\2[\\\3\2\2\2\\g\3\2\2\2][\3\2\2\2^_\7\6\2\2_`\5.\30")
        buf.write("\2`a\7\7\2\2ab\b\5\1\2bg\3\2\2\2cd\6\5\2\3de\7\b\2\2e")
        buf.write("g\b\5\1\2fN\3\2\2\2f^\3\2\2\2fc\3\2\2\2g\t\3\2\2\2hi\7")
        buf.write("\32\2\2ij\b\6\1\2j\13\3\2\2\2kl\5\20\t\2lm\b\7\1\2m\r")
        buf.write("\3\2\2\2no\5\20\t\2ov\b\b\1\2pq\7\t\2\2qr\5\20\t\2rs\b")
        buf.write("\b\1\2su\3\2\2\2tp\3\2\2\2ux\3\2\2\2vt\3\2\2\2vw\3\2\2")
        buf.write("\2w\17\3\2\2\2xv\3\2\2\2yz\5\22\n\2z{\b\t\1\2{\21\3\2")
        buf.write("\2\2|}\5\24\13\2}~\b\n\1\2~\23\3\2\2\2\177\u0080\5\26")
        buf.write("\f\2\u0080\u0081\b\13\1\2\u0081\25\3\2\2\2\u0082\u0083")
        buf.write("\5\30\r\2\u0083\u0084\b\f\1\2\u0084\27\3\2\2\2\u0085\u0086")
        buf.write("\5\32\16\2\u0086\u00a7\b\r\1\2\u0087\u0088\7\n\2\2\u0088")
        buf.write("\u0089\5\32\16\2\u0089\u008a\b\r\1\2\u008a\u00a8\3\2\2")
        buf.write("\2\u008b\u008c\7\13\2\2\u008c\u008d\5\32\16\2\u008d\u008e")
        buf.write("\b\r\1\2\u008e\u00a8\3\2\2\2\u008f\u0090\7\f\2\2\u0090")
        buf.write("\u0091\5\32\16\2\u0091\u0092\b\r\1\2\u0092\u00a8\3\2\2")
        buf.write("\2\u0093\u0094\7\r\2\2\u0094\u0095\5\32\16\2\u0095\u0096")
        buf.write("\b\r\1\2\u0096\u00a8\3\2\2\2\u0097\u0098\7\16\2\2\u0098")
        buf.write("\u0099\5\32\16\2\u0099\u009a\b\r\1\2\u009a\u00a8\3\2\2")
        buf.write("\2\u009b\u009c\7\17\2\2\u009c\u009d\5\32\16\2\u009d\u009e")
        buf.write("\b\r\1\2\u009e\u00a8\3\2\2\2\u009f\u00a0\7\20\2\2\u00a0")
        buf.write("\u00a1\5\32\16\2\u00a1\u00a2\b\r\1\2\u00a2\u00a8\3\2\2")
        buf.write("\2\u00a3\u00a4\7\21\2\2\u00a4\u00a5\5\32\16\2\u00a5\u00a6")
        buf.write("\b\r\1\2\u00a6\u00a8\3\2\2\2\u00a7\u0087\3\2\2\2\u00a7")
        buf.write("\u008b\3\2\2\2\u00a7\u008f\3\2\2\2\u00a7\u0093\3\2\2\2")
        buf.write("\u00a7\u0097\3\2\2\2\u00a7\u009b\3\2\2\2\u00a7\u009f\3")
        buf.write("\2\2\2\u00a7\u00a3\3\2\2\2\u00a7\u00a8\3\2\2\2\u00a8\31")
        buf.write("\3\2\2\2\u00a9\u00aa\5\34\17\2\u00aa\u00b5\b\16\1\2\u00ab")
        buf.write("\u00ac\7\22\2\2\u00ac\u00ad\5\34\17\2\u00ad\u00ae\b\16")
        buf.write("\1\2\u00ae\u00b4\3\2\2\2\u00af\u00b0\7\23\2\2\u00b0\u00b1")
        buf.write("\5\34\17\2\u00b1\u00b2\b\16\1\2\u00b2\u00b4\3\2\2\2\u00b3")
        buf.write("\u00ab\3\2\2\2\u00b3\u00af\3\2\2\2\u00b4\u00b7\3\2\2\2")
        buf.write("\u00b5\u00b3\3\2\2\2\u00b5\u00b6\3\2\2\2\u00b6\33\3\2")
        buf.write("\2\2\u00b7\u00b5\3\2\2\2\u00b8\u00b9\5\36\20\2\u00b9\u00ba")
        buf.write("\b\17\1\2\u00ba\35\3\2\2\2\u00bb\u00bc\5 \21\2\u00bc\u00bd")
        buf.write("\b\20\1\2\u00bd\37\3\2\2\2\u00be\u00bf\5\"\22\2\u00bf")
        buf.write("\u00c0\b\21\1\2\u00c0!\3\2\2\2\u00c1\u00c2\7\24\2\2\u00c2")
        buf.write("\u00c3\5\20\t\2\u00c3\u00c4\7\25\2\2\u00c4\u00c5\b\22")
        buf.write("\1\2\u00c5\u00ca\3\2\2\2\u00c6\u00c7\5,\27\2\u00c7\u00c8")
        buf.write("\b\22\1\2\u00c8\u00ca\3\2\2\2\u00c9\u00c1\3\2\2\2\u00c9")
        buf.write("\u00c6\3\2\2\2\u00ca\u00d4\3\2\2\2\u00cb\u00cc\7\5\2\2")
        buf.write("\u00cc\u00cd\5,\27\2\u00cd\u00ce\b\22\1\2\u00ce\u00d3")
        buf.write("\3\2\2\2\u00cf\u00d0\5$\23\2\u00d0\u00d1\b\22\1\2\u00d1")
        buf.write("\u00d3\3\2\2\2\u00d2\u00cb\3\2\2\2\u00d2\u00cf\3\2\2\2")
        buf.write("\u00d3\u00d6\3\2\2\2\u00d4\u00d2\3\2\2\2\u00d4\u00d5\3")
        buf.write("\2\2\2\u00d5\u00d9\3\2\2\2\u00d6\u00d4\3\2\2\2\u00d7\u00d8")
        buf.write("\7\26\2\2\u00d8\u00da\b\22\1\2\u00d9\u00d7\3\2\2\2\u00d9")
        buf.write("\u00da\3\2\2\2\u00da\u00e2\3\2\2\2\u00db\u00dc\5(\25\2")
        buf.write("\u00dc\u00df\b\22\1\2\u00dd\u00de\7\26\2\2\u00de\u00e0")
        buf.write("\b\22\1\2\u00df\u00dd\3\2\2\2\u00df\u00e0\3\2\2\2\u00e0")
        buf.write("\u00e2\3\2\2\2\u00e1\u00c9\3\2\2\2\u00e1\u00db\3\2\2\2")
        buf.write("\u00e2#\3\2\2\2\u00e3\u00e4\7\24\2\2\u00e4\u00e5\5&\24")
        buf.write("\2\u00e5\u00e6\7\25\2\2\u00e6\u00e7\b\23\1\2\u00e7%\3")
        buf.write("\2\2\2\u00e8\u00e9\5\16\b\2\u00e9\u00ea\b\24\1\2\u00ea")
        buf.write("\u00ed\3\2\2\2\u00eb\u00ed\3\2\2\2\u00ec\u00e8\3\2\2\2")
        buf.write("\u00ec\u00eb\3\2\2\2\u00ed\'\3\2\2\2\u00ee\u00ef\7\37")
        buf.write("\2\2\u00ef\u00f9\b\25\1\2\u00f0\u00f1\7 \2\2\u00f1\u00f9")
        buf.write("\b\25\1\2\u00f2\u00f3\5*\26\2\u00f3\u00f4\b\25\1\2\u00f4")
        buf.write("\u00f9\3\2\2\2\u00f5\u00f6\6\25\3\3\u00f6\u00f7\7\b\2")
        buf.write("\2\u00f7\u00f9\b\25\1\2\u00f8\u00ee\3\2\2\2\u00f8\u00f0")
        buf.write("\3\2\2\2\u00f8\u00f2\3\2\2\2\u00f8\u00f5\3\2\2\2\u00f9")
        buf.write(")\3\2\2\2\u00fa\u00fb\7\34\2\2\u00fb\u0105\b\26\1\2\u00fc")
        buf.write("\u00fd\7\35\2\2\u00fd\u0105\b\26\1\2\u00fe\u00ff\7\27")
        buf.write("\2\2\u00ff\u0105\b\26\1\2\u0100\u0101\7\30\2\2\u0101\u0105")
        buf.write("\b\26\1\2\u0102\u0103\7\31\2\2\u0103\u0105\b\26\1\2\u0104")
        buf.write("\u00fa\3\2\2\2\u0104\u00fc\3\2\2\2\u0104\u00fe\3\2\2\2")
        buf.write("\u0104\u0100\3\2\2\2\u0104\u0102\3\2\2\2\u0105+\3\2\2")
        buf.write("\2\u0106\u0107\7\32\2\2\u0107\u0108\b\27\1\2\u0108-\3")
        buf.write("\2\2\2\u0109\u010a\5\b\5\2\u010a\u0111\b\30\1\2\u010b")
        buf.write("\u010c\7\t\2\2\u010c\u010d\5\b\5\2\u010d\u010e\b\30\1")
        buf.write("\2\u010e\u0110\3\2\2\2\u010f\u010b\3\2\2\2\u0110\u0113")
        buf.write("\3\2\2\2\u0111\u010f\3\2\2\2\u0111\u0112\3\2\2\2\u0112")
        buf.write("/\3\2\2\2\u0113\u0111\3\2\2\2\26\65BLY[fv\u00a7\u00b3")
        buf.write("\u00b5\u00c9\u00d2\u00d4\u00d9\u00df\u00e1\u00ec\u00f8")
        buf.write("\u0104\u0111")
        return buf.getvalue()


class SetlXgrammarParser ( Parser ):

    grammarFileName = "SetlXgrammar.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "';'", "':='", "'.'", "'['", "']'", "'_'", 
                     "','", "'=='", "'!='", "'<'", "'<='", "'>'", "'>='", 
                     "'in'", "'notin'", "'+'", "'-'", "'('", "')'", "'!'", 
                     "'om'", "'True'", "'False'", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "'..'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "ID", "TERM", "NUMBER", "DOUBLE", "RANGE_SIGN", "STRING", 
                      "LITERAL", "LINE_COMMENT", "MULTI_COMMENT", "WS" ]

    RULE_block = 0
    RULE_statement = 1
    RULE_assignmentDirect = 2
    RULE_assignable = 3
    RULE_assignableVariable = 4
    RULE_expr = 5
    RULE_exprList = 6
    RULE_exprContent = 7
    RULE_implication = 8
    RULE_disjunction = 9
    RULE_conjunction = 10
    RULE_comparison = 11
    RULE_setlxSum = 12
    RULE_product = 13
    RULE_setlxReduce = 14
    RULE_prefixOperation = 15
    RULE_factor = 16
    RULE_call = 17
    RULE_callParameters = 18
    RULE_value = 19
    RULE_atomicValue = 20
    RULE_variable = 21
    RULE_assignmentList = 22

    ruleNames =  [ "block", "statement", "assignmentDirect", "assignable", 
                   "assignableVariable", "expr", "exprList", "exprContent", 
                   "implication", "disjunction", "conjunction", "comparison", 
                   "setlxSum", "product", "setlxReduce", "prefixOperation", 
                   "factor", "call", "callParameters", "value", "atomicValue", 
                   "variable", "assignmentList" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    T__7=8
    T__8=9
    T__9=10
    T__10=11
    T__11=12
    T__12=13
    T__13=14
    T__14=15
    T__15=16
    T__16=17
    T__17=18
    T__18=19
    T__19=20
    T__20=21
    T__21=22
    T__22=23
    ID=24
    TERM=25
    NUMBER=26
    DOUBLE=27
    RANGE_SIGN=28
    STRING=29
    LITERAL=30
    LINE_COMMENT=31
    MULTI_COMMENT=32
    WS=33

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.7.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None



    class BlockContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.blk = None
            self._statement = None # StatementContext

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SetlXgrammarParser.StatementContext)
            else:
                return self.getTypedRuleContext(SetlXgrammarParser.StatementContext,i)


        def getRuleIndex(self):
            return SetlXgrammarParser.RULE_block

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBlock" ):
                listener.enterBlock(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBlock" ):
                listener.exitBlock(self)




    def block(self):

        localctx = SetlXgrammarParser.BlockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_block)

        stmnts = []
          
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 51
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,0,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 46
                    localctx._statement = self.statement()
                    stmnts.append(localctx._statement.stmnt) 
                self.state = 53
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,0,self._ctx)

            localctx.blk = Block(stmnts)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class StatementContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.stmnt = None
            self._assignmentDirect = None # AssignmentDirectContext
            self._expr = None # ExprContext

        def assignmentDirect(self):
            return self.getTypedRuleContext(SetlXgrammarParser.AssignmentDirectContext,0)


        def expr(self):
            return self.getTypedRuleContext(SetlXgrammarParser.ExprContext,0)


        def getRuleIndex(self):
            return SetlXgrammarParser.RULE_statement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStatement" ):
                listener.enterStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStatement" ):
                listener.exitStatement(self)




    def statement(self):

        localctx = SetlXgrammarParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_statement)
        try:
            self.state = 64
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 56
                localctx._assignmentDirect = self.assignmentDirect()
                self.state = 57
                self.match(SetlXgrammarParser.T__0)
                localctx.stmnt = localctx._assignmentDirect.assign 
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 60
                localctx._expr = self.expr(False)
                self.state = 61
                self.match(SetlXgrammarParser.T__0)
                localctx.stmnt = localctx._expr.ex
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class AssignmentDirectContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.assign = None
            self._assignable = None # AssignableContext
            self._assignmentDirect = None # AssignmentDirectContext
            self._exprContent = None # ExprContentContext

        def assignable(self):
            return self.getTypedRuleContext(SetlXgrammarParser.AssignableContext,0)


        def assignmentDirect(self):
            return self.getTypedRuleContext(SetlXgrammarParser.AssignmentDirectContext,0)


        def exprContent(self):
            return self.getTypedRuleContext(SetlXgrammarParser.ExprContentContext,0)


        def getRuleIndex(self):
            return SetlXgrammarParser.RULE_assignmentDirect

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAssignmentDirect" ):
                listener.enterAssignmentDirect(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAssignmentDirect" ):
                listener.exitAssignmentDirect(self)




    def assignmentDirect(self):

        localctx = SetlXgrammarParser.AssignmentDirectContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_assignmentDirect)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 66
            localctx._assignable = self.assignable(False)
            self.state = 67
            self.match(SetlXgrammarParser.T__1)
            self.state = 74
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
            if la_ == 1:
                self.state = 68
                localctx._assignmentDirect = self.assignmentDirect()
                localctx.assign = Assignment(localctx._assignable.a, localctx._assignmentDirect.assign)
                			
                pass

            elif la_ == 2:
                self.state = 71
                localctx._exprContent = self.exprContent(False)
                localctx.assign = Assignment(localctx._assignable.a, localctx._exprContent.ex)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class AssignableContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1, enableIgnore=None):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.enableIgnore = None
            self.a = None
            self._assignableVariable = None # AssignableVariableContext
            self._variable = None # VariableContext
            self._assignmentList = None # AssignmentListContext
            self.enableIgnore = enableIgnore

        def assignableVariable(self):
            return self.getTypedRuleContext(SetlXgrammarParser.AssignableVariableContext,0)


        def variable(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SetlXgrammarParser.VariableContext)
            else:
                return self.getTypedRuleContext(SetlXgrammarParser.VariableContext,i)


        def exprList(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SetlXgrammarParser.ExprListContext)
            else:
                return self.getTypedRuleContext(SetlXgrammarParser.ExprListContext,i)


        def assignmentList(self):
            return self.getTypedRuleContext(SetlXgrammarParser.AssignmentListContext,0)


        def getRuleIndex(self):
            return SetlXgrammarParser.RULE_assignable

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAssignable" ):
                listener.enterAssignable(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAssignable" ):
                listener.exitAssignable(self)




    def assignable(self, enableIgnore):

        localctx = SetlXgrammarParser.AssignableContext(self, self._ctx, self.state, enableIgnore)
        self.enterRule(localctx, 6, self.RULE_assignable)
        self._la = 0 # Token type
        try:
            self.state = 100
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 76
                localctx._assignableVariable = self.assignableVariable()
                localctx.a = localctx._assignableVariable.v
                self.state = 89
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==SetlXgrammarParser.T__2 or _la==SetlXgrammarParser.T__3:
                    self.state = 87
                    self._errHandler.sync(self)
                    token = self._input.LA(1)
                    if token in [SetlXgrammarParser.T__2]:
                        self.state = 78
                        self.match(SetlXgrammarParser.T__2)
                        self.state = 79
                        localctx._variable = self.variable()
                        localctx.a = AssignableMember(localctx.a, localctx._variable.v)
                        pass
                    elif token in [SetlXgrammarParser.T__3]:
                        self.state = 82
                        self.match(SetlXgrammarParser.T__3)
                        self.state = 83
                        self.exprList(False)
                        self.state = 84
                        self.match(SetlXgrammarParser.T__4)
                        localctx.a = AssignableCollectionAccess(localctx.a)
                        pass
                    else:
                        raise NoViableAltException(self)

                    self.state = 91
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 92
                self.match(SetlXgrammarParser.T__3)
                self.state = 93
                localctx._assignmentList = self.assignmentList()
                self.state = 94
                self.match(SetlXgrammarParser.T__4)
                localctx.a = AssignableList(localctx._assignmentList.al)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 97
                if not localctx.enableIgnore:
                    from antlr4.error.Errors import FailedPredicateException
                    raise FailedPredicateException(self, "$enableIgnore")
                self.state = 98
                self.match(SetlXgrammarParser.T__5)
                localctx.a = AssignableIgnore()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class AssignableVariableContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.v = None
            self._ID = None # Token

        def ID(self):
            return self.getToken(SetlXgrammarParser.ID, 0)

        def getRuleIndex(self):
            return SetlXgrammarParser.RULE_assignableVariable

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAssignableVariable" ):
                listener.enterAssignableVariable(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAssignableVariable" ):
                listener.exitAssignableVariable(self)




    def assignableVariable(self):

        localctx = SetlXgrammarParser.AssignableVariableContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_assignableVariable)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 102
            localctx._ID = self.match(SetlXgrammarParser.ID)
            localctx.v = AssignableVariable((None if localctx._ID is None else localctx._ID.text)) 
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ExprContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1, enableIgnore=None):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.enableIgnore = None
            self.ex = None
            self._exprContent = None # ExprContentContext
            self.enableIgnore = enableIgnore

        def exprContent(self):
            return self.getTypedRuleContext(SetlXgrammarParser.ExprContentContext,0)


        def getRuleIndex(self):
            return SetlXgrammarParser.RULE_expr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpr" ):
                listener.enterExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpr" ):
                listener.exitExpr(self)




    def expr(self, enableIgnore):

        localctx = SetlXgrammarParser.ExprContext(self, self._ctx, self.state, enableIgnore)
        self.enterRule(localctx, 10, self.RULE_expr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 105
            localctx._exprContent = self.exprContent(localctx.enableIgnore)
            localctx.ex = localctx._exprContent.ex 
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ExprListContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1, enableIgnore=None):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.enableIgnore = None
            self.exprs = None
            self._exprContent = None # ExprContentContext
            self.enableIgnore = enableIgnore

        def exprContent(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SetlXgrammarParser.ExprContentContext)
            else:
                return self.getTypedRuleContext(SetlXgrammarParser.ExprContentContext,i)


        def getRuleIndex(self):
            return SetlXgrammarParser.RULE_exprList

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExprList" ):
                listener.enterExprList(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExprList" ):
                listener.exitExprList(self)




    def exprList(self, enableIgnore):

        localctx = SetlXgrammarParser.ExprListContext(self, self._ctx, self.state, enableIgnore)
        self.enterRule(localctx, 12, self.RULE_exprList)

        localctx.exprs = []
          
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 108
            localctx._exprContent = self.exprContent(localctx.enableIgnore)
            localctx.exprs.append(localctx._exprContent.ex)
            self.state = 116
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==SetlXgrammarParser.T__6:
                self.state = 110
                self.match(SetlXgrammarParser.T__6)
                self.state = 111
                localctx._exprContent = self.exprContent(localctx.enableIgnore)
                localctx.exprs.append(localctx._exprContent.ex)
                self.state = 118
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ExprContentContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1, enableIgnore=None):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.enableIgnore = None
            self.ex = None
            self._implication = None # ImplicationContext
            self.enableIgnore = enableIgnore

        def implication(self):
            return self.getTypedRuleContext(SetlXgrammarParser.ImplicationContext,0)


        def getRuleIndex(self):
            return SetlXgrammarParser.RULE_exprContent

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExprContent" ):
                listener.enterExprContent(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExprContent" ):
                listener.exitExprContent(self)




    def exprContent(self, enableIgnore):

        localctx = SetlXgrammarParser.ExprContentContext(self, self._ctx, self.state, enableIgnore)
        self.enterRule(localctx, 14, self.RULE_exprContent)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 119
            localctx._implication = self.implication(localctx.enableIgnore)
            localctx.ex = localctx._implication.i
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ImplicationContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1, enableIgnore=None):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.enableIgnore = None
            self.i = None
            self._disjunction = None # DisjunctionContext
            self.enableIgnore = enableIgnore

        def disjunction(self):
            return self.getTypedRuleContext(SetlXgrammarParser.DisjunctionContext,0)


        def getRuleIndex(self):
            return SetlXgrammarParser.RULE_implication

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterImplication" ):
                listener.enterImplication(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitImplication" ):
                listener.exitImplication(self)




    def implication(self, enableIgnore):

        localctx = SetlXgrammarParser.ImplicationContext(self, self._ctx, self.state, enableIgnore)
        self.enterRule(localctx, 16, self.RULE_implication)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 122
            localctx._disjunction = self.disjunction(localctx.enableIgnore)
            localctx.i = localctx._disjunction.d
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class DisjunctionContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1, enableIgnore=None):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.enableIgnore = None
            self.d = None
            self._conjunction = None # ConjunctionContext
            self.enableIgnore = enableIgnore

        def conjunction(self):
            return self.getTypedRuleContext(SetlXgrammarParser.ConjunctionContext,0)


        def getRuleIndex(self):
            return SetlXgrammarParser.RULE_disjunction

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDisjunction" ):
                listener.enterDisjunction(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDisjunction" ):
                listener.exitDisjunction(self)




    def disjunction(self, enableIgnore):

        localctx = SetlXgrammarParser.DisjunctionContext(self, self._ctx, self.state, enableIgnore)
        self.enterRule(localctx, 18, self.RULE_disjunction)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 125
            localctx._conjunction = self.conjunction(localctx.enableIgnore)
            localctx.d = localctx._conjunction.c
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ConjunctionContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1, enableIgnore=None):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.enableIgnore = None
            self.c = None
            self._comparison = None # ComparisonContext
            self.enableIgnore = enableIgnore

        def comparison(self):
            return self.getTypedRuleContext(SetlXgrammarParser.ComparisonContext,0)


        def getRuleIndex(self):
            return SetlXgrammarParser.RULE_conjunction

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterConjunction" ):
                listener.enterConjunction(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitConjunction" ):
                listener.exitConjunction(self)




    def conjunction(self, enableIgnore):

        localctx = SetlXgrammarParser.ConjunctionContext(self, self._ctx, self.state, enableIgnore)
        self.enterRule(localctx, 20, self.RULE_conjunction)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 128
            localctx._comparison = self.comparison(localctx.enableIgnore)
            localctx.c = localctx._comparison.c
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ComparisonContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1, enableIgnore=None):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.enableIgnore = None
            self.c = None
            self.s1 = None # SetlxSumContext
            self.s2 = None # SetlxSumContext
            self.enableIgnore = enableIgnore

        def setlxSum(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SetlXgrammarParser.SetlxSumContext)
            else:
                return self.getTypedRuleContext(SetlXgrammarParser.SetlxSumContext,i)


        def getRuleIndex(self):
            return SetlXgrammarParser.RULE_comparison

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterComparison" ):
                listener.enterComparison(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitComparison" ):
                listener.exitComparison(self)




    def comparison(self, enableIgnore):

        localctx = SetlXgrammarParser.ComparisonContext(self, self._ctx, self.state, enableIgnore)
        self.enterRule(localctx, 22, self.RULE_comparison)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 131
            localctx.s1 = self.setlxSum(localctx.enableIgnore)
            localctx.c = localctx.s1.s 
            self.state = 165
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [SetlXgrammarParser.T__7]:
                self.state = 133
                self.match(SetlXgrammarParser.T__7)
                self.state = 134
                localctx.s2 = self.setlxSum(localctx.enableIgnore)
                localctx.c = Equal(localctx.s1.s,localctx.s2.s) 
                pass
            elif token in [SetlXgrammarParser.T__8]:
                self.state = 137
                self.match(SetlXgrammarParser.T__8)
                self.state = 138
                localctx.s2 = self.setlxSum(localctx.enableIgnore)
                localctx.c = NotEqual(localctx.s1.s,localctx.s2.s) 
                pass
            elif token in [SetlXgrammarParser.T__9]:
                self.state = 141
                self.match(SetlXgrammarParser.T__9)
                self.state = 142
                localctx.s2 = self.setlxSum(localctx.enableIgnore)
                localctx.c = LessThan(localctx.s1.s,localctx.s2.s) 
                pass
            elif token in [SetlXgrammarParser.T__10]:
                self.state = 145
                self.match(SetlXgrammarParser.T__10)
                self.state = 146
                localctx.s2 = self.setlxSum(localctx.enableIgnore)
                localctx.c = LessOrEqual(localctx.s1.s,localctx.s2.s) 
                pass
            elif token in [SetlXgrammarParser.T__11]:
                self.state = 149
                self.match(SetlXgrammarParser.T__11)
                self.state = 150
                localctx.s2 = self.setlxSum(localctx.enableIgnore)
                localctx.c = GreaterThan(localctx.s1.s,localctx.s2.s) 
                pass
            elif token in [SetlXgrammarParser.T__12]:
                self.state = 153
                self.match(SetlXgrammarParser.T__12)
                self.state = 154
                localctx.s2 = self.setlxSum(localctx.enableIgnore)
                localctx.c = GreaterOrEqual(localctx.s1.s,localctx.s2.s) 
                pass
            elif token in [SetlXgrammarParser.T__13]:
                self.state = 157
                self.match(SetlXgrammarParser.T__13)
                self.state = 158
                localctx.s2 = self.setlxSum(localctx.enableIgnore)
                localctx.c = In(localctx.s1.s,localctx.s2.s) 
                pass
            elif token in [SetlXgrammarParser.T__14]:
                self.state = 161
                self.match(SetlXgrammarParser.T__14)
                self.state = 162
                localctx.s2 = self.setlxSum(localctx.enableIgnore)
                localctx.c = NotIn(localctx.s1.s,localctx.s2.s) 
                pass
            elif token in [SetlXgrammarParser.T__0, SetlXgrammarParser.T__4, SetlXgrammarParser.T__6, SetlXgrammarParser.T__18]:
                pass
            else:
                pass
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class SetlxSumContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1, enableIgnore=None):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.enableIgnore = None
            self.s = None
            self.p1 = None # ProductContext
            self.p2 = None # ProductContext
            self.enableIgnore = enableIgnore

        def product(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SetlXgrammarParser.ProductContext)
            else:
                return self.getTypedRuleContext(SetlXgrammarParser.ProductContext,i)


        def getRuleIndex(self):
            return SetlXgrammarParser.RULE_setlxSum

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSetlxSum" ):
                listener.enterSetlxSum(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSetlxSum" ):
                listener.exitSetlxSum(self)




    def setlxSum(self, enableIgnore):

        localctx = SetlXgrammarParser.SetlxSumContext(self, self._ctx, self.state, enableIgnore)
        self.enterRule(localctx, 24, self.RULE_setlxSum)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 167
            localctx.p1 = self.product(localctx.enableIgnore)
            localctx.s = localctx.p1.p
            self.state = 179
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==SetlXgrammarParser.T__15 or _la==SetlXgrammarParser.T__16:
                self.state = 177
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [SetlXgrammarParser.T__15]:
                    self.state = 169
                    self.match(SetlXgrammarParser.T__15)
                    self.state = 170
                    localctx.p2 = self.product(localctx.enableIgnore)
                    localctx.s = Sum(localctx.p1.p,localctx.p2.p) 
                    pass
                elif token in [SetlXgrammarParser.T__16]:
                    self.state = 173
                    self.match(SetlXgrammarParser.T__16)
                    self.state = 174
                    localctx.p2 = self.product(localctx.enableIgnore)
                    localctx.s = Difference(localctx.p1.p,localctx.p2.p) 
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 181
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ProductContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1, enableIgnore=None):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.enableIgnore = None
            self.p = None
            self.r1 = None # SetlxReduceContext
            self.enableIgnore = enableIgnore

        def setlxReduce(self):
            return self.getTypedRuleContext(SetlXgrammarParser.SetlxReduceContext,0)


        def getRuleIndex(self):
            return SetlXgrammarParser.RULE_product

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProduct" ):
                listener.enterProduct(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProduct" ):
                listener.exitProduct(self)




    def product(self, enableIgnore):

        localctx = SetlXgrammarParser.ProductContext(self, self._ctx, self.state, enableIgnore)
        self.enterRule(localctx, 26, self.RULE_product)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 182
            localctx.r1 = self.setlxReduce(localctx.enableIgnore)
            localctx.p = localctx.r1.r
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class SetlxReduceContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1, enableIgnore=None):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.enableIgnore = None
            self.r = None
            self.p1 = None # PrefixOperationContext
            self.enableIgnore = enableIgnore

        def prefixOperation(self):
            return self.getTypedRuleContext(SetlXgrammarParser.PrefixOperationContext,0)


        def getRuleIndex(self):
            return SetlXgrammarParser.RULE_setlxReduce

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSetlxReduce" ):
                listener.enterSetlxReduce(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSetlxReduce" ):
                listener.exitSetlxReduce(self)




    def setlxReduce(self, enableIgnore):

        localctx = SetlXgrammarParser.SetlxReduceContext(self, self._ctx, self.state, enableIgnore)
        self.enterRule(localctx, 28, self.RULE_setlxReduce)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 185
            localctx.p1 = self.prefixOperation(localctx.enableIgnore)
            localctx.r =localctx.p1.p
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class PrefixOperationContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1, enableIgnore=None):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.enableIgnore = None
            self.p = None
            self._factor = None # FactorContext
            self.enableIgnore = enableIgnore

        def factor(self):
            return self.getTypedRuleContext(SetlXgrammarParser.FactorContext,0)


        def getRuleIndex(self):
            return SetlXgrammarParser.RULE_prefixOperation

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPrefixOperation" ):
                listener.enterPrefixOperation(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPrefixOperation" ):
                listener.exitPrefixOperation(self)




    def prefixOperation(self, enableIgnore):

        localctx = SetlXgrammarParser.PrefixOperationContext(self, self._ctx, self.state, enableIgnore)
        self.enterRule(localctx, 30, self.RULE_prefixOperation)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 188
            localctx._factor = self.factor(localctx.enableIgnore)
            localctx.p = localctx._factor.f
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class FactorContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1, enableIgnore=None):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.enableIgnore = None
            self.f = None
            self._exprContent = None # ExprContentContext
            self._variable = None # VariableContext
            self._call = None # CallContext
            self._value = None # ValueContext
            self.enableIgnore = enableIgnore

        def exprContent(self):
            return self.getTypedRuleContext(SetlXgrammarParser.ExprContentContext,0)


        def variable(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SetlXgrammarParser.VariableContext)
            else:
                return self.getTypedRuleContext(SetlXgrammarParser.VariableContext,i)


        def call(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SetlXgrammarParser.CallContext)
            else:
                return self.getTypedRuleContext(SetlXgrammarParser.CallContext,i)


        def value(self):
            return self.getTypedRuleContext(SetlXgrammarParser.ValueContext,0)


        def getRuleIndex(self):
            return SetlXgrammarParser.RULE_factor

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFactor" ):
                listener.enterFactor(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFactor" ):
                listener.exitFactor(self)




    def factor(self, enableIgnore):

        localctx = SetlXgrammarParser.FactorContext(self, self._ctx, self.state, enableIgnore)
        self.enterRule(localctx, 32, self.RULE_factor)
        self._la = 0 # Token type
        try:
            self.state = 223
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,15,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 199
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [SetlXgrammarParser.T__17]:
                    self.state = 191
                    self.match(SetlXgrammarParser.T__17)
                    self.state = 192
                    localctx._exprContent = self.exprContent(localctx.enableIgnore)
                    self.state = 193
                    self.match(SetlXgrammarParser.T__18)
                    localctx.f = localctx._exprContent.ex 
                    pass
                elif token in [SetlXgrammarParser.ID]:
                    self.state = 196
                    localctx._variable = self.variable()
                    localctx.f = localctx._variable.v 
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 210
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==SetlXgrammarParser.T__2 or _la==SetlXgrammarParser.T__17:
                    self.state = 208
                    self._errHandler.sync(self)
                    token = self._input.LA(1)
                    if token in [SetlXgrammarParser.T__2]:
                        self.state = 201
                        self.match(SetlXgrammarParser.T__2)
                        self.state = 202
                        localctx._variable = self.variable()
                        localctx.f = MemberAccess(localctx.f,localctx._variable.v) 
                        pass
                    elif token in [SetlXgrammarParser.T__17]:
                        self.state = 205
                        localctx._call = self.call(localctx.enableIgnore)
                        localctx.f = localctx._call.c 
                        pass
                    else:
                        raise NoViableAltException(self)

                    self.state = 212
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 215
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==SetlXgrammarParser.T__19:
                    self.state = 213
                    self.match(SetlXgrammarParser.T__19)
                    localctx.f = Factorial(localctx.f) 


                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 217
                localctx._value = self.value(localctx.enableIgnore)
                localctx.f = localctx._value.v 
                self.state = 221
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==SetlXgrammarParser.T__19:
                    self.state = 219
                    self.match(SetlXgrammarParser.T__19)
                    localctx.f = Factorial(localctx._value.v) 


                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class CallContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1, enableIgnore=None):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.enableIgnore = None
            self.c = None
            self._callParameters = None # CallParametersContext
            self.enableIgnore = enableIgnore

        def callParameters(self):
            return self.getTypedRuleContext(SetlXgrammarParser.CallParametersContext,0)


        def getRuleIndex(self):
            return SetlXgrammarParser.RULE_call

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCall" ):
                listener.enterCall(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCall" ):
                listener.exitCall(self)




    def call(self, enableIgnore):

        localctx = SetlXgrammarParser.CallContext(self, self._ctx, self.state, enableIgnore)
        self.enterRule(localctx, 34, self.RULE_call)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 225
            self.match(SetlXgrammarParser.T__17)
            self.state = 226
            localctx._callParameters = self.callParameters(localctx.enableIgnore)
            self.state = 227
            self.match(SetlXgrammarParser.T__18)
            localctx.c = Call(localctx._callParameters.params, localctx._callParameters.ex) 
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class CallParametersContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1, enableIgnore=None):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.enableIgnore = None
            self.params = None
            self.ex = None
            self._exprList = None # ExprListContext
            self.enableIgnore = enableIgnore

        def exprList(self):
            return self.getTypedRuleContext(SetlXgrammarParser.ExprListContext,0)


        def getRuleIndex(self):
            return SetlXgrammarParser.RULE_callParameters

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCallParameters" ):
                listener.enterCallParameters(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCallParameters" ):
                listener.exitCallParameters(self)




    def callParameters(self, enableIgnore):

        localctx = SetlXgrammarParser.CallParametersContext(self, self._ctx, self.state, enableIgnore)
        self.enterRule(localctx, 36, self.RULE_callParameters)

        localctx.params                                       = []
        localctx.ex                                           = None
            
        try:
            self.state = 234
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,16,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 230
                localctx._exprList = self.exprList(localctx.enableIgnore)
                localctx.params = localctx._exprList.exprs
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)

                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ValueContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1, enableIgnore=None):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.enableIgnore = None
            self.v = None
            self._STRING = None # Token
            self._LITERAL = None # Token
            self._atomicValue = None # AtomicValueContext
            self.enableIgnore = enableIgnore

        def STRING(self):
            return self.getToken(SetlXgrammarParser.STRING, 0)

        def LITERAL(self):
            return self.getToken(SetlXgrammarParser.LITERAL, 0)

        def atomicValue(self):
            return self.getTypedRuleContext(SetlXgrammarParser.AtomicValueContext,0)


        def getRuleIndex(self):
            return SetlXgrammarParser.RULE_value

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterValue" ):
                listener.enterValue(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitValue" ):
                listener.exitValue(self)




    def value(self, enableIgnore):

        localctx = SetlXgrammarParser.ValueContext(self, self._ctx, self.state, enableIgnore)
        self.enterRule(localctx, 38, self.RULE_value)
        try:
            self.state = 246
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,17,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 236
                localctx._STRING = self.match(SetlXgrammarParser.STRING)
                localctx.v = SetlXString((None if localctx._STRING is None else localctx._STRING.text)) 
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 238
                localctx._LITERAL = self.match(SetlXgrammarParser.LITERAL)
                localctx.v = SetlXLiteral((None if localctx._LITERAL is None else localctx._LITERAL.text)) 
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 240
                localctx._atomicValue = self.atomicValue()
                localctx.v = localctx._atomicValue.av 
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 243
                if not localctx.enableIgnore:
                    from antlr4.error.Errors import FailedPredicateException
                    raise FailedPredicateException(self, "$enableIgnore")
                self.state = 244
                self.match(SetlXgrammarParser.T__5)
                localctx.v = VariableIgnore() 
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class AtomicValueContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.av = None
            self._NUMBER = None # Token
            self._DOUBLE = None # Token

        def NUMBER(self):
            return self.getToken(SetlXgrammarParser.NUMBER, 0)

        def DOUBLE(self):
            return self.getToken(SetlXgrammarParser.DOUBLE, 0)

        def getRuleIndex(self):
            return SetlXgrammarParser.RULE_atomicValue

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAtomicValue" ):
                listener.enterAtomicValue(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAtomicValue" ):
                listener.exitAtomicValue(self)




    def atomicValue(self):

        localctx = SetlXgrammarParser.AtomicValueContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_atomicValue)
        try:
            self.state = 258
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [SetlXgrammarParser.NUMBER]:
                self.enterOuterAlt(localctx, 1)
                self.state = 248
                localctx._NUMBER = self.match(SetlXgrammarParser.NUMBER)
                localctx.av = SetlXFraction((None if localctx._NUMBER is None else localctx._NUMBER.text)) 
                pass
            elif token in [SetlXgrammarParser.DOUBLE]:
                self.enterOuterAlt(localctx, 2)
                self.state = 250
                localctx._DOUBLE = self.match(SetlXgrammarParser.DOUBLE)
                localctx.av = float((None if localctx._DOUBLE is None else localctx._DOUBLE.text)) 
                pass
            elif token in [SetlXgrammarParser.T__20]:
                self.enterOuterAlt(localctx, 3)
                self.state = 252
                self.match(SetlXgrammarParser.T__20)
                localctx.av = SetlXOm() 
                pass
            elif token in [SetlXgrammarParser.T__21]:
                self.enterOuterAlt(localctx, 4)
                self.state = 254
                self.match(SetlXgrammarParser.T__21)
                localctx.av = TRUE 
                pass
            elif token in [SetlXgrammarParser.T__22]:
                self.enterOuterAlt(localctx, 5)
                self.state = 256
                self.match(SetlXgrammarParser.T__22)
                localctx.av = FALSE 
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class VariableContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.v = None
            self._ID = None # Token

        def ID(self):
            return self.getToken(SetlXgrammarParser.ID, 0)

        def getRuleIndex(self):
            return SetlXgrammarParser.RULE_variable

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVariable" ):
                listener.enterVariable(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVariable" ):
                listener.exitVariable(self)




    def variable(self):

        localctx = SetlXgrammarParser.VariableContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_variable)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 260
            localctx._ID = self.match(SetlXgrammarParser.ID)
            localctx.v = Variable((None if localctx._ID is None else localctx._ID.text)) 
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class AssignmentListContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.al = None
            self.a1 = None # AssignableContext
            self.a2 = None # AssignableContext

        def assignable(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SetlXgrammarParser.AssignableContext)
            else:
                return self.getTypedRuleContext(SetlXgrammarParser.AssignableContext,i)


        def getRuleIndex(self):
            return SetlXgrammarParser.RULE_assignmentList

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAssignmentList" ):
                listener.enterAssignmentList(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAssignmentList" ):
                listener.exitAssignmentList(self)




    def assignmentList(self):

        localctx = SetlXgrammarParser.AssignmentListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_assignmentList)

        localctx.al = []
          
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 263
            localctx.a1 = self.assignable(True)
            localctx.al.append(localctx.a1.a) 
            self.state = 271
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==SetlXgrammarParser.T__6:
                self.state = 265
                self.match(SetlXgrammarParser.T__6)
                self.state = 266
                localctx.a2 = self.assignable(True)
                localctx.al.append(localctx.a2.a) 
                self.state = 273
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[3] = self.assignable_sempred
        self._predicates[19] = self.value_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def assignable_sempred(self, localctx:AssignableContext, predIndex:int):
            if predIndex == 0:
                return localctx.enableIgnore
         

    def value_sempred(self, localctx:ValueContext, predIndex:int):
            if predIndex == 1:
                return localctx.enableIgnore
         




