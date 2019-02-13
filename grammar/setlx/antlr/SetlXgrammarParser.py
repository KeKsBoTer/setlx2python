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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3R")
        buf.write("\u032a\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31")
        buf.write("\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36")
        buf.write("\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\3\2\3\2\3\2")
        buf.write("\7\2L\n\2\f\2\16\2O\13\2\3\2\3\2\3\3\3\3\3\3\3\3\3\3\3")
        buf.write("\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\7\3d\n")
        buf.write("\3\f\3\16\3g\13\3\3\3\3\3\3\3\3\3\3\3\3\3\5\3o\n\3\3\3")
        buf.write("\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\7\3{\n\3\f\3\16\3")
        buf.write("~\13\3\3\3\3\3\3\3\5\3\u0083\n\3\3\3\3\3\3\3\3\3\3\3\3")
        buf.write("\3\3\3\3\3\3\3\5\3\u008e\n\3\3\3\3\3\3\3\3\3\3\3\3\3\3")
        buf.write("\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3")
        buf.write("\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3")
        buf.write("\3\3\3\3\3\3\3\3\3\3\3\5\3\u00b7\n\3\3\3\3\3\3\3\3\3\3")
        buf.write("\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3")
        buf.write("\5\3\u00cb\n\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3")
        buf.write("\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\5")
        buf.write("\3\u00e4\n\3\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3")
        buf.write("\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4")
        buf.write("\3\4\5\4\u00ff\n\4\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5")
        buf.write("\3\5\3\5\3\5\3\5\5\5\u010e\n\5\5\5\u0110\n\5\3\6\3\6\3")
        buf.write("\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\7\6\u011d\n\6\f\6\16")
        buf.write("\6\u0120\13\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\5\6\u012a")
        buf.write("\n\6\3\7\3\7\3\7\3\b\3\b\3\b\3\t\3\t\3\t\3\t\3\t\3\t\7")
        buf.write("\t\u0138\n\t\f\t\16\t\u013b\13\t\3\n\3\n\3\n\3\n\3\n\3")
        buf.write("\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n\5\n\u014a\n\n\5\n\u014c")
        buf.write("\n\n\3\13\3\13\3\13\3\13\3\13\3\f\3\f\3\f\3\f\3\f\3\f")
        buf.write("\3\f\3\f\3\f\3\f\7\f\u015d\n\f\f\f\16\f\u0160\13\f\5\f")
        buf.write("\u0162\n\f\3\f\5\f\u0165\n\f\3\r\3\r\3\r\3\r\3\r\3\r\5")
        buf.write("\r\u016d\n\r\3\16\3\16\3\16\3\16\3\16\3\16\7\16\u0175")
        buf.write("\n\16\f\16\16\16\u0178\13\16\3\17\3\17\3\17\3\17\3\17")
        buf.write("\3\17\7\17\u0180\n\17\f\17\16\17\u0183\13\17\3\20\3\20")
        buf.write("\3\20\3\20\3\20\3\20\3\20\3\20\3\20\3\20\3\20\3\20\3\20")
        buf.write("\3\20\3\20\3\20\3\20\3\20\3\20\3\20\3\20\3\20\3\20\3\20")
        buf.write("\3\20\3\20\3\20\3\20\3\20\3\20\3\20\3\20\3\20\3\20\5\20")
        buf.write("\u01a7\n\20\3\21\3\21\3\21\3\21\3\21\3\21\3\21\3\21\3")
        buf.write("\21\3\21\7\21\u01b3\n\21\f\21\16\21\u01b6\13\21\3\22\3")
        buf.write("\22\3\22\3\22\3\22\3\22\3\22\3\22\3\22\3\22\3\22\3\22")
        buf.write("\3\22\3\22\3\22\3\22\3\22\3\22\3\22\3\22\3\22\3\22\7\22")
        buf.write("\u01ce\n\22\f\22\16\22\u01d1\13\22\3\23\3\23\3\23\3\23")
        buf.write("\3\23\3\23\3\23\3\23\3\23\3\23\7\23\u01dd\n\23\f\23\16")
        buf.write("\23\u01e0\13\23\3\24\3\24\3\24\3\24\3\24\3\24\5\24\u01e8")
        buf.write("\n\24\3\24\3\24\3\24\3\24\3\24\3\24\3\24\3\24\3\24\3\24")
        buf.write("\3\24\3\24\3\24\3\24\3\24\3\24\5\24\u01fa\n\24\3\25\3")
        buf.write("\25\3\25\3\25\3\25\3\25\3\25\3\25\3\25\3\25\3\25\3\25")
        buf.write("\3\25\3\25\3\25\3\25\3\25\3\25\3\25\3\25\3\25\3\25\3\25")
        buf.write("\3\25\3\25\3\25\3\25\3\25\3\25\3\25\3\25\5\25\u021b\n")
        buf.write("\25\3\25\3\25\3\25\3\25\3\25\3\25\3\25\7\25\u0224\n\25")
        buf.write("\f\25\16\25\u0227\13\25\3\25\3\25\5\25\u022b\n\25\3\25")
        buf.write("\3\25\3\25\3\25\5\25\u0231\n\25\5\25\u0233\n\25\3\26\3")
        buf.write("\26\3\26\3\26\3\26\3\26\3\26\3\26\3\26\3\26\3\26\3\26")
        buf.write("\3\26\3\26\3\26\3\26\3\26\3\26\3\26\3\26\3\26\3\26\3\26")
        buf.write("\3\26\3\26\3\26\3\26\5\26\u0250\n\26\3\27\3\27\3\27\3")
        buf.write("\27\3\27\3\27\7\27\u0258\n\27\f\27\16\27\u025b\13\27\3")
        buf.write("\27\3\27\3\27\3\27\7\27\u0261\n\27\f\27\16\27\u0264\13")
        buf.write("\27\3\27\3\27\3\27\3\27\3\27\3\27\7\27\u026c\n\27\f\27")
        buf.write("\16\27\u026f\13\27\3\27\5\27\u0272\n\27\3\30\3\30\3\30")
        buf.write("\3\30\3\30\3\30\3\30\3\30\5\30\u027c\n\30\3\31\3\31\3")
        buf.write("\31\3\31\3\31\3\32\3\32\3\32\3\32\3\32\3\32\3\32\3\32")
        buf.write("\3\32\3\32\5\32\u028d\n\32\3\33\3\33\3\33\3\33\3\33\3")
        buf.write("\33\5\33\u0295\n\33\3\33\3\33\3\33\3\33\6\33\u029b\n\33")
        buf.write("\r\33\16\33\u029c\3\33\3\33\3\33\5\33\u02a2\n\33\3\33")
        buf.write("\3\33\3\33\3\33\5\33\u02a8\n\33\3\34\3\34\3\34\3\34\5")
        buf.write("\34\u02ae\n\34\3\35\3\35\3\35\3\35\5\35\u02b4\n\35\3\35")
        buf.write("\3\35\3\35\3\35\3\35\3\35\5\35\u02bc\n\35\3\35\3\35\3")
        buf.write("\35\3\35\3\35\3\35\3\35\3\35\3\35\3\35\3\35\3\35\5\35")
        buf.write("\u02ca\n\35\3\36\3\36\3\36\3\36\3\36\3\36\3\36\3\36\3")
        buf.write("\36\3\36\3\36\3\36\7\36\u02d8\n\36\f\36\16\36\u02db\13")
        buf.write("\36\3\36\3\36\3\36\3\36\3\36\5\36\u02e2\n\36\5\36\u02e4")
        buf.write("\n\36\3\36\3\36\3\36\3\36\3\36\3\36\3\36\3\36\3\36\3\36")
        buf.write("\5\36\u02f0\n\36\3\36\3\36\3\36\3\36\3\36\3\36\3\36\5")
        buf.write("\36\u02f9\n\36\5\36\u02fb\n\36\3\37\3\37\3\37\3\37\3\37")
        buf.write("\3\37\7\37\u0303\n\37\f\37\16\37\u0306\13\37\3 \3 \3 ")
        buf.write("\3 \3 \3!\3!\3!\3!\3!\3!\3!\3!\3!\3!\5!\u0317\n!\3\"\3")
        buf.write("\"\3\"\3#\3#\3#\3$\3$\3$\3$\3$\3$\7$\u0325\n$\f$\16$\u0328")
        buf.write("\13$\3$\2\2%\2\4\6\b\n\f\16\20\22\24\26\30\32\34\36 \"")
        buf.write("$&(*,.\60\62\64\668:<>@BDF\2\2\2\u0375\2M\3\2\2\2\4\u00e3")
        buf.write("\3\2\2\2\6\u00e5\3\2\2\2\b\u010f\3\2\2\2\n\u0129\3\2\2")
        buf.write("\2\f\u012b\3\2\2\2\16\u012e\3\2\2\2\20\u0131\3\2\2\2\22")
        buf.write("\u014b\3\2\2\2\24\u014d\3\2\2\2\26\u0164\3\2\2\2\30\u0166")
        buf.write("\3\2\2\2\32\u016e\3\2\2\2\34\u0179\3\2\2\2\36\u0184\3")
        buf.write("\2\2\2 \u01a8\3\2\2\2\"\u01b7\3\2\2\2$\u01d2\3\2\2\2&")
        buf.write("\u01f9\3\2\2\2(\u0232\3\2\2\2*\u024f\3\2\2\2,\u0271\3")
        buf.write("\2\2\2.\u027b\3\2\2\2\60\u027d\3\2\2\2\62\u028c\3\2\2")
        buf.write("\2\64\u02a7\3\2\2\2\66\u02ad\3\2\2\28\u02c9\3\2\2\2:\u02cb")
        buf.write("\3\2\2\2<\u02fc\3\2\2\2>\u0307\3\2\2\2@\u0316\3\2\2\2")
        buf.write("B\u0318\3\2\2\2D\u031b\3\2\2\2F\u031e\3\2\2\2HI\5\4\3")
        buf.write("\2IJ\b\2\1\2JL\3\2\2\2KH\3\2\2\2LO\3\2\2\2MK\3\2\2\2M")
        buf.write("N\3\2\2\2NP\3\2\2\2OM\3\2\2\2PQ\b\2\1\2Q\3\3\2\2\2RS\7")
        buf.write("\3\2\2ST\7\4\2\2TU\5D#\2UV\7\5\2\2VW\7\6\2\2WX\5\2\2\2")
        buf.write("Xe\7\7\2\2YZ\7\b\2\2Z[\7\3\2\2[\\\7\4\2\2\\]\5D#\2]^\7")
        buf.write("\5\2\2^_\7\6\2\2_`\5\2\2\2`a\7\7\2\2ab\b\3\1\2bd\3\2\2")
        buf.write("\2cY\3\2\2\2dg\3\2\2\2ec\3\2\2\2ef\3\2\2\2fn\3\2\2\2g")
        buf.write("e\3\2\2\2hi\7\b\2\2ij\7\6\2\2jk\5\2\2\2kl\7\7\2\2lm\b")
        buf.write("\3\1\2mo\3\2\2\2nh\3\2\2\2no\3\2\2\2op\3\2\2\2pq\b\3\1")
        buf.write("\2q\u00e4\3\2\2\2rs\7\t\2\2s|\7\6\2\2tu\7\n\2\2uv\5D#")
        buf.write("\2vw\7\13\2\2wx\5\2\2\2xy\b\3\1\2y{\3\2\2\2zt\3\2\2\2")
        buf.write("{~\3\2\2\2|z\3\2\2\2|}\3\2\2\2}\u0082\3\2\2\2~|\3\2\2")
        buf.write("\2\177\u0080\7\f\2\2\u0080\u0081\7\13\2\2\u0081\u0083")
        buf.write("\5\2\2\2\u0082\177\3\2\2\2\u0082\u0083\3\2\2\2\u0083\u0084")
        buf.write("\3\2\2\2\u0084\u0085\7\7\2\2\u0085\u00e4\b\3\1\2\u0086")
        buf.write("\u0087\7\r\2\2\u0087\u0088\7\4\2\2\u0088\u008d\5<\37\2")
        buf.write("\u0089\u008a\7\16\2\2\u008a\u008b\5D#\2\u008b\u008c\b")
        buf.write("\3\1\2\u008c\u008e\3\2\2\2\u008d\u0089\3\2\2\2\u008d\u008e")
        buf.write("\3\2\2\2\u008e\u008f\3\2\2\2\u008f\u0090\7\5\2\2\u0090")
        buf.write("\u0091\7\6\2\2\u0091\u0092\5\2\2\2\u0092\u0093\7\7\2\2")
        buf.write("\u0093\u0094\b\3\1\2\u0094\u00e4\3\2\2\2\u0095\u0096\7")
        buf.write("\17\2\2\u0096\u0097\7\4\2\2\u0097\u0098\5D#\2\u0098\u0099")
        buf.write("\7\5\2\2\u0099\u009a\7\6\2\2\u009a\u009b\5\2\2\2\u009b")
        buf.write("\u009c\7\7\2\2\u009c\u009d\b\3\1\2\u009d\u00e4\3\2\2\2")
        buf.write("\u009e\u009f\7\20\2\2\u009f\u00a0\7\6\2\2\u00a0\u00a1")
        buf.write("\5\2\2\2\u00a1\u00a2\7\7\2\2\u00a2\u00a3\7\17\2\2\u00a3")
        buf.write("\u00a4\7\4\2\2\u00a4\u00a5\5D#\2\u00a5\u00a6\7\5\2\2\u00a6")
        buf.write("\u00a7\7\21\2\2\u00a7\u00a8\b\3\1\2\u00a8\u00e4\3\2\2")
        buf.write("\2\u00a9\u00aa\7\22\2\2\u00aa\u00ab\7\6\2\2\u00ab\u00ac")
        buf.write("\5\2\2\2\u00ac\u00b6\7\7\2\2\u00ad\u00ae\7\23\2\2\u00ae")
        buf.write("\u00af\7\4\2\2\u00af\u00b0\5\f\7\2\u00b0\u00b1\7\5\2\2")
        buf.write("\u00b1\u00b2\7\6\2\2\u00b2\u00b3\5\2\2\2\u00b3\u00b4\7")
        buf.write("\7\2\2\u00b4\u00b5\b\3\1\2\u00b5\u00b7\3\2\2\2\u00b6\u00ad")
        buf.write("\3\2\2\2\u00b6\u00b7\3\2\2\2\u00b7\u00b8\3\2\2\2\u00b8")
        buf.write("\u00b9\b\3\1\2\u00b9\u00e4\3\2\2\2\u00ba\u00bb\7\24\2")
        buf.write("\2\u00bb\u00bc\7\21\2\2\u00bc\u00e4\b\3\1\2\u00bd\u00be")
        buf.write("\7\25\2\2\u00be\u00bf\7\21\2\2\u00bf\u00e4\b\3\1\2\u00c0")
        buf.write("\u00c1\7\26\2\2\u00c1\u00c2\7\21\2\2\u00c2\u00e4\b\3\1")
        buf.write("\2\u00c3\u00c4\7\27\2\2\u00c4\u00c5\7\21\2\2\u00c5\u00e4")
        buf.write("\b\3\1\2\u00c6\u00ca\7\30\2\2\u00c7\u00c8\5\16\b\2\u00c8")
        buf.write("\u00c9\b\3\1\2\u00c9\u00cb\3\2\2\2\u00ca\u00c7\3\2\2\2")
        buf.write("\u00ca\u00cb\3\2\2\2\u00cb\u00cc\3\2\2\2\u00cc\u00cd\7")
        buf.write("\21\2\2\u00cd\u00e4\b\3\1\2\u00ce\u00cf\7\31\2\2\u00cf")
        buf.write("\u00d0\7\4\2\2\u00d0\u00d1\5D#\2\u00d1\u00d2\7\32\2\2")
        buf.write("\u00d2\u00d3\5\16\b\2\u00d3\u00d4\7\5\2\2\u00d4\u00d5")
        buf.write("\7\21\2\2\u00d5\u00d6\b\3\1\2\u00d6\u00e4\3\2\2\2\u00d7")
        buf.write("\u00d8\5\6\4\2\u00d8\u00d9\7\21\2\2\u00d9\u00da\b\3\1")
        buf.write("\2\u00da\u00e4\3\2\2\2\u00db\u00dc\5\b\5\2\u00dc\u00dd")
        buf.write("\7\21\2\2\u00dd\u00de\b\3\1\2\u00de\u00e4\3\2\2\2\u00df")
        buf.write("\u00e0\5\16\b\2\u00e0\u00e1\7\21\2\2\u00e1\u00e2\b\3\1")
        buf.write("\2\u00e2\u00e4\3\2\2\2\u00e3R\3\2\2\2\u00e3r\3\2\2\2\u00e3")
        buf.write("\u0086\3\2\2\2\u00e3\u0095\3\2\2\2\u00e3\u009e\3\2\2\2")
        buf.write("\u00e3\u00a9\3\2\2\2\u00e3\u00ba\3\2\2\2\u00e3\u00bd\3")
        buf.write("\2\2\2\u00e3\u00c0\3\2\2\2\u00e3\u00c3\3\2\2\2\u00e3\u00c6")
        buf.write("\3\2\2\2\u00e3\u00ce\3\2\2\2\u00e3\u00d7\3\2\2\2\u00e3")
        buf.write("\u00db\3\2\2\2\u00e3\u00df\3\2\2\2\u00e4\5\3\2\2\2\u00e5")
        buf.write("\u00fe\5\n\6\2\u00e6\u00e7\7\33\2\2\u00e7\u00e8\5\16\b")
        buf.write("\2\u00e8\u00e9\b\4\1\2\u00e9\u00ff\3\2\2\2\u00ea\u00eb")
        buf.write("\7\34\2\2\u00eb\u00ec\5\16\b\2\u00ec\u00ed\b\4\1\2\u00ed")
        buf.write("\u00ff\3\2\2\2\u00ee\u00ef\7\35\2\2\u00ef\u00f0\5\16\b")
        buf.write("\2\u00f0\u00f1\b\4\1\2\u00f1\u00ff\3\2\2\2\u00f2\u00f3")
        buf.write("\7\36\2\2\u00f3\u00f4\5\16\b\2\u00f4\u00f5\b\4\1\2\u00f5")
        buf.write("\u00ff\3\2\2\2\u00f6\u00f7\7\37\2\2\u00f7\u00f8\5\16\b")
        buf.write("\2\u00f8\u00f9\b\4\1\2\u00f9\u00ff\3\2\2\2\u00fa\u00fb")
        buf.write("\7 \2\2\u00fb\u00fc\5\16\b\2\u00fc\u00fd\b\4\1\2\u00fd")
        buf.write("\u00ff\3\2\2\2\u00fe\u00e6\3\2\2\2\u00fe\u00ea\3\2\2\2")
        buf.write("\u00fe\u00ee\3\2\2\2\u00fe\u00f2\3\2\2\2\u00fe\u00f6\3")
        buf.write("\2\2\2\u00fe\u00fa\3\2\2\2\u00ff\7\3\2\2\2\u0100\u0101")
        buf.write("\5B\"\2\u0101\u0102\7!\2\2\u0102\u0103\5*\26\2\u0103\u0104")
        buf.write("\b\5\1\2\u0104\u0110\3\2\2\2\u0105\u0106\5\n\6\2\u0106")
        buf.write("\u010d\7!\2\2\u0107\u0108\5\b\5\2\u0108\u0109\b\5\1\2")
        buf.write("\u0109\u010e\3\2\2\2\u010a\u010b\5\22\n\2\u010b\u010c")
        buf.write("\b\5\1\2\u010c\u010e\3\2\2\2\u010d\u0107\3\2\2\2\u010d")
        buf.write("\u010a\3\2\2\2\u010e\u0110\3\2\2\2\u010f\u0100\3\2\2\2")
        buf.write("\u010f\u0105\3\2\2\2\u0110\t\3\2\2\2\u0111\u0112\5\f\7")
        buf.write("\2\u0112\u011e\b\6\1\2\u0113\u0114\7\"\2\2\u0114\u0115")
        buf.write("\5B\"\2\u0115\u0116\b\6\1\2\u0116\u011d\3\2\2\2\u0117")
        buf.write("\u0118\7#\2\2\u0118\u0119\5\20\t\2\u0119\u011a\7$\2\2")
        buf.write("\u011a\u011b\b\6\1\2\u011b\u011d\3\2\2\2\u011c\u0113\3")
        buf.write("\2\2\2\u011c\u0117\3\2\2\2\u011d\u0120\3\2\2\2\u011e\u011c")
        buf.write("\3\2\2\2\u011e\u011f\3\2\2\2\u011f\u012a\3\2\2\2\u0120")
        buf.write("\u011e\3\2\2\2\u0121\u0122\7#\2\2\u0122\u0123\5F$\2\u0123")
        buf.write("\u0124\7$\2\2\u0124\u0125\b\6\1\2\u0125\u012a\3\2\2\2")
        buf.write("\u0126\u0127\6\6\2\3\u0127\u0128\7%\2\2\u0128\u012a\b")
        buf.write("\6\1\2\u0129\u0111\3\2\2\2\u0129\u0121\3\2\2\2\u0129\u0126")
        buf.write("\3\2\2\2\u012a\13\3\2\2\2\u012b\u012c\7I\2\2\u012c\u012d")
        buf.write("\b\7\1\2\u012d\r\3\2\2\2\u012e\u012f\5\22\n\2\u012f\u0130")
        buf.write("\b\b\1\2\u0130\17\3\2\2\2\u0131\u0132\5\22\n\2\u0132\u0139")
        buf.write("\b\t\1\2\u0133\u0134\7\32\2\2\u0134\u0135\5\22\n\2\u0135")
        buf.write("\u0136\b\t\1\2\u0136\u0138\3\2\2\2\u0137\u0133\3\2\2\2")
        buf.write("\u0138\u013b\3\2\2\2\u0139\u0137\3\2\2\2\u0139\u013a\3")
        buf.write("\2\2\2\u013a\21\3\2\2\2\u013b\u0139\3\2\2\2\u013c\u013d")
        buf.write("\5\24\13\2\u013d\u013e\b\n\1\2\u013e\u014c\3\2\2\2\u013f")
        buf.write("\u0140\5\30\r\2\u0140\u0149\b\n\1\2\u0141\u0142\7&\2\2")
        buf.write("\u0142\u0143\5\30\r\2\u0143\u0144\b\n\1\2\u0144\u014a")
        buf.write("\3\2\2\2\u0145\u0146\7\'\2\2\u0146\u0147\5\30\r\2\u0147")
        buf.write("\u0148\b\n\1\2\u0148\u014a\3\2\2\2\u0149\u0141\3\2\2\2")
        buf.write("\u0149\u0145\3\2\2\2\u0149\u014a\3\2\2\2\u014a\u014c\3")
        buf.write("\2\2\2\u014b\u013c\3\2\2\2\u014b\u013f\3\2\2\2\u014c\23")
        buf.write("\3\2\2\2\u014d\u014e\5\26\f\2\u014e\u014f\7(\2\2\u014f")
        buf.write("\u0150\5\16\b\2\u0150\u0151\b\13\1\2\u0151\25\3\2\2\2")
        buf.write("\u0152\u0153\5B\"\2\u0153\u0154\b\f\1\2\u0154\u0165\3")
        buf.write("\2\2\2\u0155\u0161\7#\2\2\u0156\u0157\5B\"\2\u0157\u015e")
        buf.write("\b\f\1\2\u0158\u0159\7\32\2\2\u0159\u015a\5B\"\2\u015a")
        buf.write("\u015b\b\f\1\2\u015b\u015d\3\2\2\2\u015c\u0158\3\2\2\2")
        buf.write("\u015d\u0160\3\2\2\2\u015e\u015c\3\2\2\2\u015e\u015f\3")
        buf.write("\2\2\2\u015f\u0162\3\2\2\2\u0160\u015e\3\2\2\2\u0161\u0156")
        buf.write("\3\2\2\2\u0161\u0162\3\2\2\2\u0162\u0163\3\2\2\2\u0163")
        buf.write("\u0165\7$\2\2\u0164\u0152\3\2\2\2\u0164\u0155\3\2\2\2")
        buf.write("\u0165\27\3\2\2\2\u0166\u0167\5\32\16\2\u0167\u016c\b")
        buf.write("\r\1\2\u0168\u0169\7)\2\2\u0169\u016a\5\30\r\2\u016a\u016b")
        buf.write("\b\r\1\2\u016b\u016d\3\2\2\2\u016c\u0168\3\2\2\2\u016c")
        buf.write("\u016d\3\2\2\2\u016d\31\3\2\2\2\u016e\u016f\5\34\17\2")
        buf.write("\u016f\u0176\b\16\1\2\u0170\u0171\7*\2\2\u0171\u0172\5")
        buf.write("\34\17\2\u0172\u0173\b\16\1\2\u0173\u0175\3\2\2\2\u0174")
        buf.write("\u0170\3\2\2\2\u0175\u0178\3\2\2\2\u0176\u0174\3\2\2\2")
        buf.write("\u0176\u0177\3\2\2\2\u0177\33\3\2\2\2\u0178\u0176\3\2")
        buf.write("\2\2\u0179\u017a\5\36\20\2\u017a\u0181\b\17\1\2\u017b")
        buf.write("\u017c\7+\2\2\u017c\u017d\5\36\20\2\u017d\u017e\b\17\1")
        buf.write("\2\u017e\u0180\3\2\2\2\u017f\u017b\3\2\2\2\u0180\u0183")
        buf.write("\3\2\2\2\u0181\u017f\3\2\2\2\u0181\u0182\3\2\2\2\u0182")
        buf.write("\35\3\2\2\2\u0183\u0181\3\2\2\2\u0184\u0185\5 \21\2\u0185")
        buf.write("\u01a6\b\20\1\2\u0186\u0187\7,\2\2\u0187\u0188\5 \21\2")
        buf.write("\u0188\u0189\b\20\1\2\u0189\u01a7\3\2\2\2\u018a\u018b")
        buf.write("\7-\2\2\u018b\u018c\5 \21\2\u018c\u018d\b\20\1\2\u018d")
        buf.write("\u01a7\3\2\2\2\u018e\u018f\7.\2\2\u018f\u0190\5 \21\2")
        buf.write("\u0190\u0191\b\20\1\2\u0191\u01a7\3\2\2\2\u0192\u0193")
        buf.write("\7/\2\2\u0193\u0194\5 \21\2\u0194\u0195\b\20\1\2\u0195")
        buf.write("\u01a7\3\2\2\2\u0196\u0197\7\60\2\2\u0197\u0198\5 \21")
        buf.write("\2\u0198\u0199\b\20\1\2\u0199\u01a7\3\2\2\2\u019a\u019b")
        buf.write("\7\61\2\2\u019b\u019c\5 \21\2\u019c\u019d\b\20\1\2\u019d")
        buf.write("\u01a7\3\2\2\2\u019e\u019f\7\62\2\2\u019f\u01a0\5 \21")
        buf.write("\2\u01a0\u01a1\b\20\1\2\u01a1\u01a7\3\2\2\2\u01a2\u01a3")
        buf.write("\7\63\2\2\u01a3\u01a4\5 \21\2\u01a4\u01a5\b\20\1\2\u01a5")
        buf.write("\u01a7\3\2\2\2\u01a6\u0186\3\2\2\2\u01a6\u018a\3\2\2\2")
        buf.write("\u01a6\u018e\3\2\2\2\u01a6\u0192\3\2\2\2\u01a6\u0196\3")
        buf.write("\2\2\2\u01a6\u019a\3\2\2\2\u01a6\u019e\3\2\2\2\u01a6\u01a2")
        buf.write("\3\2\2\2\u01a6\u01a7\3\2\2\2\u01a7\37\3\2\2\2\u01a8\u01a9")
        buf.write("\5\"\22\2\u01a9\u01b4\b\21\1\2\u01aa\u01ab\7\64\2\2\u01ab")
        buf.write("\u01ac\5\"\22\2\u01ac\u01ad\b\21\1\2\u01ad\u01b3\3\2\2")
        buf.write("\2\u01ae\u01af\7\65\2\2\u01af\u01b0\5\"\22\2\u01b0\u01b1")
        buf.write("\b\21\1\2\u01b1\u01b3\3\2\2\2\u01b2\u01aa\3\2\2\2\u01b2")
        buf.write("\u01ae\3\2\2\2\u01b3\u01b6\3\2\2\2\u01b4\u01b2\3\2\2\2")
        buf.write("\u01b4\u01b5\3\2\2\2\u01b5!\3\2\2\2\u01b6\u01b4\3\2\2")
        buf.write("\2\u01b7\u01b8\5$\23\2\u01b8\u01cf\b\22\1\2\u01b9\u01ba")
        buf.write("\7\66\2\2\u01ba\u01bb\5$\23\2\u01bb\u01bc\b\22\1\2\u01bc")
        buf.write("\u01ce\3\2\2\2\u01bd\u01be\7\67\2\2\u01be\u01bf\5$\23")
        buf.write("\2\u01bf\u01c0\b\22\1\2\u01c0\u01ce\3\2\2\2\u01c1\u01c2")
        buf.write("\78\2\2\u01c2\u01c3\5$\23\2\u01c3\u01c4\b\22\1\2\u01c4")
        buf.write("\u01ce\3\2\2\2\u01c5\u01c6\79\2\2\u01c6\u01c7\5$\23\2")
        buf.write("\u01c7\u01c8\b\22\1\2\u01c8\u01ce\3\2\2\2\u01c9\u01ca")
        buf.write("\7:\2\2\u01ca\u01cb\5$\23\2\u01cb\u01cc\b\22\1\2\u01cc")
        buf.write("\u01ce\3\2\2\2\u01cd\u01b9\3\2\2\2\u01cd\u01bd\3\2\2\2")
        buf.write("\u01cd\u01c1\3\2\2\2\u01cd\u01c5\3\2\2\2\u01cd\u01c9\3")
        buf.write("\2\2\2\u01ce\u01d1\3\2\2\2\u01cf\u01cd\3\2\2\2\u01cf\u01d0")
        buf.write("\3\2\2\2\u01d0#\3\2\2\2\u01d1\u01cf\3\2\2\2\u01d2\u01d3")
        buf.write("\5&\24\2\u01d3\u01de\b\23\1\2\u01d4\u01d5\7;\2\2\u01d5")
        buf.write("\u01d6\5&\24\2\u01d6\u01d7\b\23\1\2\u01d7\u01dd\3\2\2")
        buf.write("\2\u01d8\u01d9\7<\2\2\u01d9\u01da\5&\24\2\u01da\u01db")
        buf.write("\b\23\1\2\u01db\u01dd\3\2\2\2\u01dc\u01d4\3\2\2\2\u01dc")
        buf.write("\u01d8\3\2\2\2\u01dd\u01e0\3\2\2\2\u01de\u01dc\3\2\2\2")
        buf.write("\u01de\u01df\3\2\2\2\u01df%\3\2\2\2\u01e0\u01de\3\2\2")
        buf.write("\2\u01e1\u01e2\5(\25\2\u01e2\u01e7\b\24\1\2\u01e3\u01e4")
        buf.write("\7=\2\2\u01e4\u01e5\5&\24\2\u01e5\u01e6\b\24\1\2\u01e6")
        buf.write("\u01e8\3\2\2\2\u01e7\u01e3\3\2\2\2\u01e7\u01e8\3\2\2\2")
        buf.write("\u01e8\u01fa\3\2\2\2\u01e9\u01ea\7;\2\2\u01ea\u01eb\5")
        buf.write("&\24\2\u01eb\u01ec\b\24\1\2\u01ec\u01fa\3\2\2\2\u01ed")
        buf.write("\u01ee\7<\2\2\u01ee\u01ef\5&\24\2\u01ef\u01f0\b\24\1\2")
        buf.write("\u01f0\u01fa\3\2\2\2\u01f1\u01f2\7>\2\2\u01f2\u01f3\5")
        buf.write("&\24\2\u01f3\u01f4\b\24\1\2\u01f4\u01fa\3\2\2\2\u01f5")
        buf.write("\u01f6\7\65\2\2\u01f6\u01f7\5&\24\2\u01f7\u01f8\b\24\1")
        buf.write("\2\u01f8\u01fa\3\2\2\2\u01f9\u01e1\3\2\2\2\u01f9\u01e9")
        buf.write("\3\2\2\2\u01f9\u01ed\3\2\2\2\u01f9\u01f1\3\2\2\2\u01f9")
        buf.write("\u01f5\3\2\2\2\u01fa\'\3\2\2\2\u01fb\u01fc\7?\2\2\u01fc")
        buf.write("\u01fd\5(\25\2\u01fd\u01fe\b\25\1\2\u01fe\u0233\3\2\2")
        buf.write("\2\u01ff\u0200\7@\2\2\u0200\u0201\7\4\2\2\u0201\u0202")
        buf.write("\5<\37\2\u0202\u0203\7\16\2\2\u0203\u0204\5D#\2\u0204")
        buf.write("\u0205\7\5\2\2\u0205\u0206\b\25\1\2\u0206\u0233\3\2\2")
        buf.write("\2\u0207\u0208\7A\2\2\u0208\u0209\7\4\2\2\u0209\u020a")
        buf.write("\5<\37\2\u020a\u020b\7\16\2\2\u020b\u020c\5D#\2\u020c")
        buf.write("\u020d\7\5\2\2\u020d\u020e\b\25\1\2\u020e\u0233\3\2\2")
        buf.write("\2\u020f\u0210\7\4\2\2\u0210\u0211\5\22\n\2\u0211\u0212")
        buf.write("\7\5\2\2\u0212\u0213\b\25\1\2\u0213\u021b\3\2\2\2\u0214")
        buf.write("\u0215\5*\26\2\u0215\u0216\b\25\1\2\u0216\u021b\3\2\2")
        buf.write("\2\u0217\u0218\5B\"\2\u0218\u0219\b\25\1\2\u0219\u021b")
        buf.write("\3\2\2\2\u021a\u020f\3\2\2\2\u021a\u0214\3\2\2\2\u021a")
        buf.write("\u0217\3\2\2\2\u021b\u0225\3\2\2\2\u021c\u021d\7\"\2\2")
        buf.write("\u021d\u021e\5B\"\2\u021e\u021f\b\25\1\2\u021f\u0224\3")
        buf.write("\2\2\2\u0220\u0221\5\62\32\2\u0221\u0222\b\25\1\2\u0222")
        buf.write("\u0224\3\2\2\2\u0223\u021c\3\2\2\2\u0223\u0220\3\2\2\2")
        buf.write("\u0224\u0227\3\2\2\2\u0225\u0223\3\2\2\2\u0225\u0226\3")
        buf.write("\2\2\2\u0226\u022a\3\2\2\2\u0227\u0225\3\2\2\2\u0228\u0229")
        buf.write("\7?\2\2\u0229\u022b\b\25\1\2\u022a\u0228\3\2\2\2\u022a")
        buf.write("\u022b\3\2\2\2\u022b\u0233\3\2\2\2\u022c\u022d\58\35\2")
        buf.write("\u022d\u0230\b\25\1\2\u022e\u022f\7?\2\2\u022f\u0231\b")
        buf.write("\25\1\2\u0230\u022e\3\2\2\2\u0230\u0231\3\2\2\2\u0231")
        buf.write("\u0233\3\2\2\2\u0232\u01fb\3\2\2\2\u0232\u01ff\3\2\2\2")
        buf.write("\u0232\u0207\3\2\2\2\u0232\u021a\3\2\2\2\u0232\u022c\3")
        buf.write("\2\2\2\u0233)\3\2\2\2\u0234\u0235\7B\2\2\u0235\u0236\7")
        buf.write("\4\2\2\u0236\u0237\5,\27\2\u0237\u0238\7\5\2\2\u0238\u0239")
        buf.write("\7\6\2\2\u0239\u023a\5\2\2\2\u023a\u023b\7\7\2\2\u023b")
        buf.write("\u023c\b\26\1\2\u023c\u0250\3\2\2\2\u023d\u023e\7C\2\2")
        buf.write("\u023e\u023f\7\4\2\2\u023f\u0240\5,\27\2\u0240\u0241\7")
        buf.write("\5\2\2\u0241\u0242\7\6\2\2\u0242\u0243\5\2\2\2\u0243\u0244")
        buf.write("\7\7\2\2\u0244\u0245\b\26\1\2\u0245\u0250\3\2\2\2\u0246")
        buf.write("\u0247\7D\2\2\u0247\u0248\7\4\2\2\u0248\u0249\5,\27\2")
        buf.write("\u0249\u024a\7\5\2\2\u024a\u024b\7\6\2\2\u024b\u024c\5")
        buf.write("\2\2\2\u024c\u024d\7\7\2\2\u024d\u024e\b\26\1\2\u024e")
        buf.write("\u0250\3\2\2\2\u024f\u0234\3\2\2\2\u024f\u023d\3\2\2\2")
        buf.write("\u024f\u0246\3\2\2\2\u0250+\3\2\2\2\u0251\u0252\5.\30")
        buf.write("\2\u0252\u0259\b\27\1\2\u0253\u0254\7\32\2\2\u0254\u0255")
        buf.write("\5.\30\2\u0255\u0256\b\27\1\2\u0256\u0258\3\2\2\2\u0257")
        buf.write("\u0253\3\2\2\2\u0258\u025b\3\2\2\2\u0259\u0257\3\2\2\2")
        buf.write("\u0259\u025a\3\2\2\2\u025a\u0262\3\2\2\2\u025b\u0259\3")
        buf.write("\2\2\2\u025c\u025d\7\32\2\2\u025d\u025e\5\60\31\2\u025e")
        buf.write("\u025f\b\27\1\2\u025f\u0261\3\2\2\2\u0260\u025c\3\2\2")
        buf.write("\2\u0261\u0264\3\2\2\2\u0262\u0260\3\2\2\2\u0262\u0263")
        buf.write("\3\2\2\2\u0263\u0272\3\2\2\2\u0264\u0262\3\2\2\2\u0265")
        buf.write("\u0266\5\60\31\2\u0266\u026d\b\27\1\2\u0267\u0268\7\32")
        buf.write("\2\2\u0268\u0269\5\60\31\2\u0269\u026a\b\27\1\2\u026a")
        buf.write("\u026c\3\2\2\2\u026b\u0267\3\2\2\2\u026c\u026f\3\2\2\2")
        buf.write("\u026d\u026b\3\2\2\2\u026d\u026e\3\2\2\2\u026e\u0272\3")
        buf.write("\2\2\2\u026f\u026d\3\2\2\2\u0270\u0272\3\2\2\2\u0271\u0251")
        buf.write("\3\2\2\2\u0271\u0265\3\2\2\2\u0271\u0270\3\2\2\2\u0272")
        buf.write("-\3\2\2\2\u0273\u0274\6\30\3\3\u0274\u0275\7E\2\2\u0275")
        buf.write("\u0276\5\f\7\2\u0276\u0277\b\30\1\2\u0277\u027c\3\2\2")
        buf.write("\2\u0278\u0279\5B\"\2\u0279\u027a\b\30\1\2\u027a\u027c")
        buf.write("\3\2\2\2\u027b\u0273\3\2\2\2\u027b\u0278\3\2\2\2\u027c")
        buf.write("/\3\2\2\2\u027d\u027e\5\f\7\2\u027e\u027f\7!\2\2\u027f")
        buf.write("\u0280\5\16\b\2\u0280\u0281\b\31\1\2\u0281\61\3\2\2\2")
        buf.write("\u0282\u0283\7\4\2\2\u0283\u0284\5\66\34\2\u0284\u0285")
        buf.write("\7\5\2\2\u0285\u0286\b\32\1\2\u0286\u028d\3\2\2\2\u0287")
        buf.write("\u0288\7#\2\2\u0288\u0289\5\64\33\2\u0289\u028a\7$\2\2")
        buf.write("\u028a\u028b\b\32\1\2\u028b\u028d\3\2\2\2\u028c\u0282")
        buf.write("\3\2\2\2\u028c\u0287\3\2\2\2\u028d\63\3\2\2\2\u028e\u02a1")
        buf.write("\5\16\b\2\u028f\u0294\7L\2\2\u0290\u0291\5\16\b\2\u0291")
        buf.write("\u0292\b\33\1\2\u0292\u0295\3\2\2\2\u0293\u0295\b\33\1")
        buf.write("\2\u0294\u0290\3\2\2\2\u0294\u0293\3\2\2\2\u0295\u02a2")
        buf.write("\3\2\2\2\u0296\u0297\7\32\2\2\u0297\u0298\5\16\b\2\u0298")
        buf.write("\u0299\b\33\1\2\u0299\u029b\3\2\2\2\u029a\u0296\3\2\2")
        buf.write("\2\u029b\u029c\3\2\2\2\u029c\u029a\3\2\2\2\u029c\u029d")
        buf.write("\3\2\2\2\u029d\u029e\3\2\2\2\u029e\u029f\b\33\1\2\u029f")
        buf.write("\u02a2\3\2\2\2\u02a0\u02a2\b\33\1\2\u02a1\u028f\3\2\2")
        buf.write("\2\u02a1\u029a\3\2\2\2\u02a1\u02a0\3\2\2\2\u02a2\u02a8")
        buf.write("\3\2\2\2\u02a3\u02a4\7L\2\2\u02a4\u02a5\5\16\b\2\u02a5")
        buf.write("\u02a6\b\33\1\2\u02a6\u02a8\3\2\2\2\u02a7\u028e\3\2\2")
        buf.write("\2\u02a7\u02a3\3\2\2\2\u02a8\65\3\2\2\2\u02a9\u02aa\5")
        buf.write("\20\t\2\u02aa\u02ab\b\34\1\2\u02ab\u02ae\3\2\2\2\u02ac")
        buf.write("\u02ae\3\2\2\2\u02ad\u02a9\3\2\2\2\u02ad\u02ac\3\2\2\2")
        buf.write("\u02ae\67\3\2\2\2\u02af\u02b3\7#\2\2\u02b0\u02b1\5:\36")
        buf.write("\2\u02b1\u02b2\b\35\1\2\u02b2\u02b4\3\2\2\2\u02b3\u02b0")
        buf.write("\3\2\2\2\u02b3\u02b4\3\2\2\2\u02b4\u02b5\3\2\2\2\u02b5")
        buf.write("\u02b6\7$\2\2\u02b6\u02ca\b\35\1\2\u02b7\u02bb\7\6\2\2")
        buf.write("\u02b8\u02b9\5:\36\2\u02b9\u02ba\b\35\1\2\u02ba\u02bc")
        buf.write("\3\2\2\2\u02bb\u02b8\3\2\2\2\u02bb\u02bc\3\2\2\2\u02bc")
        buf.write("\u02bd\3\2\2\2\u02bd\u02be\7\7\2\2\u02be\u02ca\b\35\1")
        buf.write("\2\u02bf\u02c0\7M\2\2\u02c0\u02ca\b\35\1\2\u02c1\u02c2")
        buf.write("\7N\2\2\u02c2\u02ca\b\35\1\2\u02c3\u02c4\5@!\2\u02c4\u02c5")
        buf.write("\b\35\1\2\u02c5\u02ca\3\2\2\2\u02c6\u02c7\6\35\4\3\u02c7")
        buf.write("\u02c8\7%\2\2\u02c8\u02ca\b\35\1\2\u02c9\u02af\3\2\2\2")
        buf.write("\u02c9\u02b7\3\2\2\2\u02c9\u02bf\3\2\2\2\u02c9\u02c1\3")
        buf.write("\2\2\2\u02c9\u02c3\3\2\2\2\u02c9\u02c6\3\2\2\2\u02ca9")
        buf.write("\3\2\2\2\u02cb\u02fa\5\16\b\2\u02cc\u02cd\7\32\2\2\u02cd")
        buf.write("\u02e3\5\16\b\2\u02ce\u02cf\7L\2\2\u02cf\u02d0\5\16\b")
        buf.write("\2\u02d0\u02d1\b\36\1\2\u02d1\u02e4\3\2\2\2\u02d2\u02d9")
        buf.write("\b\36\1\2\u02d3\u02d4\7\32\2\2\u02d4\u02d5\5\16\b\2\u02d5")
        buf.write("\u02d6\b\36\1\2\u02d6\u02d8\3\2\2\2\u02d7\u02d3\3\2\2")
        buf.write("\2\u02d8\u02db\3\2\2\2\u02d9\u02d7\3\2\2\2\u02d9\u02da")
        buf.write("\3\2\2\2\u02da\u02e1\3\2\2\2\u02db\u02d9\3\2\2\2\u02dc")
        buf.write("\u02dd\7\16\2\2\u02dd\u02de\5\16\b\2\u02de\u02df\b\36")
        buf.write("\1\2\u02df\u02e2\3\2\2\2\u02e0\u02e2\b\36\1\2\u02e1\u02dc")
        buf.write("\3\2\2\2\u02e1\u02e0\3\2\2\2\u02e2\u02e4\3\2\2\2\u02e3")
        buf.write("\u02ce\3\2\2\2\u02e3\u02d2\3\2\2\2\u02e4\u02fb\3\2\2\2")
        buf.write("\u02e5\u02e6\7L\2\2\u02e6\u02e7\5\16\b\2\u02e7\u02e8\b")
        buf.write("\36\1\2\u02e8\u02fb\3\2\2\2\u02e9\u02ef\b\36\1\2\u02ea")
        buf.write("\u02eb\7\16\2\2\u02eb\u02ec\5\16\b\2\u02ec\u02ed\b\36")
        buf.write("\1\2\u02ed\u02f0\3\2\2\2\u02ee\u02f0\b\36\1\2\u02ef\u02ea")
        buf.write("\3\2\2\2\u02ef\u02ee\3\2\2\2\u02f0\u02fb\3\2\2\2\u02f1")
        buf.write("\u02f2\7\13\2\2\u02f2\u02f8\5<\37\2\u02f3\u02f4\7\16\2")
        buf.write("\2\u02f4\u02f5\5D#\2\u02f5\u02f6\b\36\1\2\u02f6\u02f9")
        buf.write("\3\2\2\2\u02f7\u02f9\b\36\1\2\u02f8\u02f3\3\2\2\2\u02f8")
        buf.write("\u02f7\3\2\2\2\u02f9\u02fb\3\2\2\2\u02fa\u02cc\3\2\2\2")
        buf.write("\u02fa\u02e5\3\2\2\2\u02fa\u02e9\3\2\2\2\u02fa\u02f1\3")
        buf.write("\2\2\2\u02fb;\3\2\2\2\u02fc\u02fd\5> \2\u02fd\u0304\b")
        buf.write("\37\1\2\u02fe\u02ff\7\32\2\2\u02ff\u0300\5> \2\u0300\u0301")
        buf.write("\b\37\1\2\u0301\u0303\3\2\2\2\u0302\u02fe\3\2\2\2\u0303")
        buf.write("\u0306\3\2\2\2\u0304\u0302\3\2\2\2\u0304\u0305\3\2\2\2")
        buf.write("\u0305=\3\2\2\2\u0306\u0304\3\2\2\2\u0307\u0308\5\n\6")
        buf.write("\2\u0308\u0309\7\62\2\2\u0309\u030a\5\16\b\2\u030a\u030b")
        buf.write("\b \1\2\u030b?\3\2\2\2\u030c\u030d\7J\2\2\u030d\u0317")
        buf.write("\b!\1\2\u030e\u030f\7K\2\2\u030f\u0317\b!\1\2\u0310\u0311")
        buf.write("\7F\2\2\u0311\u0317\b!\1\2\u0312\u0313\7G\2\2\u0313\u0317")
        buf.write("\b!\1\2\u0314\u0315\7H\2\2\u0315\u0317\b!\1\2\u0316\u030c")
        buf.write("\3\2\2\2\u0316\u030e\3\2\2\2\u0316\u0310\3\2\2\2\u0316")
        buf.write("\u0312\3\2\2\2\u0316\u0314\3\2\2\2\u0317A\3\2\2\2\u0318")
        buf.write("\u0319\7I\2\2\u0319\u031a\b\"\1\2\u031aC\3\2\2\2\u031b")
        buf.write("\u031c\5\16\b\2\u031c\u031d\b#\1\2\u031dE\3\2\2\2\u031e")
        buf.write("\u031f\5\n\6\2\u031f\u0326\b$\1\2\u0320\u0321\7\32\2\2")
        buf.write("\u0321\u0322\5\n\6\2\u0322\u0323\b$\1\2\u0323\u0325\3")
        buf.write("\2\2\2\u0324\u0320\3\2\2\2\u0325\u0328\3\2\2\2\u0326\u0324")
        buf.write("\3\2\2\2\u0326\u0327\3\2\2\2\u0327G\3\2\2\2\u0328\u0326")
        buf.write("\3\2\2\2AMen|\u0082\u008d\u00b6\u00ca\u00e3\u00fe\u010d")
        buf.write("\u010f\u011c\u011e\u0129\u0139\u0149\u014b\u015e\u0161")
        buf.write("\u0164\u016c\u0176\u0181\u01a6\u01b2\u01b4\u01cd\u01cf")
        buf.write("\u01dc\u01de\u01e7\u01f9\u021a\u0223\u0225\u022a\u0230")
        buf.write("\u0232\u024f\u0259\u0262\u026d\u0271\u027b\u028c\u0294")
        buf.write("\u029c\u02a1\u02a7\u02ad\u02b3\u02bb\u02c9\u02d9\u02e1")
        buf.write("\u02e3\u02ef\u02f8\u02fa\u0304\u0316\u0326")
        return buf.getvalue()


class SetlXgrammarParser ( Parser ):

    grammarFileName = "SetlXgrammar.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'if'", "'('", "')'", "'{'", "'}'", "'else'", 
                     "'switch'", "'case'", "':'", "'default'", "'for'", 
                     "'|'", "'while'", "'do'", "';'", "'try'", "'catch'", 
                     "'backtrack'", "'break'", "'continue'", "'exit'", "'return'", 
                     "'assert'", "','", "'+='", "'-='", "'*='", "'/='", 
                     "'\\='", "'%='", "':='", "'.'", "'['", "']'", "'_'", 
                     "'<==>'", "'<!=>'", "'|=>'", "'=>'", "'||'", "'&&'", 
                     "'=='", "'!='", "'<'", "'<='", "'>'", "'>='", "'in'", 
                     "'notin'", "'+'", "'-'", "'*'", "'/'", "'\\'", "'%'", 
                     "'><'", "'+/'", "'*/'", "'**'", "'#'", "'!'", "'forall'", 
                     "'exists'", "'procedure'", "'cachedProcedure'", "'closure'", 
                     "'rw'", "'om'", "'true'", "'false'", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "'..'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "ID", "NUMBER", 
                      "DOUBLE", "RANGE_SIGN", "STRING", "LITERAL", "LINE_COMMENT", 
                      "MULTI_COMMENT", "WS", "REMAINDER" ]

    RULE_block = 0
    RULE_statement = 1
    RULE_assignmentOther = 2
    RULE_assignmentDirect = 3
    RULE_assignable = 4
    RULE_assignableVariable = 5
    RULE_expr = 6
    RULE_exprList = 7
    RULE_exprContent = 8
    RULE_lambdaProcedure = 9
    RULE_lambdaParameters = 10
    RULE_implication = 11
    RULE_disjunction = 12
    RULE_conjunction = 13
    RULE_comparison = 14
    RULE_setlxSum = 15
    RULE_product = 16
    RULE_setlxReduce = 17
    RULE_prefixOperation = 18
    RULE_factor = 19
    RULE_procedure = 20
    RULE_procedureParameters = 21
    RULE_procedureParameter = 22
    RULE_procedureDefaultParameter = 23
    RULE_call = 24
    RULE_collectionAccessParams = 25
    RULE_callParameters = 26
    RULE_value = 27
    RULE_collectionBuilder = 28
    RULE_iteratorChain = 29
    RULE_iterator = 30
    RULE_atomicValue = 31
    RULE_variable = 32
    RULE_condition = 33
    RULE_assignmentList = 34

    ruleNames =  [ "block", "statement", "assignmentOther", "assignmentDirect", 
                   "assignable", "assignableVariable", "expr", "exprList", 
                   "exprContent", "lambdaProcedure", "lambdaParameters", 
                   "implication", "disjunction", "conjunction", "comparison", 
                   "setlxSum", "product", "setlxReduce", "prefixOperation", 
                   "factor", "procedure", "procedureParameters", "procedureParameter", 
                   "procedureDefaultParameter", "call", "collectionAccessParams", 
                   "callParameters", "value", "collectionBuilder", "iteratorChain", 
                   "iterator", "atomicValue", "variable", "condition", "assignmentList" ]

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
    T__23=24
    T__24=25
    T__25=26
    T__26=27
    T__27=28
    T__28=29
    T__29=30
    T__30=31
    T__31=32
    T__32=33
    T__33=34
    T__34=35
    T__35=36
    T__36=37
    T__37=38
    T__38=39
    T__39=40
    T__40=41
    T__41=42
    T__42=43
    T__43=44
    T__44=45
    T__45=46
    T__46=47
    T__47=48
    T__48=49
    T__49=50
    T__50=51
    T__51=52
    T__52=53
    T__53=54
    T__54=55
    T__55=56
    T__56=57
    T__57=58
    T__58=59
    T__59=60
    T__60=61
    T__61=62
    T__62=63
    T__63=64
    T__64=65
    T__65=66
    T__66=67
    T__67=68
    T__68=69
    T__69=70
    ID=71
    NUMBER=72
    DOUBLE=73
    RANGE_SIGN=74
    STRING=75
    LITERAL=76
    LINE_COMMENT=77
    MULTI_COMMENT=78
    WS=79
    REMAINDER=80

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
            self.state = 75
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,0,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 70
                    localctx._statement = self.statement()
                    stmnts.append(localctx._statement.stmnt) 
                self.state = 77
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
            self.c1 = None # ConditionContext
            self.b1 = None # BlockContext
            self.c2 = None # ConditionContext
            self.b2 = None # BlockContext
            self.b3 = None # BlockContext
            self._iteratorChain = None # IteratorChainContext
            self._condition = None # ConditionContext
            self._block = None # BlockContext
            self.v2 = None # AssignableVariableContext
            self._expr = None # ExprContext
            self._assignmentOther = None # AssignmentOtherContext
            self._assignmentDirect = None # AssignmentDirectContext

        def condition(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SetlXgrammarParser.ConditionContext)
            else:
                return self.getTypedRuleContext(SetlXgrammarParser.ConditionContext,i)


        def block(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SetlXgrammarParser.BlockContext)
            else:
                return self.getTypedRuleContext(SetlXgrammarParser.BlockContext,i)


        def iteratorChain(self):
            return self.getTypedRuleContext(SetlXgrammarParser.IteratorChainContext,0)


        def assignableVariable(self):
            return self.getTypedRuleContext(SetlXgrammarParser.AssignableVariableContext,0)


        def expr(self):
            return self.getTypedRuleContext(SetlXgrammarParser.ExprContext,0)


        def assignmentOther(self):
            return self.getTypedRuleContext(SetlXgrammarParser.AssignmentOtherContext,0)


        def assignmentDirect(self):
            return self.getTypedRuleContext(SetlXgrammarParser.AssignmentDirectContext,0)


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

        else_list = []
        caseList = []
        tryList = []
        expression = None
        condition = None
            
        self._la = 0 # Token type
        try:
            self.state = 225
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,8,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 80
                self.match(SetlXgrammarParser.T__0)
                self.state = 81
                self.match(SetlXgrammarParser.T__1)
                self.state = 82
                localctx.c1 = self.condition()
                self.state = 83
                self.match(SetlXgrammarParser.T__2)
                self.state = 84
                self.match(SetlXgrammarParser.T__3)
                self.state = 85
                localctx.b1 = self.block()
                self.state = 86
                self.match(SetlXgrammarParser.T__4)
                self.state = 99
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,1,self._ctx)
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1:
                        self.state = 87
                        self.match(SetlXgrammarParser.T__5)
                        self.state = 88
                        self.match(SetlXgrammarParser.T__0)
                        self.state = 89
                        self.match(SetlXgrammarParser.T__1)
                        self.state = 90
                        localctx.c2 = self.condition()
                        self.state = 91
                        self.match(SetlXgrammarParser.T__2)
                        self.state = 92
                        self.match(SetlXgrammarParser.T__3)
                        self.state = 93
                        localctx.b2 = self.block()
                        self.state = 94
                        self.match(SetlXgrammarParser.T__4)
                        else_list.append(IfThenBranch(localctx.c2.cnd,localctx.b2.blk)) 
                        			 
                    self.state = 101
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,1,self._ctx)

                self.state = 108
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
                if la_ == 1:
                    self.state = 102
                    self.match(SetlXgrammarParser.T__5)
                    self.state = 103
                    self.match(SetlXgrammarParser.T__3)
                    self.state = 104
                    localctx.b3 = self.block()
                    self.state = 105
                    self.match(SetlXgrammarParser.T__4)
                    else_list.append(localctx.b3.blk) 


                localctx.stmnt = IfThen(localctx.c1.cnd,localctx.b1.blk,else_list) 
                		
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 112
                self.match(SetlXgrammarParser.T__6)
                self.state = 113
                self.match(SetlXgrammarParser.T__3)
                self.state = 122
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==SetlXgrammarParser.T__7:
                    self.state = 114
                    self.match(SetlXgrammarParser.T__7)
                    self.state = 115
                    localctx.c1 = self.condition()
                    self.state = 116
                    self.match(SetlXgrammarParser.T__8)
                    self.state = 117
                    localctx.b1 = self.block()
                    caseList.append((localctx.c1.cnd, localctx.b1.blk)) 
                    self.state = 124
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 128
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==SetlXgrammarParser.T__9:
                    self.state = 125
                    self.match(SetlXgrammarParser.T__9)
                    self.state = 126
                    self.match(SetlXgrammarParser.T__8)
                    self.state = 127
                    localctx.b2 = self.block()


                self.state = 130
                self.match(SetlXgrammarParser.T__4)
                localctx.stmnt = Switch(caseList,localctx.b2.blk) 
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 132
                self.match(SetlXgrammarParser.T__10)
                self.state = 133
                self.match(SetlXgrammarParser.T__1)
                self.state = 134
                localctx._iteratorChain = self.iteratorChain(False)
                self.state = 139
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==SetlXgrammarParser.T__11:
                    self.state = 135
                    self.match(SetlXgrammarParser.T__11)
                    self.state = 136
                    localctx._condition = self.condition()
                    condition = localctx._condition.cnd


                self.state = 141
                self.match(SetlXgrammarParser.T__2)
                self.state = 142
                self.match(SetlXgrammarParser.T__3)
                self.state = 143
                localctx._block = self.block()
                self.state = 144
                self.match(SetlXgrammarParser.T__4)
                localctx.stmnt = For(localctx._iteratorChain.ic, condition, localctx._block.blk) 
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 147
                self.match(SetlXgrammarParser.T__12)
                self.state = 148
                self.match(SetlXgrammarParser.T__1)
                self.state = 149
                localctx._condition = self.condition()
                self.state = 150
                self.match(SetlXgrammarParser.T__2)
                self.state = 151
                self.match(SetlXgrammarParser.T__3)
                self.state = 152
                localctx._block = self.block()
                self.state = 153
                self.match(SetlXgrammarParser.T__4)
                localctx.stmnt = While(localctx._condition.cnd, localctx._block.blk) 
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 156
                self.match(SetlXgrammarParser.T__13)
                self.state = 157
                self.match(SetlXgrammarParser.T__3)
                self.state = 158
                localctx._block = self.block()
                self.state = 159
                self.match(SetlXgrammarParser.T__4)
                self.state = 160
                self.match(SetlXgrammarParser.T__12)
                self.state = 161
                self.match(SetlXgrammarParser.T__1)
                self.state = 162
                localctx._condition = self.condition()
                self.state = 163
                self.match(SetlXgrammarParser.T__2)
                self.state = 164
                self.match(SetlXgrammarParser.T__14)
                localctx.stmnt = DoWhile(localctx._condition.cnd, localctx._block.blk) 
                		
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 167
                self.match(SetlXgrammarParser.T__15)
                self.state = 168
                self.match(SetlXgrammarParser.T__3)
                self.state = 169
                localctx.b1 = self.block()
                self.state = 170
                self.match(SetlXgrammarParser.T__4)
                self.state = 180
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,6,self._ctx)
                if la_ == 1:
                    self.state = 171
                    self.match(SetlXgrammarParser.T__16)
                    self.state = 172
                    self.match(SetlXgrammarParser.T__1)
                    self.state = 173
                    localctx.v2 = self.assignableVariable()
                    self.state = 174
                    self.match(SetlXgrammarParser.T__2)
                    self.state = 175
                    self.match(SetlXgrammarParser.T__3)
                    self.state = 176
                    localctx.b3 = self.block()
                    self.state = 177
                    self.match(SetlXgrammarParser.T__4)
                    tryList.append(TryCatchBranch(localctx.v2.v, localctx.b3.blk))         
                    			


                localctx.stmnt = TryCatch(localctx.b1.blk, tryList) 
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 184
                self.match(SetlXgrammarParser.T__17)
                self.state = 185
                self.match(SetlXgrammarParser.T__14)
                localctx.stmnt = Backtrack() 
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 187
                self.match(SetlXgrammarParser.T__18)
                self.state = 188
                self.match(SetlXgrammarParser.T__14)
                localctx.stmnt = Break() 
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 190
                self.match(SetlXgrammarParser.T__19)
                self.state = 191
                self.match(SetlXgrammarParser.T__14)
                localctx.stmnt = Continue() 
                pass

            elif la_ == 10:
                self.enterOuterAlt(localctx, 10)
                self.state = 193
                self.match(SetlXgrammarParser.T__20)
                self.state = 194
                self.match(SetlXgrammarParser.T__14)
                localctx.stmnt = Exit() 
                pass

            elif la_ == 11:
                self.enterOuterAlt(localctx, 11)
                self.state = 196
                self.match(SetlXgrammarParser.T__21)
                self.state = 200
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,7,self._ctx)
                if la_ == 1:
                    self.state = 197
                    localctx._expr = self.expr(False)
                    expression = localctx._expr.ex 


                self.state = 202
                self.match(SetlXgrammarParser.T__14)
                localctx.stmnt = Return(expression) 
                pass

            elif la_ == 12:
                self.enterOuterAlt(localctx, 12)
                self.state = 204
                self.match(SetlXgrammarParser.T__22)
                self.state = 205
                self.match(SetlXgrammarParser.T__1)
                self.state = 206
                localctx._condition = self.condition()
                self.state = 207
                self.match(SetlXgrammarParser.T__23)
                self.state = 208
                localctx._expr = self.expr(False)
                self.state = 209
                self.match(SetlXgrammarParser.T__2)
                self.state = 210
                self.match(SetlXgrammarParser.T__14)
                localctx.stmnt = Assert(localctx._condition.cnd, localctx._expr.ex)
                pass

            elif la_ == 13:
                self.enterOuterAlt(localctx, 13)
                self.state = 213
                localctx._assignmentOther = self.assignmentOther()
                self.state = 214
                self.match(SetlXgrammarParser.T__14)
                localctx.stmnt = localctx._assignmentOther.assign 
                pass

            elif la_ == 14:
                self.enterOuterAlt(localctx, 14)
                self.state = 217
                localctx._assignmentDirect = self.assignmentDirect()
                self.state = 218
                self.match(SetlXgrammarParser.T__14)
                localctx.stmnt = localctx._assignmentDirect.assign 
                pass

            elif la_ == 15:
                self.enterOuterAlt(localctx, 15)
                self.state = 221
                localctx._expr = self.expr(False)
                self.state = 222
                self.match(SetlXgrammarParser.T__14)
                localctx.stmnt = localctx._expr.ex
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class AssignmentOtherContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.assign = None
            self._assignable = None # AssignableContext
            self.e = None # ExprContext

        def assignable(self):
            return self.getTypedRuleContext(SetlXgrammarParser.AssignableContext,0)


        def expr(self):
            return self.getTypedRuleContext(SetlXgrammarParser.ExprContext,0)


        def getRuleIndex(self):
            return SetlXgrammarParser.RULE_assignmentOther

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAssignmentOther" ):
                listener.enterAssignmentOther(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAssignmentOther" ):
                listener.exitAssignmentOther(self)




    def assignmentOther(self):

        localctx = SetlXgrammarParser.AssignmentOtherContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_assignmentOther)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 227
            localctx._assignable = self.assignable(False)
            self.state = 252
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [SetlXgrammarParser.T__24]:
                self.state = 228
                self.match(SetlXgrammarParser.T__24)
                self.state = 229
                localctx.e = self.expr(False)
                localctx.assign = SumAssignment(localctx._assignable.a, localctx.e.ex) 
                pass
            elif token in [SetlXgrammarParser.T__25]:
                self.state = 232
                self.match(SetlXgrammarParser.T__25)
                self.state = 233
                localctx.e = self.expr(False)
                localctx.assign = DifferenceAssignment(localctx._assignable.a, localctx.e.ex) 
                pass
            elif token in [SetlXgrammarParser.T__26]:
                self.state = 236
                self.match(SetlXgrammarParser.T__26)
                self.state = 237
                localctx.e = self.expr(False)
                localctx.assign = ProductAssignment(localctx._assignable.a, localctx.e.ex) 
                pass
            elif token in [SetlXgrammarParser.T__27]:
                self.state = 240
                self.match(SetlXgrammarParser.T__27)
                self.state = 241
                localctx.e = self.expr(False)
                localctx.assign = QuotientAssignment(localctx._assignable.a, localctx.e.ex) 
                pass
            elif token in [SetlXgrammarParser.T__28]:
                self.state = 244
                self.match(SetlXgrammarParser.T__28)
                self.state = 245
                localctx.e = self.expr(False)
                localctx.assign = IntegerDivisionAssignment(localctx._assignable.a, localctx.e.ex) 
                pass
            elif token in [SetlXgrammarParser.T__29]:
                self.state = 248
                self.match(SetlXgrammarParser.T__29)
                self.state = 249
                localctx.e = self.expr(False)
                localctx.assign = ModuloAssignment(localctx._assignable.a, localctx.e.ex) 
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

    class AssignmentDirectContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.assign = None
            self._variable = None # VariableContext
            self._procedure = None # ProcedureContext
            self._assignable = None # AssignableContext
            self._assignmentDirect = None # AssignmentDirectContext
            self._exprContent = None # ExprContentContext

        def variable(self):
            return self.getTypedRuleContext(SetlXgrammarParser.VariableContext,0)


        def procedure(self):
            return self.getTypedRuleContext(SetlXgrammarParser.ProcedureContext,0)


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
        self.enterRule(localctx, 6, self.RULE_assignmentDirect)
        try:
            self.state = 269
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,11,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 254
                localctx._variable = self.variable()
                self.state = 255
                self.match(SetlXgrammarParser.T__30)
                self.state = 256
                localctx._procedure = self.procedure()

                localctx._procedure.pd.name = localctx._variable.v.id
                localctx.assign = localctx._procedure.pd
                    
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 259
                localctx._assignable = self.assignable(False)
                self.state = 260
                self.match(SetlXgrammarParser.T__30)
                self.state = 267
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,10,self._ctx)
                if la_ == 1:
                    self.state = 261
                    localctx._assignmentDirect = self.assignmentDirect()
                    localctx.assign = Assignment(localctx._assignable.a, localctx._assignmentDirect.assign) 
                    pass

                elif la_ == 2:
                    self.state = 264
                    localctx._exprContent = self.exprContent(False)
                    localctx.assign = Assignment(localctx._assignable.a, localctx._exprContent.ex) 
                    pass


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
            self._exprList = None # ExprListContext
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
        self.enterRule(localctx, 8, self.RULE_assignable)
        self._la = 0 # Token type
        try:
            self.state = 295
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,14,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 271
                localctx._assignableVariable = self.assignableVariable()
                localctx.a = localctx._assignableVariable.v
                self.state = 284
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==SetlXgrammarParser.T__31 or _la==SetlXgrammarParser.T__32:
                    self.state = 282
                    self._errHandler.sync(self)
                    token = self._input.LA(1)
                    if token in [SetlXgrammarParser.T__31]:
                        self.state = 273
                        self.match(SetlXgrammarParser.T__31)
                        self.state = 274
                        localctx._variable = self.variable()
                        localctx.a = AssignableMember(localctx.a, localctx._variable.v)
                        pass
                    elif token in [SetlXgrammarParser.T__32]:
                        self.state = 277
                        self.match(SetlXgrammarParser.T__32)
                        self.state = 278
                        localctx._exprList = self.exprList(False)
                        self.state = 279
                        self.match(SetlXgrammarParser.T__33)
                        localctx.a = AssignableCollectionAccess(localctx.a, localctx._exprList.exprs)
                        pass
                    else:
                        raise NoViableAltException(self)

                    self.state = 286
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 287
                self.match(SetlXgrammarParser.T__32)
                self.state = 288
                localctx._assignmentList = self.assignmentList()
                self.state = 289
                self.match(SetlXgrammarParser.T__33)
                localctx.a = AssignableList(localctx._assignmentList.al)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 292
                if not localctx.enableIgnore:
                    from antlr4.error.Errors import FailedPredicateException
                    raise FailedPredicateException(self, "$enableIgnore")
                self.state = 293
                self.match(SetlXgrammarParser.T__34)
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
        self.enterRule(localctx, 10, self.RULE_assignableVariable)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 297
            localctx._ID = self.match(SetlXgrammarParser.ID)
            localctx.v = Variable((None if localctx._ID is None else localctx._ID.text)) 
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
        self.enterRule(localctx, 12, self.RULE_expr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 300
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
        self.enterRule(localctx, 14, self.RULE_exprList)

        localctx.exprs = []
            
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 303
            localctx._exprContent = self.exprContent(localctx.enableIgnore)
            localctx.exprs.append(localctx._exprContent.ex)
            self.state = 311
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==SetlXgrammarParser.T__23:
                self.state = 305
                self.match(SetlXgrammarParser.T__23)
                self.state = 306
                localctx._exprContent = self.exprContent(localctx.enableIgnore)
                localctx.exprs.append(localctx._exprContent.ex)
                self.state = 313
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
            self._lambdaProcedure = None # LambdaProcedureContext
            self._implication = None # ImplicationContext
            self.enableIgnore = enableIgnore

        def lambdaProcedure(self):
            return self.getTypedRuleContext(SetlXgrammarParser.LambdaProcedureContext,0)


        def implication(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SetlXgrammarParser.ImplicationContext)
            else:
                return self.getTypedRuleContext(SetlXgrammarParser.ImplicationContext,i)


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
        self.enterRule(localctx, 16, self.RULE_exprContent)
        try:
            self.state = 329
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,17,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 314
                localctx._lambdaProcedure = self.lambdaProcedure()
                localctx.ex = localctx._lambdaProcedure.lp 
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 317
                localctx._implication = self.implication(localctx.enableIgnore)
                localctx.ex = localctx._implication.i
                self.state = 327
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [SetlXgrammarParser.T__35]:
                    self.state = 319
                    self.match(SetlXgrammarParser.T__35)
                    self.state = 320
                    localctx._implication = self.implication(localctx.enableIgnore)
                    localctx.ex = BooleanEqual(localctx.ex,localctx._implication.i) 
                    pass
                elif token in [SetlXgrammarParser.T__36]:
                    self.state = 323
                    self.match(SetlXgrammarParser.T__36)
                    self.state = 324
                    localctx._implication = self.implication(localctx.enableIgnore)
                    localctx.ex = BooleanNotEqual(localctx.ex,localctx._implication.i) 
                    pass
                elif token in [SetlXgrammarParser.T__2, SetlXgrammarParser.T__4, SetlXgrammarParser.T__8, SetlXgrammarParser.T__11, SetlXgrammarParser.T__14, SetlXgrammarParser.T__23, SetlXgrammarParser.T__33, SetlXgrammarParser.RANGE_SIGN]:
                    pass
                else:
                    pass
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class LambdaProcedureContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.lp = None
            self._lambdaParameters = None # LambdaParametersContext
            self._expr = None # ExprContext

        def lambdaParameters(self):
            return self.getTypedRuleContext(SetlXgrammarParser.LambdaParametersContext,0)


        def expr(self):
            return self.getTypedRuleContext(SetlXgrammarParser.ExprContext,0)


        def getRuleIndex(self):
            return SetlXgrammarParser.RULE_lambdaProcedure

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLambdaProcedure" ):
                listener.enterLambdaProcedure(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLambdaProcedure" ):
                listener.exitLambdaProcedure(self)




    def lambdaProcedure(self):

        localctx = SetlXgrammarParser.LambdaProcedureContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_lambdaProcedure)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 331
            localctx._lambdaParameters = self.lambdaParameters()

            self.state = 332
            self.match(SetlXgrammarParser.T__37)
            self.state = 333
            localctx._expr = self.expr(False)
            localctx.lp = LambdaClosure(localctx._lambdaParameters.paramList, localctx._expr.ex)   
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class LambdaParametersContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.paramList = None
            self._variable = None # VariableContext
            self.v1 = None # VariableContext
            self.v2 = None # VariableContext

        def variable(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SetlXgrammarParser.VariableContext)
            else:
                return self.getTypedRuleContext(SetlXgrammarParser.VariableContext,i)


        def getRuleIndex(self):
            return SetlXgrammarParser.RULE_lambdaParameters

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLambdaParameters" ):
                listener.enterLambdaParameters(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLambdaParameters" ):
                listener.exitLambdaParameters(self)




    def lambdaParameters(self):

        localctx = SetlXgrammarParser.LambdaParametersContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_lambdaParameters)

        localctx.paramList = []
            
        self._la = 0 # Token type
        try:
            self.state = 354
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [SetlXgrammarParser.ID]:
                self.enterOuterAlt(localctx, 1)
                self.state = 336
                localctx._variable = self.variable()
                localctx.paramList.append(Parameter(localctx._variable.v.id)) 
                pass
            elif token in [SetlXgrammarParser.T__32]:
                self.enterOuterAlt(localctx, 2)
                self.state = 339
                self.match(SetlXgrammarParser.T__32)
                self.state = 351
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==SetlXgrammarParser.ID:
                    self.state = 340
                    localctx.v1 = self.variable()
                    localctx.paramList.append(Parameter(localctx.v1.v.id))
                    self.state = 348
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    while _la==SetlXgrammarParser.T__23:
                        self.state = 342
                        self.match(SetlXgrammarParser.T__23)
                        self.state = 343
                        localctx.v2 = self.variable()
                        localctx.paramList.append(Parameter(localctx.v2.v.id))
                        self.state = 350
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)



                self.state = 353
                self.match(SetlXgrammarParser.T__33)
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

    class ImplicationContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1, enableIgnore=None):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.enableIgnore = None
            self.i = None
            self._disjunction = None # DisjunctionContext
            self._implication = None # ImplicationContext
            self.enableIgnore = enableIgnore

        def disjunction(self):
            return self.getTypedRuleContext(SetlXgrammarParser.DisjunctionContext,0)


        def implication(self):
            return self.getTypedRuleContext(SetlXgrammarParser.ImplicationContext,0)


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
        self.enterRule(localctx, 22, self.RULE_implication)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 356
            localctx._disjunction = self.disjunction(localctx.enableIgnore)
            localctx.i = localctx._disjunction.d
            self.state = 362
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==SetlXgrammarParser.T__38:
                self.state = 358
                self.match(SetlXgrammarParser.T__38)
                self.state = 359
                localctx._implication = self.implication(localctx.enableIgnore)
                localctx.i = Implication(localctx.i, localctx._implication.i) 


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

        def conjunction(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SetlXgrammarParser.ConjunctionContext)
            else:
                return self.getTypedRuleContext(SetlXgrammarParser.ConjunctionContext,i)


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
        self.enterRule(localctx, 24, self.RULE_disjunction)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 364
            localctx._conjunction = self.conjunction(localctx.enableIgnore)
            localctx.d = localctx._conjunction.c
            self.state = 372
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==SetlXgrammarParser.T__39:
                self.state = 366
                self.match(SetlXgrammarParser.T__39)
                self.state = 367
                localctx._conjunction = self.conjunction(localctx.enableIgnore)
                localctx.d = Disjunction(localctx.d, localctx._conjunction.c) 
                self.state = 374
                self._errHandler.sync(self)
                _la = self._input.LA(1)

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

        def comparison(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SetlXgrammarParser.ComparisonContext)
            else:
                return self.getTypedRuleContext(SetlXgrammarParser.ComparisonContext,i)


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
        self.enterRule(localctx, 26, self.RULE_conjunction)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 375
            localctx._comparison = self.comparison(localctx.enableIgnore)
            localctx.c = localctx._comparison.c
            self.state = 383
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==SetlXgrammarParser.T__40:
                self.state = 377
                self.match(SetlXgrammarParser.T__40)
                self.state = 378
                localctx._comparison = self.comparison(localctx.enableIgnore)
                localctx.c = Conjunction(localctx.c, localctx._comparison.c) 
                self.state = 385
                self._errHandler.sync(self)
                _la = self._input.LA(1)

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
        self.enterRule(localctx, 28, self.RULE_comparison)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 386
            localctx.s1 = self.setlxSum(localctx.enableIgnore)
            localctx.c = localctx.s1.s 
            self.state = 420
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [SetlXgrammarParser.T__41]:
                self.state = 388
                self.match(SetlXgrammarParser.T__41)
                self.state = 389
                localctx.s2 = self.setlxSum(localctx.enableIgnore)
                localctx.c = Equal(localctx.s1.s,localctx.s2.s) 
                pass
            elif token in [SetlXgrammarParser.T__42]:
                self.state = 392
                self.match(SetlXgrammarParser.T__42)
                self.state = 393
                localctx.s2 = self.setlxSum(localctx.enableIgnore)
                localctx.c = NotEqual(localctx.s1.s,localctx.s2.s) 
                pass
            elif token in [SetlXgrammarParser.T__43]:
                self.state = 396
                self.match(SetlXgrammarParser.T__43)
                self.state = 397
                localctx.s2 = self.setlxSum(localctx.enableIgnore)
                localctx.c = LessThan(localctx.s1.s,localctx.s2.s) 
                pass
            elif token in [SetlXgrammarParser.T__44]:
                self.state = 400
                self.match(SetlXgrammarParser.T__44)
                self.state = 401
                localctx.s2 = self.setlxSum(localctx.enableIgnore)
                localctx.c = LessOrEqual(localctx.s1.s,localctx.s2.s) 
                pass
            elif token in [SetlXgrammarParser.T__45]:
                self.state = 404
                self.match(SetlXgrammarParser.T__45)
                self.state = 405
                localctx.s2 = self.setlxSum(localctx.enableIgnore)
                localctx.c = GreaterThan(localctx.s1.s,localctx.s2.s) 
                pass
            elif token in [SetlXgrammarParser.T__46]:
                self.state = 408
                self.match(SetlXgrammarParser.T__46)
                self.state = 409
                localctx.s2 = self.setlxSum(localctx.enableIgnore)
                localctx.c = GreaterOrEqual(localctx.s1.s,localctx.s2.s) 
                pass
            elif token in [SetlXgrammarParser.T__47]:
                self.state = 412
                self.match(SetlXgrammarParser.T__47)
                self.state = 413
                localctx.s2 = self.setlxSum(localctx.enableIgnore)
                localctx.c = In(localctx.s1.s,localctx.s2.s) 
                pass
            elif token in [SetlXgrammarParser.T__48]:
                self.state = 416
                self.match(SetlXgrammarParser.T__48)
                self.state = 417
                localctx.s2 = self.setlxSum(localctx.enableIgnore)
                localctx.c = NotIn(localctx.s1.s,localctx.s2.s) 
                pass
            elif token in [SetlXgrammarParser.T__2, SetlXgrammarParser.T__4, SetlXgrammarParser.T__8, SetlXgrammarParser.T__11, SetlXgrammarParser.T__14, SetlXgrammarParser.T__23, SetlXgrammarParser.T__33, SetlXgrammarParser.T__35, SetlXgrammarParser.T__36, SetlXgrammarParser.T__38, SetlXgrammarParser.T__39, SetlXgrammarParser.T__40, SetlXgrammarParser.RANGE_SIGN]:
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
        self.enterRule(localctx, 30, self.RULE_setlxSum)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 422
            localctx.p1 = self.product(localctx.enableIgnore)
            localctx.s = localctx.p1.p
            self.state = 434
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==SetlXgrammarParser.T__49 or _la==SetlXgrammarParser.T__50:
                self.state = 432
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [SetlXgrammarParser.T__49]:
                    self.state = 424
                    self.match(SetlXgrammarParser.T__49)
                    self.state = 425
                    localctx.p2 = self.product(localctx.enableIgnore)
                    localctx.s = Sum(localctx.p1.p,localctx.p2.p) 
                    pass
                elif token in [SetlXgrammarParser.T__50]:
                    self.state = 428
                    self.match(SetlXgrammarParser.T__50)
                    self.state = 429
                    localctx.p2 = self.product(localctx.enableIgnore)
                    localctx.s = Difference(localctx.p1.p,localctx.p2.p) 
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 436
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
            self.r2 = None # SetlxReduceContext
            self.enableIgnore = enableIgnore

        def setlxReduce(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SetlXgrammarParser.SetlxReduceContext)
            else:
                return self.getTypedRuleContext(SetlXgrammarParser.SetlxReduceContext,i)


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
        self.enterRule(localctx, 32, self.RULE_product)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 437
            localctx.r1 = self.setlxReduce(localctx.enableIgnore)
            localctx.p = localctx.r1.r
            self.state = 461
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << SetlXgrammarParser.T__51) | (1 << SetlXgrammarParser.T__52) | (1 << SetlXgrammarParser.T__53) | (1 << SetlXgrammarParser.T__54) | (1 << SetlXgrammarParser.T__55))) != 0):
                self.state = 459
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [SetlXgrammarParser.T__51]:
                    self.state = 439
                    self.match(SetlXgrammarParser.T__51)
                    self.state = 440
                    localctx.r2 = self.setlxReduce(localctx.enableIgnore)
                    localctx.p = Product(localctx.p,localctx.r2.r) 
                    pass
                elif token in [SetlXgrammarParser.T__52]:
                    self.state = 443
                    self.match(SetlXgrammarParser.T__52)
                    self.state = 444
                    localctx.r2 = self.setlxReduce(localctx.enableIgnore)
                    localctx.p = Quotient(localctx.p,localctx.r2.r) 
                    pass
                elif token in [SetlXgrammarParser.T__53]:
                    self.state = 447
                    self.match(SetlXgrammarParser.T__53)
                    self.state = 448
                    localctx.r2 = self.setlxReduce(localctx.enableIgnore)
                    localctx.p = IntegerDivision(localctx.p,localctx.r2.r) 
                    pass
                elif token in [SetlXgrammarParser.T__54]:
                    self.state = 451
                    self.match(SetlXgrammarParser.T__54)
                    self.state = 452
                    localctx.r2 = self.setlxReduce(localctx.enableIgnore)
                    localctx.p = Modulo(localctx.p,localctx.r2.r) 
                    pass
                elif token in [SetlXgrammarParser.T__55]:
                    self.state = 455
                    self.match(SetlXgrammarParser.T__55)
                    self.state = 456
                    localctx.r2 = self.setlxReduce(localctx.enableIgnore)
                    localctx.p = CartesianProduct(localctx.p,localctx.r2.r) 
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 463
                self._errHandler.sync(self)
                _la = self._input.LA(1)

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
            self.p2 = None # PrefixOperationContext
            self.enableIgnore = enableIgnore

        def prefixOperation(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SetlXgrammarParser.PrefixOperationContext)
            else:
                return self.getTypedRuleContext(SetlXgrammarParser.PrefixOperationContext,i)


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
        self.enterRule(localctx, 34, self.RULE_setlxReduce)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 464
            localctx.p1 = self.prefixOperation(localctx.enableIgnore)
            localctx.r = localctx.p1.p
            self.state = 476
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==SetlXgrammarParser.T__56 or _la==SetlXgrammarParser.T__57:
                self.state = 474
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [SetlXgrammarParser.T__56]:
                    self.state = 466
                    self.match(SetlXgrammarParser.T__56)
                    self.state = 467
                    localctx.p2 = self.prefixOperation(localctx.enableIgnore)
                    localctx.r = SumOfMembersBinary(localctx.r,localctx.p2.p) 
                    pass
                elif token in [SetlXgrammarParser.T__57]:
                    self.state = 470
                    self.match(SetlXgrammarParser.T__57)
                    self.state = 471
                    localctx.p2 = self.prefixOperation(localctx.enableIgnore)
                    localctx.r = ProductOfMembersBinary(localctx.r,localctx.p2.p) 
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 478
                self._errHandler.sync(self)
                _la = self._input.LA(1)

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
            self._prefixOperation = None # PrefixOperationContext
            self.enableIgnore = enableIgnore

        def factor(self):
            return self.getTypedRuleContext(SetlXgrammarParser.FactorContext,0)


        def prefixOperation(self):
            return self.getTypedRuleContext(SetlXgrammarParser.PrefixOperationContext,0)


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
        self.enterRule(localctx, 36, self.RULE_prefixOperation)
        self._la = 0 # Token type
        try:
            self.state = 503
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,32,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 479
                localctx._factor = self.factor(localctx.enableIgnore)
                localctx.p = localctx._factor.f
                self.state = 485
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==SetlXgrammarParser.T__58:
                    self.state = 481
                    self.match(SetlXgrammarParser.T__58)
                    self.state = 482
                    localctx._prefixOperation = self.prefixOperation(localctx.enableIgnore)
                    localctx.p = Power(localctx.p,localctx._prefixOperation.p) 


                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 487
                self.match(SetlXgrammarParser.T__56)
                self.state = 488
                localctx._prefixOperation = self.prefixOperation(localctx.enableIgnore)
                localctx.p = SumOfMembers(localctx._prefixOperation.p) 
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 491
                self.match(SetlXgrammarParser.T__57)
                self.state = 492
                localctx._prefixOperation = self.prefixOperation(localctx.enableIgnore)
                localctx.p = ProductOfMembers(localctx._prefixOperation.p) 
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 495
                self.match(SetlXgrammarParser.T__59)
                self.state = 496
                localctx._prefixOperation = self.prefixOperation(localctx.enableIgnore)
                localctx.p = Cardinality(localctx._prefixOperation.p) 
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 499
                self.match(SetlXgrammarParser.T__50)
                self.state = 500
                localctx._prefixOperation = self.prefixOperation(localctx.enableIgnore)
                localctx.p = Minus(localctx._prefixOperation.p)
                pass


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
            self._factor = None # FactorContext
            self._iteratorChain = None # IteratorChainContext
            self._condition = None # ConditionContext
            self._exprContent = None # ExprContentContext
            self._procedure = None # ProcedureContext
            self._variable = None # VariableContext
            self._call = None # CallContext
            self._value = None # ValueContext
            self.enableIgnore = enableIgnore

        def factor(self):
            return self.getTypedRuleContext(SetlXgrammarParser.FactorContext,0)


        def iteratorChain(self):
            return self.getTypedRuleContext(SetlXgrammarParser.IteratorChainContext,0)


        def condition(self):
            return self.getTypedRuleContext(SetlXgrammarParser.ConditionContext,0)


        def exprContent(self):
            return self.getTypedRuleContext(SetlXgrammarParser.ExprContentContext,0)


        def procedure(self):
            return self.getTypedRuleContext(SetlXgrammarParser.ProcedureContext,0)


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
        self.enterRule(localctx, 38, self.RULE_factor)
        self._la = 0 # Token type
        try:
            self.state = 560
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,38,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 505
                self.match(SetlXgrammarParser.T__60)
                self.state = 506
                localctx._factor = self.factor(localctx.enableIgnore)
                localctx.f = Not(localctx._factor.f) 
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 509
                self.match(SetlXgrammarParser.T__61)
                self.state = 510
                self.match(SetlXgrammarParser.T__1)
                self.state = 511
                localctx._iteratorChain = self.iteratorChain(localctx.enableIgnore)
                self.state = 512
                self.match(SetlXgrammarParser.T__11)
                self.state = 513
                localctx._condition = self.condition()
                self.state = 514
                self.match(SetlXgrammarParser.T__2)
                localctx.f = Forall(localctx._iteratorChain.ic,localctx._condition.cnd)
                		
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 517
                self.match(SetlXgrammarParser.T__62)
                self.state = 518
                self.match(SetlXgrammarParser.T__1)
                self.state = 519
                localctx._iteratorChain = self.iteratorChain(localctx.enableIgnore)
                self.state = 520
                self.match(SetlXgrammarParser.T__11)
                self.state = 521
                localctx._condition = self.condition()
                self.state = 522
                self.match(SetlXgrammarParser.T__2)
                localctx.f = Exists(localctx._iteratorChain.ic,localctx._condition.cnd)
                		
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 536
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [SetlXgrammarParser.T__1]:
                    self.state = 525
                    self.match(SetlXgrammarParser.T__1)
                    self.state = 526
                    localctx._exprContent = self.exprContent(localctx.enableIgnore)
                    self.state = 527
                    self.match(SetlXgrammarParser.T__2)
                    localctx.f = localctx._exprContent.ex 
                    pass
                elif token in [SetlXgrammarParser.T__63, SetlXgrammarParser.T__64, SetlXgrammarParser.T__65]:
                    self.state = 530
                    localctx._procedure = self.procedure()
                    localctx.f = localctx._procedure.pd 
                    pass
                elif token in [SetlXgrammarParser.ID]:
                    self.state = 533
                    localctx._variable = self.variable()
                    localctx.f = localctx._variable.v 
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 547
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << SetlXgrammarParser.T__1) | (1 << SetlXgrammarParser.T__31) | (1 << SetlXgrammarParser.T__32))) != 0):
                    self.state = 545
                    self._errHandler.sync(self)
                    token = self._input.LA(1)
                    if token in [SetlXgrammarParser.T__31]:
                        self.state = 538
                        self.match(SetlXgrammarParser.T__31)
                        self.state = 539
                        localctx._variable = self.variable()
                        localctx.f = MemberAccess(localctx.f,localctx._variable.v) 
                        pass
                    elif token in [SetlXgrammarParser.T__1, SetlXgrammarParser.T__32]:
                        self.state = 542
                        localctx._call = self.call(localctx.enableIgnore)

                        localctx._call.c.callable = localctx.f
                        localctx.f = localctx._call.c
                                
                        pass
                    else:
                        raise NoViableAltException(self)

                    self.state = 549
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 552
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==SetlXgrammarParser.T__60:
                    self.state = 550
                    self.match(SetlXgrammarParser.T__60)
                    localctx.f = Factorial(localctx.f) 


                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 554
                localctx._value = self.value(localctx.enableIgnore)
                localctx.f = localctx._value.v 
                self.state = 558
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==SetlXgrammarParser.T__60:
                    self.state = 556
                    self.match(SetlXgrammarParser.T__60)
                    localctx.f = Factorial(localctx._value.v) 


                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ProcedureContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.pd = None
            self._procedureParameters = None # ProcedureParametersContext
            self._block = None # BlockContext

        def procedureParameters(self):
            return self.getTypedRuleContext(SetlXgrammarParser.ProcedureParametersContext,0)


        def block(self):
            return self.getTypedRuleContext(SetlXgrammarParser.BlockContext,0)


        def getRuleIndex(self):
            return SetlXgrammarParser.RULE_procedure

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProcedure" ):
                listener.enterProcedure(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProcedure" ):
                listener.exitProcedure(self)




    def procedure(self):

        localctx = SetlXgrammarParser.ProcedureContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_procedure)
        try:
            self.state = 589
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [SetlXgrammarParser.T__63]:
                self.enterOuterAlt(localctx, 1)
                self.state = 562
                self.match(SetlXgrammarParser.T__63)
                self.state = 563
                self.match(SetlXgrammarParser.T__1)
                self.state = 564
                localctx._procedureParameters = self.procedureParameters(True)
                self.state = 565
                self.match(SetlXgrammarParser.T__2)
                self.state = 566
                self.match(SetlXgrammarParser.T__3)
                self.state = 567
                localctx._block = self.block()
                self.state = 568
                self.match(SetlXgrammarParser.T__4)
                localctx.pd = Procedure(localctx._procedureParameters.paramList, localctx._block.blk) 
                		
                pass
            elif token in [SetlXgrammarParser.T__64]:
                self.enterOuterAlt(localctx, 2)
                self.state = 571
                self.match(SetlXgrammarParser.T__64)
                self.state = 572
                self.match(SetlXgrammarParser.T__1)
                self.state = 573
                localctx._procedureParameters = self.procedureParameters(False)
                self.state = 574
                self.match(SetlXgrammarParser.T__2)
                self.state = 575
                self.match(SetlXgrammarParser.T__3)
                self.state = 576
                localctx._block = self.block()
                self.state = 577
                self.match(SetlXgrammarParser.T__4)
                localctx.pd = CachedProcedure(localctx._procedureParameters.paramList, localctx._block.blk) 
                		
                pass
            elif token in [SetlXgrammarParser.T__65]:
                self.enterOuterAlt(localctx, 3)
                self.state = 580
                self.match(SetlXgrammarParser.T__65)
                self.state = 581
                self.match(SetlXgrammarParser.T__1)
                self.state = 582
                localctx._procedureParameters = self.procedureParameters(True)
                self.state = 583
                self.match(SetlXgrammarParser.T__2)
                self.state = 584
                self.match(SetlXgrammarParser.T__3)
                self.state = 585
                localctx._block = self.block()
                self.state = 586
                self.match(SetlXgrammarParser.T__4)
                localctx.pd = Closure(localctx._procedureParameters.paramList, localctx._block.blk) 
                		
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

    class ProcedureParametersContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1, enableRw=None):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.enableRw = None
            self.paramList = None
            self.pp1 = None # ProcedureParameterContext
            self.pp2 = None # ProcedureParameterContext
            self.dp1 = None # ProcedureDefaultParameterContext
            self.dp2 = None # ProcedureDefaultParameterContext
            self.dp3 = None # ProcedureDefaultParameterContext
            self.enableRw = enableRw

        def procedureParameter(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SetlXgrammarParser.ProcedureParameterContext)
            else:
                return self.getTypedRuleContext(SetlXgrammarParser.ProcedureParameterContext,i)


        def procedureDefaultParameter(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SetlXgrammarParser.ProcedureDefaultParameterContext)
            else:
                return self.getTypedRuleContext(SetlXgrammarParser.ProcedureDefaultParameterContext,i)


        def getRuleIndex(self):
            return SetlXgrammarParser.RULE_procedureParameters

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProcedureParameters" ):
                listener.enterProcedureParameters(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProcedureParameters" ):
                listener.exitProcedureParameters(self)




    def procedureParameters(self, enableRw):

        localctx = SetlXgrammarParser.ProcedureParametersContext(self, self._ctx, self.state, enableRw)
        self.enterRule(localctx, 42, self.RULE_procedureParameters)

        localctx.paramList = []
            
        self._la = 0 # Token type
        try:
            self.state = 623
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,43,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 591
                localctx.pp1 = self.procedureParameter(localctx.enableRw)
                localctx.paramList.append(localctx.pp1.param) 
                self.state = 599
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,40,self._ctx)
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1:
                        self.state = 593
                        self.match(SetlXgrammarParser.T__23)
                        self.state = 594
                        localctx.pp2 = self.procedureParameter(localctx.enableRw)
                        localctx.paramList.append(localctx.pp2.param)  
                    self.state = 601
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,40,self._ctx)

                self.state = 608
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==SetlXgrammarParser.T__23:
                    self.state = 602
                    self.match(SetlXgrammarParser.T__23)
                    self.state = 603
                    localctx.dp1 = self.procedureDefaultParameter()
                    localctx.paramList.append(localctx.dp1.param) 
                    self.state = 610
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 611
                localctx.dp2 = self.procedureDefaultParameter()
                localctx.paramList.append(localctx.dp2.param) 
                self.state = 619
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==SetlXgrammarParser.T__23:
                    self.state = 613
                    self.match(SetlXgrammarParser.T__23)
                    self.state = 614
                    localctx.dp3 = self.procedureDefaultParameter()
                    localctx.paramList.append(localctx.dp3.param) 
                    self.state = 621
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)

                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ProcedureParameterContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1, enableRw=None):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.enableRw = None
            self.param = None
            self._assignableVariable = None # AssignableVariableContext
            self._variable = None # VariableContext
            self.enableRw = enableRw

        def assignableVariable(self):
            return self.getTypedRuleContext(SetlXgrammarParser.AssignableVariableContext,0)


        def variable(self):
            return self.getTypedRuleContext(SetlXgrammarParser.VariableContext,0)


        def getRuleIndex(self):
            return SetlXgrammarParser.RULE_procedureParameter

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProcedureParameter" ):
                listener.enterProcedureParameter(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProcedureParameter" ):
                listener.exitProcedureParameter(self)




    def procedureParameter(self, enableRw):

        localctx = SetlXgrammarParser.ProcedureParameterContext(self, self._ctx, self.state, enableRw)
        self.enterRule(localctx, 44, self.RULE_procedureParameter)
        try:
            self.state = 633
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,44,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 625
                if not localctx.enableRw:
                    from antlr4.error.Errors import FailedPredicateException
                    raise FailedPredicateException(self, "$enableRw")
                self.state = 626
                self.match(SetlXgrammarParser.T__66)
                self.state = 627
                localctx._assignableVariable = self.assignableVariable()
                localctx.param = ReadWriteParameter(localctx._assignableVariable.v.id) 
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 630
                localctx._variable = self.variable()
                localctx.param = Parameter(localctx._variable.v.id) 
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ProcedureDefaultParameterContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.param = None
            self._assignableVariable = None # AssignableVariableContext
            self._expr = None # ExprContext

        def assignableVariable(self):
            return self.getTypedRuleContext(SetlXgrammarParser.AssignableVariableContext,0)


        def expr(self):
            return self.getTypedRuleContext(SetlXgrammarParser.ExprContext,0)


        def getRuleIndex(self):
            return SetlXgrammarParser.RULE_procedureDefaultParameter

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProcedureDefaultParameter" ):
                listener.enterProcedureDefaultParameter(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProcedureDefaultParameter" ):
                listener.exitProcedureDefaultParameter(self)




    def procedureDefaultParameter(self):

        localctx = SetlXgrammarParser.ProcedureDefaultParameterContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_procedureDefaultParameter)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 635
            localctx._assignableVariable = self.assignableVariable()
            self.state = 636
            self.match(SetlXgrammarParser.T__30)
            self.state = 637
            localctx._expr = self.expr(False)
            localctx.param = Parameter(localctx._assignableVariable.v.id, localctx._expr.ex) 
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
            self._collectionAccessParams = None # CollectionAccessParamsContext
            self.enableIgnore = enableIgnore

        def callParameters(self):
            return self.getTypedRuleContext(SetlXgrammarParser.CallParametersContext,0)


        def collectionAccessParams(self):
            return self.getTypedRuleContext(SetlXgrammarParser.CollectionAccessParamsContext,0)


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
        self.enterRule(localctx, 48, self.RULE_call)
        try:
            self.state = 650
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [SetlXgrammarParser.T__1]:
                self.enterOuterAlt(localctx, 1)
                self.state = 640
                self.match(SetlXgrammarParser.T__1)
                self.state = 641
                localctx._callParameters = self.callParameters(localctx.enableIgnore)
                self.state = 642
                self.match(SetlXgrammarParser.T__2)
                localctx.c = FunctionCall(localctx._callParameters.params, localctx._callParameters.ex) 
                		
                pass
            elif token in [SetlXgrammarParser.T__32]:
                self.enterOuterAlt(localctx, 2)
                self.state = 645
                self.match(SetlXgrammarParser.T__32)
                self.state = 646
                localctx._collectionAccessParams = self.collectionAccessParams(localctx.enableIgnore)
                self.state = 647
                self.match(SetlXgrammarParser.T__33)
                localctx.c = CollectionAccess(localctx._collectionAccessParams.p)
                		
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

    class CollectionAccessParamsContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1, enableIgnore=None):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.enableIgnore = None
            self.p = None
            self.e1 = None # ExprContext
            self.e2 = None # ExprContext
            self.e3 = None # ExprContext
            self._expr = None # ExprContext
            self.enableIgnore = enableIgnore

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SetlXgrammarParser.ExprContext)
            else:
                return self.getTypedRuleContext(SetlXgrammarParser.ExprContext,i)


        def RANGE_SIGN(self):
            return self.getToken(SetlXgrammarParser.RANGE_SIGN, 0)

        def getRuleIndex(self):
            return SetlXgrammarParser.RULE_collectionAccessParams

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCollectionAccessParams" ):
                listener.enterCollectionAccessParams(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCollectionAccessParams" ):
                listener.exitCollectionAccessParams(self)




    def collectionAccessParams(self, enableIgnore):

        localctx = SetlXgrammarParser.CollectionAccessParamsContext(self, self._ctx, self.state, enableIgnore)
        self.enterRule(localctx, 50, self.RULE_collectionAccessParams)

        params = []
            
        self._la = 0 # Token type
        try:
            self.state = 677
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,49,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 652
                localctx.e1 = self.expr(localctx.enableIgnore)
                self.state = 671
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [SetlXgrammarParser.RANGE_SIGN]:
                    self.state = 653
                    self.match(SetlXgrammarParser.RANGE_SIGN)
                    self.state = 658
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,46,self._ctx)
                    if la_ == 1:
                        self.state = 654
                        localctx.e2 = self.expr(localctx.enableIgnore)
                        localctx.p = ListRange(localctx.e1.ex,localctx.e2.ex) 
                        pass

                    elif la_ == 2:
                        localctx.p = ListRange(localctx.e1.ex,None) 
                        pass


                    pass
                elif token in [SetlXgrammarParser.T__23]:
                    self.state = 664 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    while True:
                        self.state = 660
                        self.match(SetlXgrammarParser.T__23)
                        self.state = 661
                        localctx.e3 = self.expr(False)
                        params.append(localctx.e3.ex) 
                        self.state = 666 
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)
                        if not (_la==SetlXgrammarParser.T__23):
                            break

                    localctx.p = params 
                    pass
                elif token in [SetlXgrammarParser.T__33]:
                    localctx.p = localctx.e1.ex 
                    pass
                else:
                    raise NoViableAltException(self)

                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 673
                self.match(SetlXgrammarParser.RANGE_SIGN)
                self.state = 674
                localctx._expr = self.expr(localctx.enableIgnore)
                localctx.p = ListRange(None,localctx._expr.ex) 
                pass


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
        self.enterRule(localctx, 52, self.RULE_callParameters)

        localctx.params = []
        localctx.ex = None
            
        try:
            self.state = 683
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,50,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 679
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
            self._collectionBuilder = None # CollectionBuilderContext
            self._STRING = None # Token
            self._LITERAL = None # Token
            self._atomicValue = None # AtomicValueContext
            self.enableIgnore = enableIgnore

        def collectionBuilder(self):
            return self.getTypedRuleContext(SetlXgrammarParser.CollectionBuilderContext,0)


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
        self.enterRule(localctx, 54, self.RULE_value)

        cb = None
            
        try:
            self.state = 711
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,53,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 685
                self.match(SetlXgrammarParser.T__32)
                self.state = 689
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,51,self._ctx)
                if la_ == 1:
                    self.state = 686
                    localctx._collectionBuilder = self.collectionBuilder(localctx.enableIgnore)
                    cb = localctx._collectionBuilder.cb; 


                self.state = 691
                self.match(SetlXgrammarParser.T__33)
                localctx.v = SetlXList(cb) 
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 693
                self.match(SetlXgrammarParser.T__3)
                self.state = 697
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,52,self._ctx)
                if la_ == 1:
                    self.state = 694
                    localctx._collectionBuilder = self.collectionBuilder(localctx.enableIgnore)
                    cb = localctx._collectionBuilder.cb; 


                self.state = 699
                self.match(SetlXgrammarParser.T__4)
                localctx.v = SetListConstructor(cb) 
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 701
                localctx._STRING = self.match(SetlXgrammarParser.STRING)
                localctx.v = SetlXString((None if localctx._STRING is None else localctx._STRING.text)) 
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 703
                localctx._LITERAL = self.match(SetlXgrammarParser.LITERAL)
                localctx.v = SetlXLiteral((None if localctx._LITERAL is None else localctx._LITERAL.text)) 
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 705
                localctx._atomicValue = self.atomicValue()
                localctx.v = localctx._atomicValue.av 
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 708
                if not localctx.enableIgnore:
                    from antlr4.error.Errors import FailedPredicateException
                    raise FailedPredicateException(self, "$enableIgnore")
                self.state = 709
                self.match(SetlXgrammarParser.T__34)
                localctx.v = VariableIgnore() 
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class CollectionBuilderContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1, enableIgnore=None):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.enableIgnore = None
            self.cb = None
            self.e1 = None # ExprContext
            self.e2 = None # ExprContext
            self.e3 = None # ExprContext
            self.e4 = None # ExprContext
            self._iteratorChain = None # IteratorChainContext
            self.c1 = None # ConditionContext
            self.enableIgnore = enableIgnore

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SetlXgrammarParser.ExprContext)
            else:
                return self.getTypedRuleContext(SetlXgrammarParser.ExprContext,i)


        def RANGE_SIGN(self):
            return self.getToken(SetlXgrammarParser.RANGE_SIGN, 0)

        def iteratorChain(self):
            return self.getTypedRuleContext(SetlXgrammarParser.IteratorChainContext,0)


        def condition(self):
            return self.getTypedRuleContext(SetlXgrammarParser.ConditionContext,0)


        def getRuleIndex(self):
            return SetlXgrammarParser.RULE_collectionBuilder

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCollectionBuilder" ):
                listener.enterCollectionBuilder(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCollectionBuilder" ):
                listener.exitCollectionBuilder(self)




    def collectionBuilder(self, enableIgnore):

        localctx = SetlXgrammarParser.CollectionBuilderContext(self, self._ctx, self.state, enableIgnore)
        self.enterRule(localctx, 56, self.RULE_collectionBuilder)

        exprs = []
            
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 713
            localctx.e1 = self.expr(localctx.enableIgnore)
            self.state = 760
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [SetlXgrammarParser.T__23]:
                self.state = 714
                self.match(SetlXgrammarParser.T__23)
                self.state = 715
                localctx.e2 = self.expr(localctx.enableIgnore)
                self.state = 737
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [SetlXgrammarParser.RANGE_SIGN]:
                    self.state = 716
                    self.match(SetlXgrammarParser.RANGE_SIGN)
                    self.state = 717
                    localctx.e3 = self.expr(localctx.enableIgnore)
                    localctx.cb = Range(localctx.e1.ex, localctx.e2.ex, localctx.e3.ex) 
                    pass
                elif token in [SetlXgrammarParser.T__4, SetlXgrammarParser.T__11, SetlXgrammarParser.T__23, SetlXgrammarParser.T__33]:
                    exprs.append(localctx.e1.ex); exprs.append(localctx.e2.ex) 
                    self.state = 727
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    while _la==SetlXgrammarParser.T__23:
                        self.state = 721
                        self.match(SetlXgrammarParser.T__23)
                        self.state = 722
                        localctx.e3 = self.expr(localctx.enableIgnore)
                        exprs.append(localctx.e3.ex) 
                        self.state = 729
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)

                    self.state = 735
                    self._errHandler.sync(self)
                    token = self._input.LA(1)
                    if token in [SetlXgrammarParser.T__11]:
                        self.state = 730
                        self.match(SetlXgrammarParser.T__11)
                        self.state = 731
                        localctx.e4 = self.expr(False)
                        localctx.cb = ExplicitListWithRest(exprs, localctx.e4.ex) 
                        pass
                    elif token in [SetlXgrammarParser.T__4, SetlXgrammarParser.T__33]:
                        localctx.cb = ExplicitList(exprs)         
                        pass
                    else:
                        raise NoViableAltException(self)

                    pass
                else:
                    raise NoViableAltException(self)

                pass
            elif token in [SetlXgrammarParser.RANGE_SIGN]:
                self.state = 739
                self.match(SetlXgrammarParser.RANGE_SIGN)
                self.state = 740
                localctx.e3 = self.expr(localctx.enableIgnore)
                localctx.cb = Range(localctx.e1.ex, None, localctx.e3.ex) 
                pass
            elif token in [SetlXgrammarParser.T__4, SetlXgrammarParser.T__11, SetlXgrammarParser.T__33]:
                exprs.append(localctx.e1.ex) 
                self.state = 749
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [SetlXgrammarParser.T__11]:
                    self.state = 744
                    self.match(SetlXgrammarParser.T__11)
                    self.state = 745
                    localctx.e2 = self.expr(False)
                    localctx.cb = ExplicitListWithRest(exprs, localctx.e2.ex) 
                    pass
                elif token in [SetlXgrammarParser.T__4, SetlXgrammarParser.T__33]:
                    localctx.cb = ExplicitList(exprs)         
                    pass
                else:
                    raise NoViableAltException(self)

                pass
            elif token in [SetlXgrammarParser.T__8]:
                self.state = 751
                self.match(SetlXgrammarParser.T__8)
                self.state = 752
                localctx._iteratorChain = self.iteratorChain(localctx.enableIgnore)
                self.state = 758
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [SetlXgrammarParser.T__11]:
                    self.state = 753
                    self.match(SetlXgrammarParser.T__11)
                    self.state = 754
                    localctx.c1 = self.condition()
                    localctx.cb = SetlIteration(localctx.e1.ex, localctx._iteratorChain.ic, localctx.c1.cnd) 
                    pass
                elif token in [SetlXgrammarParser.T__4, SetlXgrammarParser.T__33]:
                    localctx.cb = SetlIteration(localctx.e1.ex, localctx._iteratorChain.ic, None) 
                    pass
                else:
                    raise NoViableAltException(self)

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

    class IteratorChainContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1, enableIgnore=None):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.enableIgnore = None
            self.ic = None
            self.i1 = None # IteratorContext
            self.i2 = None # IteratorContext
            self.enableIgnore = enableIgnore

        def iterator(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SetlXgrammarParser.IteratorContext)
            else:
                return self.getTypedRuleContext(SetlXgrammarParser.IteratorContext,i)


        def getRuleIndex(self):
            return SetlXgrammarParser.RULE_iteratorChain

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIteratorChain" ):
                listener.enterIteratorChain(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIteratorChain" ):
                listener.exitIteratorChain(self)




    def iteratorChain(self, enableIgnore):

        localctx = SetlXgrammarParser.IteratorChainContext(self, self._ctx, self.state, enableIgnore)
        self.enterRule(localctx, 58, self.RULE_iteratorChain)

        localctx.ic = []
            
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 762
            localctx.i1 = self.iterator(localctx.enableIgnore)
            localctx.ic.append(localctx.i1.iter)
            self.state = 770
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==SetlXgrammarParser.T__23:
                self.state = 764
                self.match(SetlXgrammarParser.T__23)
                self.state = 765
                localctx.i2 = self.iterator(localctx.enableIgnore)
                localctx.ic.append(localctx.i2.iter) 
                self.state = 772
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class IteratorContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1, enableIgnore=None):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.enableIgnore = None
            self.iter = None
            self._assignable = None # AssignableContext
            self._expr = None # ExprContext
            self.enableIgnore = enableIgnore

        def assignable(self):
            return self.getTypedRuleContext(SetlXgrammarParser.AssignableContext,0)


        def expr(self):
            return self.getTypedRuleContext(SetlXgrammarParser.ExprContext,0)


        def getRuleIndex(self):
            return SetlXgrammarParser.RULE_iterator

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIterator" ):
                listener.enterIterator(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIterator" ):
                listener.exitIterator(self)




    def iterator(self, enableIgnore):

        localctx = SetlXgrammarParser.IteratorContext(self, self._ctx, self.state, enableIgnore)
        self.enterRule(localctx, 60, self.RULE_iterator)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 773
            localctx._assignable = self.assignable(True)
            self.state = 774
            self.match(SetlXgrammarParser.T__47)
            self.state = 775
            localctx._expr = self.expr(localctx.enableIgnore)
            localctx.iter = SetlIterator(localctx._assignable.a, localctx._expr.ex) 
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
        self.enterRule(localctx, 62, self.RULE_atomicValue)
        try:
            self.state = 788
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [SetlXgrammarParser.NUMBER]:
                self.enterOuterAlt(localctx, 1)
                self.state = 778
                localctx._NUMBER = self.match(SetlXgrammarParser.NUMBER)
                localctx.av = SetlXFraction((None if localctx._NUMBER is None else localctx._NUMBER.text)) 
                pass
            elif token in [SetlXgrammarParser.DOUBLE]:
                self.enterOuterAlt(localctx, 2)
                self.state = 780
                localctx._DOUBLE = self.match(SetlXgrammarParser.DOUBLE)
                localctx.av = float((None if localctx._DOUBLE is None else localctx._DOUBLE.text)) 
                pass
            elif token in [SetlXgrammarParser.T__67]:
                self.enterOuterAlt(localctx, 3)
                self.state = 782
                self.match(SetlXgrammarParser.T__67)
                localctx.av = SetlXOm() 
                pass
            elif token in [SetlXgrammarParser.T__68]:
                self.enterOuterAlt(localctx, 4)
                self.state = 784
                self.match(SetlXgrammarParser.T__68)
                localctx.av = SetlXTrue() 
                pass
            elif token in [SetlXgrammarParser.T__69]:
                self.enterOuterAlt(localctx, 5)
                self.state = 786
                self.match(SetlXgrammarParser.T__69)
                localctx.av = SetlXFalse() 
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
        self.enterRule(localctx, 64, self.RULE_variable)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 790
            localctx._ID = self.match(SetlXgrammarParser.ID)
            localctx.v = Variable((None if localctx._ID is None else localctx._ID.text)) 
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ConditionContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.cnd = None
            self._expr = None # ExprContext

        def expr(self):
            return self.getTypedRuleContext(SetlXgrammarParser.ExprContext,0)


        def getRuleIndex(self):
            return SetlXgrammarParser.RULE_condition

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCondition" ):
                listener.enterCondition(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCondition" ):
                listener.exitCondition(self)




    def condition(self):

        localctx = SetlXgrammarParser.ConditionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 66, self.RULE_condition)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 793
            localctx._expr = self.expr(False)
            localctx.cnd = Condition(localctx._expr.ex) 
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
        self.enterRule(localctx, 68, self.RULE_assignmentList)

        localctx.al = []
            
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 796
            localctx.a1 = self.assignable(True)
            localctx.al.append(localctx.a1.a) 
            self.state = 804
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==SetlXgrammarParser.T__23:
                self.state = 798
                self.match(SetlXgrammarParser.T__23)
                self.state = 799
                localctx.a2 = self.assignable(True)
                localctx.al.append(localctx.a2.a) 
                self.state = 806
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
        self._predicates[4] = self.assignable_sempred
        self._predicates[22] = self.procedureParameter_sempred
        self._predicates[27] = self.value_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def assignable_sempred(self, localctx:AssignableContext, predIndex:int):
            if predIndex == 0:
                return localctx.enableIgnore
         

    def procedureParameter_sempred(self, localctx:ProcedureParameterContext, predIndex:int):
            if predIndex == 1:
                return localctx.enableRw
         

    def value_sempred(self, localctx:ValueContext, predIndex:int):
            if predIndex == 2:
                return localctx.enableIgnore
         




