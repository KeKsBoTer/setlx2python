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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3>")
        buf.write("\u027e\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31")
        buf.write("\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36")
        buf.write("\4\37\t\37\4 \t \4!\t!\4\"\t\"\3\2\3\2\3\2\7\2H\n\2\f")
        buf.write("\2\16\2K\13\2\3\2\3\2\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3")
        buf.write("\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\7\3a\n\3\f\3")
        buf.write("\16\3d\13\3\3\3\3\3\3\3\3\3\3\3\3\3\5\3l\n\3\3\3\3\3\3")
        buf.write("\3\3\3\3\3\3\3\3\3\3\3\3\3\5\3w\n\3\3\3\3\3\3\3\3\3\3")
        buf.write("\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3")
        buf.write("\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3")
        buf.write("\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\5\3\u00a3\n")
        buf.write("\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3")
        buf.write("\3\3\5\3\u00b3\n\3\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4")
        buf.write("\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3")
        buf.write("\4\3\4\3\4\5\4\u00ce\n\4\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3")
        buf.write("\5\3\5\3\5\3\5\3\5\3\5\5\5\u00dd\n\5\5\5\u00df\n\5\3\6")
        buf.write("\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\7\6\u00ec\n\6")
        buf.write("\f\6\16\6\u00ef\13\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\5")
        buf.write("\6\u00f9\n\6\3\7\3\7\3\7\3\b\3\b\3\b\3\t\3\t\3\t\3\t\3")
        buf.write("\t\3\t\7\t\u0107\n\t\f\t\16\t\u010a\13\t\3\n\3\n\3\n\3")
        buf.write("\13\3\13\3\13\3\f\3\f\3\f\3\f\3\f\3\f\7\f\u0118\n\f\f")
        buf.write("\f\16\f\u011b\13\f\3\r\3\r\3\r\3\r\3\r\3\r\7\r\u0123\n")
        buf.write("\r\f\r\16\r\u0126\13\r\3\16\3\16\3\16\3\16\3\16\3\16\3")
        buf.write("\16\3\16\3\16\3\16\3\16\3\16\3\16\3\16\3\16\3\16\3\16")
        buf.write("\3\16\3\16\3\16\3\16\3\16\3\16\3\16\3\16\3\16\3\16\3\16")
        buf.write("\3\16\3\16\3\16\3\16\3\16\3\16\5\16\u014a\n\16\3\17\3")
        buf.write("\17\3\17\3\17\3\17\3\17\3\17\3\17\3\17\3\17\7\17\u0156")
        buf.write("\n\17\f\17\16\17\u0159\13\17\3\20\3\20\3\20\3\20\3\20")
        buf.write("\3\20\3\20\3\20\3\20\3\20\3\20\3\20\3\20\3\20\3\20\3\20")
        buf.write("\3\20\3\20\7\20\u016d\n\20\f\20\16\20\u0170\13\20\3\21")
        buf.write("\3\21\3\21\3\22\3\22\3\22\3\22\3\22\3\22\5\22\u017b\n")
        buf.write("\22\3\22\3\22\3\22\3\22\5\22\u0181\n\22\3\23\3\23\3\23")
        buf.write("\3\23\3\23\3\23\3\23\3\23\3\23\3\23\3\23\3\23\3\23\3\23")
        buf.write("\3\23\5\23\u0192\n\23\3\23\3\23\3\23\3\23\3\23\3\23\3")
        buf.write("\23\7\23\u019b\n\23\f\23\16\23\u019e\13\23\3\23\3\23\5")
        buf.write("\23\u01a2\n\23\3\23\3\23\3\23\3\23\5\23\u01a8\n\23\5\23")
        buf.write("\u01aa\n\23\3\24\3\24\3\24\3\24\3\24\3\24\3\24\3\24\3")
        buf.write("\24\3\25\3\25\3\25\3\25\3\25\3\25\7\25\u01bb\n\25\f\25")
        buf.write("\16\25\u01be\13\25\3\25\3\25\3\25\3\25\7\25\u01c4\n\25")
        buf.write("\f\25\16\25\u01c7\13\25\3\25\3\25\3\25\3\25\3\25\3\25")
        buf.write("\7\25\u01cf\n\25\f\25\16\25\u01d2\13\25\3\25\5\25\u01d5")
        buf.write("\n\25\3\26\3\26\3\26\3\27\3\27\3\27\3\27\3\27\3\30\3\30")
        buf.write("\3\30\3\30\3\30\3\30\3\30\3\30\3\30\3\30\5\30\u01e9\n")
        buf.write("\30\3\31\3\31\3\31\3\31\3\31\3\31\5\31\u01f1\n\31\3\31")
        buf.write("\3\31\3\31\3\31\6\31\u01f7\n\31\r\31\16\31\u01f8\3\31")
        buf.write("\3\31\3\31\5\31\u01fe\n\31\3\31\3\31\3\31\3\31\5\31\u0204")
        buf.write("\n\31\3\32\3\32\3\32\3\32\5\32\u020a\n\32\3\33\3\33\3")
        buf.write("\33\3\33\5\33\u0210\n\33\3\33\3\33\3\33\3\33\3\33\3\33")
        buf.write("\3\33\3\33\3\33\3\33\3\33\3\33\5\33\u021e\n\33\3\34\3")
        buf.write("\34\3\34\3\34\3\34\3\34\3\34\3\34\3\34\3\34\3\34\3\34")
        buf.write("\7\34\u022c\n\34\f\34\16\34\u022f\13\34\3\34\3\34\3\34")
        buf.write("\3\34\3\34\5\34\u0236\n\34\5\34\u0238\n\34\3\34\3\34\3")
        buf.write("\34\3\34\3\34\3\34\3\34\3\34\3\34\3\34\5\34\u0244\n\34")
        buf.write("\3\34\3\34\3\34\3\34\3\34\3\34\3\34\5\34\u024d\n\34\5")
        buf.write("\34\u024f\n\34\3\35\3\35\3\35\3\35\3\35\3\35\7\35\u0257")
        buf.write("\n\35\f\35\16\35\u025a\13\35\3\36\3\36\3\36\3\36\3\36")
        buf.write("\3\37\3\37\3\37\3\37\3\37\3\37\3\37\3\37\3\37\3\37\5\37")
        buf.write("\u026b\n\37\3 \3 \3 \3!\3!\3!\3\"\3\"\3\"\3\"\3\"\3\"")
        buf.write("\7\"\u0279\n\"\f\"\16\"\u027c\13\"\3\"\2\2#\2\4\6\b\n")
        buf.write("\f\16\20\22\24\26\30\32\34\36 \"$&(*,.\60\62\64\668:<")
        buf.write(">@B\2\2\2\u02b1\2I\3\2\2\2\4\u00b2\3\2\2\2\6\u00b4\3\2")
        buf.write("\2\2\b\u00de\3\2\2\2\n\u00f8\3\2\2\2\f\u00fa\3\2\2\2\16")
        buf.write("\u00fd\3\2\2\2\20\u0100\3\2\2\2\22\u010b\3\2\2\2\24\u010e")
        buf.write("\3\2\2\2\26\u0111\3\2\2\2\30\u011c\3\2\2\2\32\u0127\3")
        buf.write("\2\2\2\34\u014b\3\2\2\2\36\u015a\3\2\2\2 \u0171\3\2\2")
        buf.write("\2\"\u0180\3\2\2\2$\u01a9\3\2\2\2&\u01ab\3\2\2\2(\u01d4")
        buf.write("\3\2\2\2*\u01d6\3\2\2\2,\u01d9\3\2\2\2.\u01e8\3\2\2\2")
        buf.write("\60\u0203\3\2\2\2\62\u0209\3\2\2\2\64\u021d\3\2\2\2\66")
        buf.write("\u021f\3\2\2\28\u0250\3\2\2\2:\u025b\3\2\2\2<\u026a\3")
        buf.write("\2\2\2>\u026c\3\2\2\2@\u026f\3\2\2\2B\u0272\3\2\2\2DE")
        buf.write("\5\4\3\2EF\b\2\1\2FH\3\2\2\2GD\3\2\2\2HK\3\2\2\2IG\3\2")
        buf.write("\2\2IJ\3\2\2\2JL\3\2\2\2KI\3\2\2\2LM\b\2\1\2M\3\3\2\2")
        buf.write("\2NO\7\3\2\2OP\7\4\2\2PQ\5@!\2QR\7\5\2\2RS\7\6\2\2ST\5")
        buf.write("\2\2\2TU\7\7\2\2Ub\b\3\1\2VW\7\b\2\2WX\7\3\2\2XY\7\4\2")
        buf.write("\2YZ\5@!\2Z[\7\5\2\2[\\\7\6\2\2\\]\5\2\2\2]^\7\7\2\2^")
        buf.write("_\b\3\1\2_a\3\2\2\2`V\3\2\2\2ad\3\2\2\2b`\3\2\2\2bc\3")
        buf.write("\2\2\2ck\3\2\2\2db\3\2\2\2ef\7\b\2\2fg\7\6\2\2gh\5\2\2")
        buf.write("\2hi\7\7\2\2ij\b\3\1\2jl\3\2\2\2ke\3\2\2\2kl\3\2\2\2l")
        buf.write("m\3\2\2\2mn\b\3\1\2n\u00b3\3\2\2\2op\7\t\2\2pq\7\4\2\2")
        buf.write("qv\58\35\2rs\7\n\2\2st\5@!\2tu\b\3\1\2uw\3\2\2\2vr\3\2")
        buf.write("\2\2vw\3\2\2\2wx\3\2\2\2xy\7\5\2\2yz\7\6\2\2z{\5\2\2\2")
        buf.write("{|\7\7\2\2|}\b\3\1\2}\u00b3\3\2\2\2~\177\7\13\2\2\177")
        buf.write("\u0080\7\4\2\2\u0080\u0081\5@!\2\u0081\u0082\7\5\2\2\u0082")
        buf.write("\u0083\7\6\2\2\u0083\u0084\5\2\2\2\u0084\u0085\7\7\2\2")
        buf.write("\u0085\u0086\b\3\1\2\u0086\u00b3\3\2\2\2\u0087\u0088\7")
        buf.write("\f\2\2\u0088\u0089\7\6\2\2\u0089\u008a\5\2\2\2\u008a\u008b")
        buf.write("\7\7\2\2\u008b\u008c\7\13\2\2\u008c\u008d\7\4\2\2\u008d")
        buf.write("\u008e\5@!\2\u008e\u008f\7\5\2\2\u008f\u0090\7\r\2\2\u0090")
        buf.write("\u0091\b\3\1\2\u0091\u00b3\3\2\2\2\u0092\u0093\7\16\2")
        buf.write("\2\u0093\u0094\7\r\2\2\u0094\u00b3\b\3\1\2\u0095\u0096")
        buf.write("\7\17\2\2\u0096\u0097\7\r\2\2\u0097\u00b3\b\3\1\2\u0098")
        buf.write("\u0099\7\20\2\2\u0099\u009a\7\r\2\2\u009a\u00b3\b\3\1")
        buf.write("\2\u009b\u009c\7\21\2\2\u009c\u009d\7\r\2\2\u009d\u00b3")
        buf.write("\b\3\1\2\u009e\u00a2\7\22\2\2\u009f\u00a0\5\16\b\2\u00a0")
        buf.write("\u00a1\b\3\1\2\u00a1\u00a3\3\2\2\2\u00a2\u009f\3\2\2\2")
        buf.write("\u00a2\u00a3\3\2\2\2\u00a3\u00a4\3\2\2\2\u00a4\u00a5\7")
        buf.write("\r\2\2\u00a5\u00b3\b\3\1\2\u00a6\u00a7\5\6\4\2\u00a7\u00a8")
        buf.write("\7\r\2\2\u00a8\u00a9\b\3\1\2\u00a9\u00b3\3\2\2\2\u00aa")
        buf.write("\u00ab\5\b\5\2\u00ab\u00ac\7\r\2\2\u00ac\u00ad\b\3\1\2")
        buf.write("\u00ad\u00b3\3\2\2\2\u00ae\u00af\5\16\b\2\u00af\u00b0")
        buf.write("\7\r\2\2\u00b0\u00b1\b\3\1\2\u00b1\u00b3\3\2\2\2\u00b2")
        buf.write("N\3\2\2\2\u00b2o\3\2\2\2\u00b2~\3\2\2\2\u00b2\u0087\3")
        buf.write("\2\2\2\u00b2\u0092\3\2\2\2\u00b2\u0095\3\2\2\2\u00b2\u0098")
        buf.write("\3\2\2\2\u00b2\u009b\3\2\2\2\u00b2\u009e\3\2\2\2\u00b2")
        buf.write("\u00a6\3\2\2\2\u00b2\u00aa\3\2\2\2\u00b2\u00ae\3\2\2\2")
        buf.write("\u00b3\5\3\2\2\2\u00b4\u00cd\5\n\6\2\u00b5\u00b6\7\23")
        buf.write("\2\2\u00b6\u00b7\5\16\b\2\u00b7\u00b8\b\4\1\2\u00b8\u00ce")
        buf.write("\3\2\2\2\u00b9\u00ba\7\24\2\2\u00ba\u00bb\5\16\b\2\u00bb")
        buf.write("\u00bc\b\4\1\2\u00bc\u00ce\3\2\2\2\u00bd\u00be\7\25\2")
        buf.write("\2\u00be\u00bf\5\16\b\2\u00bf\u00c0\b\4\1\2\u00c0\u00ce")
        buf.write("\3\2\2\2\u00c1\u00c2\7\26\2\2\u00c2\u00c3\5\16\b\2\u00c3")
        buf.write("\u00c4\b\4\1\2\u00c4\u00ce\3\2\2\2\u00c5\u00c6\7\27\2")
        buf.write("\2\u00c6\u00c7\5\16\b\2\u00c7\u00c8\b\4\1\2\u00c8\u00ce")
        buf.write("\3\2\2\2\u00c9\u00ca\7\30\2\2\u00ca\u00cb\5\16\b\2\u00cb")
        buf.write("\u00cc\b\4\1\2\u00cc\u00ce\3\2\2\2\u00cd\u00b5\3\2\2\2")
        buf.write("\u00cd\u00b9\3\2\2\2\u00cd\u00bd\3\2\2\2\u00cd\u00c1\3")
        buf.write("\2\2\2\u00cd\u00c5\3\2\2\2\u00cd\u00c9\3\2\2\2\u00ce\7")
        buf.write("\3\2\2\2\u00cf\u00d0\5> \2\u00d0\u00d1\7\31\2\2\u00d1")
        buf.write("\u00d2\5&\24\2\u00d2\u00d3\b\5\1\2\u00d3\u00df\3\2\2\2")
        buf.write("\u00d4\u00d5\5\n\6\2\u00d5\u00dc\7\31\2\2\u00d6\u00d7")
        buf.write("\5\b\5\2\u00d7\u00d8\b\5\1\2\u00d8\u00dd\3\2\2\2\u00d9")
        buf.write("\u00da\5\22\n\2\u00da\u00db\b\5\1\2\u00db\u00dd\3\2\2")
        buf.write("\2\u00dc\u00d6\3\2\2\2\u00dc\u00d9\3\2\2\2\u00dd\u00df")
        buf.write("\3\2\2\2\u00de\u00cf\3\2\2\2\u00de\u00d4\3\2\2\2\u00df")
        buf.write("\t\3\2\2\2\u00e0\u00e1\5\f\7\2\u00e1\u00ed\b\6\1\2\u00e2")
        buf.write("\u00e3\7\32\2\2\u00e3\u00e4\5> \2\u00e4\u00e5\b\6\1\2")
        buf.write("\u00e5\u00ec\3\2\2\2\u00e6\u00e7\7\33\2\2\u00e7\u00e8")
        buf.write("\5\20\t\2\u00e8\u00e9\7\34\2\2\u00e9\u00ea\b\6\1\2\u00ea")
        buf.write("\u00ec\3\2\2\2\u00eb\u00e2\3\2\2\2\u00eb\u00e6\3\2\2\2")
        buf.write("\u00ec\u00ef\3\2\2\2\u00ed\u00eb\3\2\2\2\u00ed\u00ee\3")
        buf.write("\2\2\2\u00ee\u00f9\3\2\2\2\u00ef\u00ed\3\2\2\2\u00f0\u00f1")
        buf.write("\7\33\2\2\u00f1\u00f2\5B\"\2\u00f2\u00f3\7\34\2\2\u00f3")
        buf.write("\u00f4\b\6\1\2\u00f4\u00f9\3\2\2\2\u00f5\u00f6\6\6\2\3")
        buf.write("\u00f6\u00f7\7\35\2\2\u00f7\u00f9\b\6\1\2\u00f8\u00e0")
        buf.write("\3\2\2\2\u00f8\u00f0\3\2\2\2\u00f8\u00f5\3\2\2\2\u00f9")
        buf.write("\13\3\2\2\2\u00fa\u00fb\7\66\2\2\u00fb\u00fc\b\7\1\2\u00fc")
        buf.write("\r\3\2\2\2\u00fd\u00fe\5\22\n\2\u00fe\u00ff\b\b\1\2\u00ff")
        buf.write("\17\3\2\2\2\u0100\u0101\5\22\n\2\u0101\u0108\b\t\1\2\u0102")
        buf.write("\u0103\7\36\2\2\u0103\u0104\5\22\n\2\u0104\u0105\b\t\1")
        buf.write("\2\u0105\u0107\3\2\2\2\u0106\u0102\3\2\2\2\u0107\u010a")
        buf.write("\3\2\2\2\u0108\u0106\3\2\2\2\u0108\u0109\3\2\2\2\u0109")
        buf.write("\21\3\2\2\2\u010a\u0108\3\2\2\2\u010b\u010c\5\24\13\2")
        buf.write("\u010c\u010d\b\n\1\2\u010d\23\3\2\2\2\u010e\u010f\5\26")
        buf.write("\f\2\u010f\u0110\b\13\1\2\u0110\25\3\2\2\2\u0111\u0112")
        buf.write("\5\30\r\2\u0112\u0119\b\f\1\2\u0113\u0114\7\37\2\2\u0114")
        buf.write("\u0115\5\30\r\2\u0115\u0116\b\f\1\2\u0116\u0118\3\2\2")
        buf.write("\2\u0117\u0113\3\2\2\2\u0118\u011b\3\2\2\2\u0119\u0117")
        buf.write("\3\2\2\2\u0119\u011a\3\2\2\2\u011a\27\3\2\2\2\u011b\u0119")
        buf.write("\3\2\2\2\u011c\u011d\5\32\16\2\u011d\u0124\b\r\1\2\u011e")
        buf.write("\u011f\7 \2\2\u011f\u0120\5\32\16\2\u0120\u0121\b\r\1")
        buf.write("\2\u0121\u0123\3\2\2\2\u0122\u011e\3\2\2\2\u0123\u0126")
        buf.write("\3\2\2\2\u0124\u0122\3\2\2\2\u0124\u0125\3\2\2\2\u0125")
        buf.write("\31\3\2\2\2\u0126\u0124\3\2\2\2\u0127\u0128\5\34\17\2")
        buf.write("\u0128\u0149\b\16\1\2\u0129\u012a\7!\2\2\u012a\u012b\5")
        buf.write("\34\17\2\u012b\u012c\b\16\1\2\u012c\u014a\3\2\2\2\u012d")
        buf.write("\u012e\7\"\2\2\u012e\u012f\5\34\17\2\u012f\u0130\b\16")
        buf.write("\1\2\u0130\u014a\3\2\2\2\u0131\u0132\7#\2\2\u0132\u0133")
        buf.write("\5\34\17\2\u0133\u0134\b\16\1\2\u0134\u014a\3\2\2\2\u0135")
        buf.write("\u0136\7$\2\2\u0136\u0137\5\34\17\2\u0137\u0138\b\16\1")
        buf.write("\2\u0138\u014a\3\2\2\2\u0139\u013a\7%\2\2\u013a\u013b")
        buf.write("\5\34\17\2\u013b\u013c\b\16\1\2\u013c\u014a\3\2\2\2\u013d")
        buf.write("\u013e\7&\2\2\u013e\u013f\5\34\17\2\u013f\u0140\b\16\1")
        buf.write("\2\u0140\u014a\3\2\2\2\u0141\u0142\7\'\2\2\u0142\u0143")
        buf.write("\5\34\17\2\u0143\u0144\b\16\1\2\u0144\u014a\3\2\2\2\u0145")
        buf.write("\u0146\7(\2\2\u0146\u0147\5\34\17\2\u0147\u0148\b\16\1")
        buf.write("\2\u0148\u014a\3\2\2\2\u0149\u0129\3\2\2\2\u0149\u012d")
        buf.write("\3\2\2\2\u0149\u0131\3\2\2\2\u0149\u0135\3\2\2\2\u0149")
        buf.write("\u0139\3\2\2\2\u0149\u013d\3\2\2\2\u0149\u0141\3\2\2\2")
        buf.write("\u0149\u0145\3\2\2\2\u0149\u014a\3\2\2\2\u014a\33\3\2")
        buf.write("\2\2\u014b\u014c\5\36\20\2\u014c\u0157\b\17\1\2\u014d")
        buf.write("\u014e\7)\2\2\u014e\u014f\5\36\20\2\u014f\u0150\b\17\1")
        buf.write("\2\u0150\u0156\3\2\2\2\u0151\u0152\7*\2\2\u0152\u0153")
        buf.write("\5\36\20\2\u0153\u0154\b\17\1\2\u0154\u0156\3\2\2\2\u0155")
        buf.write("\u014d\3\2\2\2\u0155\u0151\3\2\2\2\u0156\u0159\3\2\2\2")
        buf.write("\u0157\u0155\3\2\2\2\u0157\u0158\3\2\2\2\u0158\35\3\2")
        buf.write("\2\2\u0159\u0157\3\2\2\2\u015a\u015b\5 \21\2\u015b\u016e")
        buf.write("\b\20\1\2\u015c\u015d\7+\2\2\u015d\u015e\5 \21\2\u015e")
        buf.write("\u015f\b\20\1\2\u015f\u016d\3\2\2\2\u0160\u0161\7,\2\2")
        buf.write("\u0161\u0162\5 \21\2\u0162\u0163\b\20\1\2\u0163\u016d")
        buf.write("\3\2\2\2\u0164\u0165\7-\2\2\u0165\u0166\5 \21\2\u0166")
        buf.write("\u0167\b\20\1\2\u0167\u016d\3\2\2\2\u0168\u0169\7.\2\2")
        buf.write("\u0169\u016a\5 \21\2\u016a\u016b\b\20\1\2\u016b\u016d")
        buf.write("\3\2\2\2\u016c\u015c\3\2\2\2\u016c\u0160\3\2\2\2\u016c")
        buf.write("\u0164\3\2\2\2\u016c\u0168\3\2\2\2\u016d\u0170\3\2\2\2")
        buf.write("\u016e\u016c\3\2\2\2\u016e\u016f\3\2\2\2\u016f\37\3\2")
        buf.write("\2\2\u0170\u016e\3\2\2\2\u0171\u0172\5\"\22\2\u0172\u0173")
        buf.write("\b\21\1\2\u0173!\3\2\2\2\u0174\u0175\5$\23\2\u0175\u017a")
        buf.write("\b\22\1\2\u0176\u0177\7/\2\2\u0177\u0178\5\"\22\2\u0178")
        buf.write("\u0179\b\22\1\2\u0179\u017b\3\2\2\2\u017a\u0176\3\2\2")
        buf.write("\2\u017a\u017b\3\2\2\2\u017b\u0181\3\2\2\2\u017c\u017d")
        buf.write("\7*\2\2\u017d\u017e\5\"\22\2\u017e\u017f\b\22\1\2\u017f")
        buf.write("\u0181\3\2\2\2\u0180\u0174\3\2\2\2\u0180\u017c\3\2\2\2")
        buf.write("\u0181#\3\2\2\2\u0182\u0183\7\60\2\2\u0183\u0184\5$\23")
        buf.write("\2\u0184\u0185\b\23\1\2\u0185\u01aa\3\2\2\2\u0186\u0187")
        buf.write("\7\4\2\2\u0187\u0188\5\22\n\2\u0188\u0189\7\5\2\2\u0189")
        buf.write("\u018a\b\23\1\2\u018a\u0192\3\2\2\2\u018b\u018c\5&\24")
        buf.write("\2\u018c\u018d\b\23\1\2\u018d\u0192\3\2\2\2\u018e\u018f")
        buf.write("\5> \2\u018f\u0190\b\23\1\2\u0190\u0192\3\2\2\2\u0191")
        buf.write("\u0186\3\2\2\2\u0191\u018b\3\2\2\2\u0191\u018e\3\2\2\2")
        buf.write("\u0192\u019c\3\2\2\2\u0193\u0194\7\32\2\2\u0194\u0195")
        buf.write("\5> \2\u0195\u0196\b\23\1\2\u0196\u019b\3\2\2\2\u0197")
        buf.write("\u0198\5.\30\2\u0198\u0199\b\23\1\2\u0199\u019b\3\2\2")
        buf.write("\2\u019a\u0193\3\2\2\2\u019a\u0197\3\2\2\2\u019b\u019e")
        buf.write("\3\2\2\2\u019c\u019a\3\2\2\2\u019c\u019d\3\2\2\2\u019d")
        buf.write("\u01a1\3\2\2\2\u019e\u019c\3\2\2\2\u019f\u01a0\7\60\2")
        buf.write("\2\u01a0\u01a2\b\23\1\2\u01a1\u019f\3\2\2\2\u01a1\u01a2")
        buf.write("\3\2\2\2\u01a2\u01aa\3\2\2\2\u01a3\u01a4\5\64\33\2\u01a4")
        buf.write("\u01a7\b\23\1\2\u01a5\u01a6\7\60\2\2\u01a6\u01a8\b\23")
        buf.write("\1\2\u01a7\u01a5\3\2\2\2\u01a7\u01a8\3\2\2\2\u01a8\u01aa")
        buf.write("\3\2\2\2\u01a9\u0182\3\2\2\2\u01a9\u0191\3\2\2\2\u01a9")
        buf.write("\u01a3\3\2\2\2\u01aa%\3\2\2\2\u01ab\u01ac\7\61\2\2\u01ac")
        buf.write("\u01ad\7\4\2\2\u01ad\u01ae\5(\25\2\u01ae\u01af\7\5\2\2")
        buf.write("\u01af\u01b0\7\6\2\2\u01b0\u01b1\5\2\2\2\u01b1\u01b2\7")
        buf.write("\7\2\2\u01b2\u01b3\b\24\1\2\u01b3\'\3\2\2\2\u01b4\u01b5")
        buf.write("\5*\26\2\u01b5\u01bc\b\25\1\2\u01b6\u01b7\7\36\2\2\u01b7")
        buf.write("\u01b8\5*\26\2\u01b8\u01b9\b\25\1\2\u01b9\u01bb\3\2\2")
        buf.write("\2\u01ba\u01b6\3\2\2\2\u01bb\u01be\3\2\2\2\u01bc\u01ba")
        buf.write("\3\2\2\2\u01bc\u01bd\3\2\2\2\u01bd\u01c5\3\2\2\2\u01be")
        buf.write("\u01bc\3\2\2\2\u01bf\u01c0\7\36\2\2\u01c0\u01c1\5,\27")
        buf.write("\2\u01c1\u01c2\b\25\1\2\u01c2\u01c4\3\2\2\2\u01c3\u01bf")
        buf.write("\3\2\2\2\u01c4\u01c7\3\2\2\2\u01c5\u01c3\3\2\2\2\u01c5")
        buf.write("\u01c6\3\2\2\2\u01c6\u01d5\3\2\2\2\u01c7\u01c5\3\2\2\2")
        buf.write("\u01c8\u01c9\5,\27\2\u01c9\u01d0\b\25\1\2\u01ca\u01cb")
        buf.write("\7\36\2\2\u01cb\u01cc\5,\27\2\u01cc\u01cd\b\25\1\2\u01cd")
        buf.write("\u01cf\3\2\2\2\u01ce\u01ca\3\2\2\2\u01cf\u01d2\3\2\2\2")
        buf.write("\u01d0\u01ce\3\2\2\2\u01d0\u01d1\3\2\2\2\u01d1\u01d5\3")
        buf.write("\2\2\2\u01d2\u01d0\3\2\2\2\u01d3\u01d5\3\2\2\2\u01d4\u01b4")
        buf.write("\3\2\2\2\u01d4\u01c8\3\2\2\2\u01d4\u01d3\3\2\2\2\u01d5")
        buf.write(")\3\2\2\2\u01d6\u01d7\5> \2\u01d7\u01d8\b\26\1\2\u01d8")
        buf.write("+\3\2\2\2\u01d9\u01da\5\f\7\2\u01da\u01db\7\31\2\2\u01db")
        buf.write("\u01dc\5\16\b\2\u01dc\u01dd\b\27\1\2\u01dd-\3\2\2\2\u01de")
        buf.write("\u01df\7\4\2\2\u01df\u01e0\5\62\32\2\u01e0\u01e1\7\5\2")
        buf.write("\2\u01e1\u01e2\b\30\1\2\u01e2\u01e9\3\2\2\2\u01e3\u01e4")
        buf.write("\7\33\2\2\u01e4\u01e5\5\60\31\2\u01e5\u01e6\7\34\2\2\u01e6")
        buf.write("\u01e7\b\30\1\2\u01e7\u01e9\3\2\2\2\u01e8\u01de\3\2\2")
        buf.write("\2\u01e8\u01e3\3\2\2\2\u01e9/\3\2\2\2\u01ea\u01fd\5\16")
        buf.write("\b\2\u01eb\u01f0\79\2\2\u01ec\u01ed\5\16\b\2\u01ed\u01ee")
        buf.write("\b\31\1\2\u01ee\u01f1\3\2\2\2\u01ef\u01f1\b\31\1\2\u01f0")
        buf.write("\u01ec\3\2\2\2\u01f0\u01ef\3\2\2\2\u01f1\u01fe\3\2\2\2")
        buf.write("\u01f2\u01f3\7\36\2\2\u01f3\u01f4\5\16\b\2\u01f4\u01f5")
        buf.write("\b\31\1\2\u01f5\u01f7\3\2\2\2\u01f6\u01f2\3\2\2\2\u01f7")
        buf.write("\u01f8\3\2\2\2\u01f8\u01f6\3\2\2\2\u01f8\u01f9\3\2\2\2")
        buf.write("\u01f9\u01fa\3\2\2\2\u01fa\u01fb\b\31\1\2\u01fb\u01fe")
        buf.write("\3\2\2\2\u01fc\u01fe\b\31\1\2\u01fd\u01eb\3\2\2\2\u01fd")
        buf.write("\u01f6\3\2\2\2\u01fd\u01fc\3\2\2\2\u01fe\u0204\3\2\2\2")
        buf.write("\u01ff\u0200\79\2\2\u0200\u0201\5\16\b\2\u0201\u0202\b")
        buf.write("\31\1\2\u0202\u0204\3\2\2\2\u0203\u01ea\3\2\2\2\u0203")
        buf.write("\u01ff\3\2\2\2\u0204\61\3\2\2\2\u0205\u0206\5\20\t\2\u0206")
        buf.write("\u0207\b\32\1\2\u0207\u020a\3\2\2\2\u0208\u020a\3\2\2")
        buf.write("\2\u0209\u0205\3\2\2\2\u0209\u0208\3\2\2\2\u020a\63\3")
        buf.write("\2\2\2\u020b\u020f\7\33\2\2\u020c\u020d\5\66\34\2\u020d")
        buf.write("\u020e\b\33\1\2\u020e\u0210\3\2\2\2\u020f\u020c\3\2\2")
        buf.write("\2\u020f\u0210\3\2\2\2\u0210\u0211\3\2\2\2\u0211\u0212")
        buf.write("\7\34\2\2\u0212\u021e\b\33\1\2\u0213\u0214\7:\2\2\u0214")
        buf.write("\u021e\b\33\1\2\u0215\u0216\7;\2\2\u0216\u021e\b\33\1")
        buf.write("\2\u0217\u0218\5<\37\2\u0218\u0219\b\33\1\2\u0219\u021e")
        buf.write("\3\2\2\2\u021a\u021b\6\33\3\3\u021b\u021c\7\35\2\2\u021c")
        buf.write("\u021e\b\33\1\2\u021d\u020b\3\2\2\2\u021d\u0213\3\2\2")
        buf.write("\2\u021d\u0215\3\2\2\2\u021d\u0217\3\2\2\2\u021d\u021a")
        buf.write("\3\2\2\2\u021e\65\3\2\2\2\u021f\u024e\5\16\b\2\u0220\u0221")
        buf.write("\7\36\2\2\u0221\u0237\5\16\b\2\u0222\u0223\79\2\2\u0223")
        buf.write("\u0224\5\16\b\2\u0224\u0225\b\34\1\2\u0225\u0238\3\2\2")
        buf.write("\2\u0226\u022d\b\34\1\2\u0227\u0228\7\36\2\2\u0228\u0229")
        buf.write("\5\16\b\2\u0229\u022a\b\34\1\2\u022a\u022c\3\2\2\2\u022b")
        buf.write("\u0227\3\2\2\2\u022c\u022f\3\2\2\2\u022d\u022b\3\2\2\2")
        buf.write("\u022d\u022e\3\2\2\2\u022e\u0235\3\2\2\2\u022f\u022d\3")
        buf.write("\2\2\2\u0230\u0231\7\n\2\2\u0231\u0232\5\16\b\2\u0232")
        buf.write("\u0233\b\34\1\2\u0233\u0236\3\2\2\2\u0234\u0236\b\34\1")
        buf.write("\2\u0235\u0230\3\2\2\2\u0235\u0234\3\2\2\2\u0236\u0238")
        buf.write("\3\2\2\2\u0237\u0222\3\2\2\2\u0237\u0226\3\2\2\2\u0238")
        buf.write("\u024f\3\2\2\2\u0239\u023a\79\2\2\u023a\u023b\5\16\b\2")
        buf.write("\u023b\u023c\b\34\1\2\u023c\u024f\3\2\2\2\u023d\u0243")
        buf.write("\b\34\1\2\u023e\u023f\7\n\2\2\u023f\u0240\5\16\b\2\u0240")
        buf.write("\u0241\b\34\1\2\u0241\u0244\3\2\2\2\u0242\u0244\b\34\1")
        buf.write("\2\u0243\u023e\3\2\2\2\u0243\u0242\3\2\2\2\u0244\u024f")
        buf.write("\3\2\2\2\u0245\u0246\7\62\2\2\u0246\u024c\58\35\2\u0247")
        buf.write("\u0248\7\n\2\2\u0248\u0249\5@!\2\u0249\u024a\b\34\1\2")
        buf.write("\u024a\u024d\3\2\2\2\u024b\u024d\b\34\1\2\u024c\u0247")
        buf.write("\3\2\2\2\u024c\u024b\3\2\2\2\u024d\u024f\3\2\2\2\u024e")
        buf.write("\u0220\3\2\2\2\u024e\u0239\3\2\2\2\u024e\u023d\3\2\2\2")
        buf.write("\u024e\u0245\3\2\2\2\u024f\67\3\2\2\2\u0250\u0251\5:\36")
        buf.write("\2\u0251\u0258\b\35\1\2\u0252\u0253\7\36\2\2\u0253\u0254")
        buf.write("\5:\36\2\u0254\u0255\b\35\1\2\u0255\u0257\3\2\2\2\u0256")
        buf.write("\u0252\3\2\2\2\u0257\u025a\3\2\2\2\u0258\u0256\3\2\2\2")
        buf.write("\u0258\u0259\3\2\2\2\u02599\3\2\2\2\u025a\u0258\3\2\2")
        buf.write("\2\u025b\u025c\5\n\6\2\u025c\u025d\7\'\2\2\u025d\u025e")
        buf.write("\5\16\b\2\u025e\u025f\b\36\1\2\u025f;\3\2\2\2\u0260\u0261")
        buf.write("\7\67\2\2\u0261\u026b\b\37\1\2\u0262\u0263\78\2\2\u0263")
        buf.write("\u026b\b\37\1\2\u0264\u0265\7\63\2\2\u0265\u026b\b\37")
        buf.write("\1\2\u0266\u0267\7\64\2\2\u0267\u026b\b\37\1\2\u0268\u0269")
        buf.write("\7\65\2\2\u0269\u026b\b\37\1\2\u026a\u0260\3\2\2\2\u026a")
        buf.write("\u0262\3\2\2\2\u026a\u0264\3\2\2\2\u026a\u0266\3\2\2\2")
        buf.write("\u026a\u0268\3\2\2\2\u026b=\3\2\2\2\u026c\u026d\7\66\2")
        buf.write("\2\u026d\u026e\b \1\2\u026e?\3\2\2\2\u026f\u0270\5\16")
        buf.write("\b\2\u0270\u0271\b!\1\2\u0271A\3\2\2\2\u0272\u0273\5\n")
        buf.write("\6\2\u0273\u027a\b\"\1\2\u0274\u0275\7\36\2\2\u0275\u0276")
        buf.write("\5\n\6\2\u0276\u0277\b\"\1\2\u0277\u0279\3\2\2\2\u0278")
        buf.write("\u0274\3\2\2\2\u0279\u027c\3\2\2\2\u027a\u0278\3\2\2\2")
        buf.write("\u027a\u027b\3\2\2\2\u027bC\3\2\2\2\u027c\u027a\3\2\2")
        buf.write("\2\63Ibkv\u00a2\u00b2\u00cd\u00dc\u00de\u00eb\u00ed\u00f8")
        buf.write("\u0108\u0119\u0124\u0149\u0155\u0157\u016c\u016e\u017a")
        buf.write("\u0180\u0191\u019a\u019c\u01a1\u01a7\u01a9\u01bc\u01c5")
        buf.write("\u01d0\u01d4\u01e8\u01f0\u01f8\u01fd\u0203\u0209\u020f")
        buf.write("\u021d\u022d\u0235\u0237\u0243\u024c\u024e\u0258\u026a")
        buf.write("\u027a")
        return buf.getvalue()


class SetlXgrammarParser ( Parser ):

    grammarFileName = "SetlXgrammar.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'if'", "'('", "')'", "'{'", "'}'", "'else'", 
                     "'for'", "'|'", "'while'", "'do'", "';'", "'backtrack'", 
                     "'break'", "'continue'", "'exit'", "'return'", "'+='", 
                     "'-='", "'*='", "'/='", "'\\='", "'%='", "':='", "'.'", 
                     "'['", "']'", "'_'", "','", "'||'", "'&&'", "'=='", 
                     "'!='", "'<'", "'<='", "'>'", "'>='", "'in'", "'notin'", 
                     "'+'", "'-'", "'*'", "'/'", "'\\'", "'%'", "'**'", 
                     "'!'", "'procedure'", "':'", "'om'", "'True'", "'False'", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "'..'" ]

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
                      "ID", "NUMBER", "DOUBLE", "RANGE_SIGN", "STRING", 
                      "LITERAL", "LINE_COMMENT", "MULTI_COMMENT", "WS" ]

    RULE_block = 0
    RULE_statement = 1
    RULE_assignmentOther = 2
    RULE_assignmentDirect = 3
    RULE_assignable = 4
    RULE_assignableVariable = 5
    RULE_expr = 6
    RULE_exprList = 7
    RULE_exprContent = 8
    RULE_implication = 9
    RULE_disjunction = 10
    RULE_conjunction = 11
    RULE_comparison = 12
    RULE_setlxSum = 13
    RULE_product = 14
    RULE_setlxReduce = 15
    RULE_prefixOperation = 16
    RULE_factor = 17
    RULE_procedure = 18
    RULE_procedureParameters = 19
    RULE_procedureParameter = 20
    RULE_procedureDefaultParameter = 21
    RULE_call = 22
    RULE_collectionAccessParams = 23
    RULE_callParameters = 24
    RULE_value = 25
    RULE_collectionBuilder = 26
    RULE_iteratorChain = 27
    RULE_iterator = 28
    RULE_atomicValue = 29
    RULE_variable = 30
    RULE_condition = 31
    RULE_assignmentList = 32

    ruleNames =  [ "block", "statement", "assignmentOther", "assignmentDirect", 
                   "assignable", "assignableVariable", "expr", "exprList", 
                   "exprContent", "implication", "disjunction", "conjunction", 
                   "comparison", "setlxSum", "product", "setlxReduce", "prefixOperation", 
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
    ID=52
    NUMBER=53
    DOUBLE=54
    RANGE_SIGN=55
    STRING=56
    LITERAL=57
    LINE_COMMENT=58
    MULTI_COMMENT=59
    WS=60

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
            self.state = 71
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,0,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 66
                    localctx._statement = self.statement()
                    stmnts.append(localctx._statement.stmnt) 
                self.state = 73
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

        ifList = []
        expression = None
        condition = None
            
        self._la = 0 # Token type
        try:
            self.state = 176
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 76
                self.match(SetlXgrammarParser.T__0)
                self.state = 77
                self.match(SetlXgrammarParser.T__1)
                self.state = 78
                localctx.c1 = self.condition()
                self.state = 79
                self.match(SetlXgrammarParser.T__2)
                self.state = 80
                self.match(SetlXgrammarParser.T__3)
                self.state = 81
                localctx.b1 = self.block()
                self.state = 82
                self.match(SetlXgrammarParser.T__4)
                ifList.append(IfThenBranch(localctx.c1.cnd, localctx.b1.blk)) 
                self.state = 96
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,1,self._ctx)
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1:
                        self.state = 84
                        self.match(SetlXgrammarParser.T__5)
                        self.state = 85
                        self.match(SetlXgrammarParser.T__0)
                        self.state = 86
                        self.match(SetlXgrammarParser.T__1)
                        self.state = 87
                        localctx.c2 = self.condition()
                        self.state = 88
                        self.match(SetlXgrammarParser.T__2)
                        self.state = 89
                        self.match(SetlXgrammarParser.T__3)
                        self.state = 90
                        localctx.b2 = self.block()
                        self.state = 91
                        self.match(SetlXgrammarParser.T__4)
                        ifList.append(IfThenElseIfBranch(localctx.c2.cnd, localctx.b2.blk))  
                    self.state = 98
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,1,self._ctx)

                self.state = 105
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
                if la_ == 1:
                    self.state = 99
                    self.match(SetlXgrammarParser.T__5)
                    self.state = 100
                    self.match(SetlXgrammarParser.T__3)
                    self.state = 101
                    localctx.b3 = self.block()
                    self.state = 102
                    self.match(SetlXgrammarParser.T__4)
                    ifList.append(IfThenElseBranch(localctx.b3.blk))                  


                localctx.stmnt = IfThen(ifList) 
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 109
                self.match(SetlXgrammarParser.T__6)
                self.state = 110
                self.match(SetlXgrammarParser.T__1)
                self.state = 111
                localctx._iteratorChain = self.iteratorChain(False)
                self.state = 116
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==SetlXgrammarParser.T__7:
                    self.state = 112
                    self.match(SetlXgrammarParser.T__7)
                    self.state = 113
                    localctx._condition = self.condition()
                    condition = localctx._condition.cnd


                self.state = 118
                self.match(SetlXgrammarParser.T__2)
                self.state = 119
                self.match(SetlXgrammarParser.T__3)
                self.state = 120
                localctx._block = self.block()
                self.state = 121
                self.match(SetlXgrammarParser.T__4)
                localctx.stmnt = For(localctx._iteratorChain.ic, condition, localctx._block.blk) 
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 124
                self.match(SetlXgrammarParser.T__8)
                self.state = 125
                self.match(SetlXgrammarParser.T__1)
                self.state = 126
                localctx._condition = self.condition()
                self.state = 127
                self.match(SetlXgrammarParser.T__2)
                self.state = 128
                self.match(SetlXgrammarParser.T__3)
                self.state = 129
                localctx._block = self.block()
                self.state = 130
                self.match(SetlXgrammarParser.T__4)
                localctx.stmnt = While(localctx._condition.cnd, localctx._block.blk) 
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 133
                self.match(SetlXgrammarParser.T__9)
                self.state = 134
                self.match(SetlXgrammarParser.T__3)
                self.state = 135
                localctx._block = self.block()
                self.state = 136
                self.match(SetlXgrammarParser.T__4)
                self.state = 137
                self.match(SetlXgrammarParser.T__8)
                self.state = 138
                self.match(SetlXgrammarParser.T__1)
                self.state = 139
                localctx._condition = self.condition()
                self.state = 140
                self.match(SetlXgrammarParser.T__2)
                self.state = 141
                self.match(SetlXgrammarParser.T__10)
                localctx.stmnt = DoWhile(localctx._condition.cnd, localctx._block.blk) 
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 144
                self.match(SetlXgrammarParser.T__11)
                self.state = 145
                self.match(SetlXgrammarParser.T__10)
                localctx.stmnt = Backtrack() 
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 147
                self.match(SetlXgrammarParser.T__12)
                self.state = 148
                self.match(SetlXgrammarParser.T__10)
                localctx.stmnt = Break() 
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 150
                self.match(SetlXgrammarParser.T__13)
                self.state = 151
                self.match(SetlXgrammarParser.T__10)
                localctx.stmnt = Continue() 
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 153
                self.match(SetlXgrammarParser.T__14)
                self.state = 154
                self.match(SetlXgrammarParser.T__10)
                localctx.stmnt = Exit() 
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 156
                self.match(SetlXgrammarParser.T__15)
                self.state = 160
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
                if la_ == 1:
                    self.state = 157
                    localctx._expr = self.expr(False)
                    expression = localctx._expr.ex 


                self.state = 162
                self.match(SetlXgrammarParser.T__10)
                localctx.stmnt = Return(expression) 
                pass

            elif la_ == 10:
                self.enterOuterAlt(localctx, 10)
                self.state = 164
                localctx._assignmentOther = self.assignmentOther()
                self.state = 165
                self.match(SetlXgrammarParser.T__10)
                localctx.stmnt = localctx._assignmentOther.assign 
                pass

            elif la_ == 11:
                self.enterOuterAlt(localctx, 11)
                self.state = 168
                localctx._assignmentDirect = self.assignmentDirect()
                self.state = 169
                self.match(SetlXgrammarParser.T__10)
                localctx.stmnt = localctx._assignmentDirect.assign 
                pass

            elif la_ == 12:
                self.enterOuterAlt(localctx, 12)
                self.state = 172
                localctx._expr = self.expr(False)
                self.state = 173
                self.match(SetlXgrammarParser.T__10)
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
            self.state = 178
            localctx._assignable = self.assignable(False)
            self.state = 203
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [SetlXgrammarParser.T__16]:
                self.state = 179
                self.match(SetlXgrammarParser.T__16)
                self.state = 180
                localctx.e = self.expr(False)
                localctx.assign = SumAssignment(localctx._assignable.a, localctx.e.ex) 
                pass
            elif token in [SetlXgrammarParser.T__17]:
                self.state = 183
                self.match(SetlXgrammarParser.T__17)
                self.state = 184
                localctx.e = self.expr(False)
                localctx.assign = DifferenceAssignment(localctx._assignable.a, localctx.e.ex) 
                pass
            elif token in [SetlXgrammarParser.T__18]:
                self.state = 187
                self.match(SetlXgrammarParser.T__18)
                self.state = 188
                localctx.e = self.expr(False)
                localctx.assign = ProductAssignment(localctx._assignable.a, localctx.e.ex) 
                pass
            elif token in [SetlXgrammarParser.T__19]:
                self.state = 191
                self.match(SetlXgrammarParser.T__19)
                self.state = 192
                localctx.e = self.expr(False)
                localctx.assign = QuotientAssignment(localctx._assignable.a, localctx.e.ex) 
                pass
            elif token in [SetlXgrammarParser.T__20]:
                self.state = 195
                self.match(SetlXgrammarParser.T__20)
                self.state = 196
                localctx.e = self.expr(False)
                localctx.assign = IntegerDivisionAssignment(localctx._assignable.a, localctx.e.ex) 
                pass
            elif token in [SetlXgrammarParser.T__21]:
                self.state = 199
                self.match(SetlXgrammarParser.T__21)
                self.state = 200
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
            self.state = 220
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,8,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 205
                localctx._variable = self.variable()
                self.state = 206
                self.match(SetlXgrammarParser.T__22)
                self.state = 207
                localctx._procedure = self.procedure()

                localctx._procedure.pd.name = localctx._variable.v.id
                localctx.assign = localctx._procedure.pd
                    
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 210
                localctx._assignable = self.assignable(False)
                self.state = 211
                self.match(SetlXgrammarParser.T__22)
                self.state = 218
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,7,self._ctx)
                if la_ == 1:
                    self.state = 212
                    localctx._assignmentDirect = self.assignmentDirect()
                    localctx.assign = Assignment(localctx._assignable.a, localctx._assignmentDirect.assign)
                    			
                    pass

                elif la_ == 2:
                    self.state = 215
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
            self.state = 246
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,11,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 222
                localctx._assignableVariable = self.assignableVariable()
                localctx.a = localctx._assignableVariable.v
                self.state = 235
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==SetlXgrammarParser.T__23 or _la==SetlXgrammarParser.T__24:
                    self.state = 233
                    self._errHandler.sync(self)
                    token = self._input.LA(1)
                    if token in [SetlXgrammarParser.T__23]:
                        self.state = 224
                        self.match(SetlXgrammarParser.T__23)
                        self.state = 225
                        localctx._variable = self.variable()
                        localctx.a = AssignableMember(localctx.a, localctx._variable.v)
                        pass
                    elif token in [SetlXgrammarParser.T__24]:
                        self.state = 228
                        self.match(SetlXgrammarParser.T__24)
                        self.state = 229
                        self.exprList(False)
                        self.state = 230
                        self.match(SetlXgrammarParser.T__25)
                        localctx.a = AssignableCollectionAccess(localctx.a)
                        pass
                    else:
                        raise NoViableAltException(self)

                    self.state = 237
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 238
                self.match(SetlXgrammarParser.T__24)
                self.state = 239
                localctx._assignmentList = self.assignmentList()
                self.state = 240
                self.match(SetlXgrammarParser.T__25)
                localctx.a = AssignableList(localctx._assignmentList.al)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 243
                if not localctx.enableIgnore:
                    from antlr4.error.Errors import FailedPredicateException
                    raise FailedPredicateException(self, "$enableIgnore")
                self.state = 244
                self.match(SetlXgrammarParser.T__26)
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
            self.state = 248
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
        self.enterRule(localctx, 12, self.RULE_expr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 251
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
            self.state = 254
            localctx._exprContent = self.exprContent(localctx.enableIgnore)
            localctx.exprs.append(localctx._exprContent.ex)
            self.state = 262
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==SetlXgrammarParser.T__27:
                self.state = 256
                self.match(SetlXgrammarParser.T__27)
                self.state = 257
                localctx._exprContent = self.exprContent(localctx.enableIgnore)
                localctx.exprs.append(localctx._exprContent.ex)
                self.state = 264
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
        self.enterRule(localctx, 16, self.RULE_exprContent)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 265
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
        self.enterRule(localctx, 18, self.RULE_implication)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 268
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
        self.enterRule(localctx, 20, self.RULE_disjunction)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 271
            localctx._conjunction = self.conjunction(localctx.enableIgnore)
            localctx.d = localctx._conjunction.c
            self.state = 279
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==SetlXgrammarParser.T__28:
                self.state = 273
                self.match(SetlXgrammarParser.T__28)
                self.state = 274
                localctx._conjunction = self.conjunction(localctx.enableIgnore)
                localctx.d = Disjunction(localctx.d, localctx._conjunction.c) 
                self.state = 281
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
        self.enterRule(localctx, 22, self.RULE_conjunction)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 282
            localctx._comparison = self.comparison(localctx.enableIgnore)
            localctx.c = localctx._comparison.c
            self.state = 290
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==SetlXgrammarParser.T__29:
                self.state = 284
                self.match(SetlXgrammarParser.T__29)
                self.state = 285
                localctx._comparison = self.comparison(localctx.enableIgnore)
                localctx.c = Conjunction(localctx.c, localctx._comparison.c) 
                self.state = 292
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
        self.enterRule(localctx, 24, self.RULE_comparison)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 293
            localctx.s1 = self.setlxSum(localctx.enableIgnore)
            localctx.c = localctx.s1.s 
            self.state = 327
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [SetlXgrammarParser.T__30]:
                self.state = 295
                self.match(SetlXgrammarParser.T__30)
                self.state = 296
                localctx.s2 = self.setlxSum(localctx.enableIgnore)
                localctx.c = Equal(localctx.s1.s,localctx.s2.s) 
                pass
            elif token in [SetlXgrammarParser.T__31]:
                self.state = 299
                self.match(SetlXgrammarParser.T__31)
                self.state = 300
                localctx.s2 = self.setlxSum(localctx.enableIgnore)
                localctx.c = NotEqual(localctx.s1.s,localctx.s2.s) 
                pass
            elif token in [SetlXgrammarParser.T__32]:
                self.state = 303
                self.match(SetlXgrammarParser.T__32)
                self.state = 304
                localctx.s2 = self.setlxSum(localctx.enableIgnore)
                localctx.c = LessThan(localctx.s1.s,localctx.s2.s) 
                pass
            elif token in [SetlXgrammarParser.T__33]:
                self.state = 307
                self.match(SetlXgrammarParser.T__33)
                self.state = 308
                localctx.s2 = self.setlxSum(localctx.enableIgnore)
                localctx.c = LessOrEqual(localctx.s1.s,localctx.s2.s) 
                pass
            elif token in [SetlXgrammarParser.T__34]:
                self.state = 311
                self.match(SetlXgrammarParser.T__34)
                self.state = 312
                localctx.s2 = self.setlxSum(localctx.enableIgnore)
                localctx.c = GreaterThan(localctx.s1.s,localctx.s2.s) 
                pass
            elif token in [SetlXgrammarParser.T__35]:
                self.state = 315
                self.match(SetlXgrammarParser.T__35)
                self.state = 316
                localctx.s2 = self.setlxSum(localctx.enableIgnore)
                localctx.c = GreaterOrEqual(localctx.s1.s,localctx.s2.s) 
                pass
            elif token in [SetlXgrammarParser.T__36]:
                self.state = 319
                self.match(SetlXgrammarParser.T__36)
                self.state = 320
                localctx.s2 = self.setlxSum(localctx.enableIgnore)
                localctx.c = In(localctx.s1.s,localctx.s2.s) 
                pass
            elif token in [SetlXgrammarParser.T__37]:
                self.state = 323
                self.match(SetlXgrammarParser.T__37)
                self.state = 324
                localctx.s2 = self.setlxSum(localctx.enableIgnore)
                localctx.c = NotIn(localctx.s1.s,localctx.s2.s) 
                pass
            elif token in [SetlXgrammarParser.T__2, SetlXgrammarParser.T__7, SetlXgrammarParser.T__10, SetlXgrammarParser.T__25, SetlXgrammarParser.T__27, SetlXgrammarParser.T__28, SetlXgrammarParser.T__29, SetlXgrammarParser.T__47, SetlXgrammarParser.RANGE_SIGN]:
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
        self.enterRule(localctx, 26, self.RULE_setlxSum)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 329
            localctx.p1 = self.product(localctx.enableIgnore)
            localctx.s = localctx.p1.p
            self.state = 341
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==SetlXgrammarParser.T__38 or _la==SetlXgrammarParser.T__39:
                self.state = 339
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [SetlXgrammarParser.T__38]:
                    self.state = 331
                    self.match(SetlXgrammarParser.T__38)
                    self.state = 332
                    localctx.p2 = self.product(localctx.enableIgnore)
                    localctx.s = Sum(localctx.p1.p,localctx.p2.p) 
                    pass
                elif token in [SetlXgrammarParser.T__39]:
                    self.state = 335
                    self.match(SetlXgrammarParser.T__39)
                    self.state = 336
                    localctx.p2 = self.product(localctx.enableIgnore)
                    localctx.s = Difference(localctx.p1.p,localctx.p2.p) 
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 343
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
        self.enterRule(localctx, 28, self.RULE_product)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 344
            localctx.r1 = self.setlxReduce(localctx.enableIgnore)
            localctx.p = localctx.r1.r
            self.state = 364
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << SetlXgrammarParser.T__40) | (1 << SetlXgrammarParser.T__41) | (1 << SetlXgrammarParser.T__42) | (1 << SetlXgrammarParser.T__43))) != 0):
                self.state = 362
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [SetlXgrammarParser.T__40]:
                    self.state = 346
                    self.match(SetlXgrammarParser.T__40)
                    self.state = 347
                    localctx.r2 = self.setlxReduce(localctx.enableIgnore)
                    localctx.p = Product(localctx.p,localctx.r2.r) 
                    pass
                elif token in [SetlXgrammarParser.T__41]:
                    self.state = 350
                    self.match(SetlXgrammarParser.T__41)
                    self.state = 351
                    localctx.r2 = self.setlxReduce(localctx.enableIgnore)
                    localctx.p = Quotient(localctx.p,localctx.r2.r) 
                    pass
                elif token in [SetlXgrammarParser.T__42]:
                    self.state = 354
                    self.match(SetlXgrammarParser.T__42)
                    self.state = 355
                    localctx.r2 = self.setlxReduce(localctx.enableIgnore)
                    localctx.p = IntegerDivision(localctx.p,localctx.r2.r) 
                    pass
                elif token in [SetlXgrammarParser.T__43]:
                    self.state = 358
                    self.match(SetlXgrammarParser.T__43)
                    self.state = 359
                    localctx.r2 = self.setlxReduce(localctx.enableIgnore)
                    localctx.p = Modulo(localctx.p,localctx.r2.r) 
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 366
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
        self.enterRule(localctx, 30, self.RULE_setlxReduce)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 367
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
        self.enterRule(localctx, 32, self.RULE_prefixOperation)
        self._la = 0 # Token type
        try:
            self.state = 382
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,21,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 370
                localctx._factor = self.factor(localctx.enableIgnore)
                localctx.p = localctx._factor.f
                self.state = 376
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==SetlXgrammarParser.T__44:
                    self.state = 372
                    self.match(SetlXgrammarParser.T__44)
                    self.state = 373
                    localctx._prefixOperation = self.prefixOperation(localctx.enableIgnore)
                    localctx.p = Power(localctx.p,localctx._prefixOperation.p) 


                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 378
                self.match(SetlXgrammarParser.T__39)
                self.state = 379
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
            self._exprContent = None # ExprContentContext
            self._procedure = None # ProcedureContext
            self._variable = None # VariableContext
            self._call = None # CallContext
            self._value = None # ValueContext
            self.enableIgnore = enableIgnore

        def factor(self):
            return self.getTypedRuleContext(SetlXgrammarParser.FactorContext,0)


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
        self.enterRule(localctx, 34, self.RULE_factor)
        self._la = 0 # Token type
        try:
            self.state = 423
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,27,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 384
                self.match(SetlXgrammarParser.T__45)
                self.state = 385
                localctx._factor = self.factor(localctx.enableIgnore)
                localctx.f = Not(localctx._factor.f) 
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 399
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [SetlXgrammarParser.T__1]:
                    self.state = 388
                    self.match(SetlXgrammarParser.T__1)
                    self.state = 389
                    localctx._exprContent = self.exprContent(localctx.enableIgnore)
                    self.state = 390
                    self.match(SetlXgrammarParser.T__2)
                    localctx.f = localctx._exprContent.ex 
                    pass
                elif token in [SetlXgrammarParser.T__46]:
                    self.state = 393
                    localctx._procedure = self.procedure()
                    localctx.f = localctx._procedure.pd 
                    pass
                elif token in [SetlXgrammarParser.ID]:
                    self.state = 396
                    localctx._variable = self.variable()
                    localctx.f = localctx._variable.v 
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 410
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << SetlXgrammarParser.T__1) | (1 << SetlXgrammarParser.T__23) | (1 << SetlXgrammarParser.T__24))) != 0):
                    self.state = 408
                    self._errHandler.sync(self)
                    token = self._input.LA(1)
                    if token in [SetlXgrammarParser.T__23]:
                        self.state = 401
                        self.match(SetlXgrammarParser.T__23)
                        self.state = 402
                        localctx._variable = self.variable()
                        localctx.f = MemberAccess(localctx.f,localctx._variable.v) 
                        pass
                    elif token in [SetlXgrammarParser.T__1, SetlXgrammarParser.T__24]:
                        self.state = 405
                        localctx._call = self.call(localctx.enableIgnore)

                        localctx._call.c.callable = localctx.f
                        localctx.f = localctx._call.c
                                
                        pass
                    else:
                        raise NoViableAltException(self)

                    self.state = 412
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 415
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==SetlXgrammarParser.T__45:
                    self.state = 413
                    self.match(SetlXgrammarParser.T__45)
                    localctx.f = Factorial(localctx.f) 


                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 417
                localctx._value = self.value(localctx.enableIgnore)
                localctx.f = localctx._value.v 
                self.state = 421
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==SetlXgrammarParser.T__45:
                    self.state = 419
                    self.match(SetlXgrammarParser.T__45)
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
        self.enterRule(localctx, 36, self.RULE_procedure)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 425
            self.match(SetlXgrammarParser.T__46)
            self.state = 426
            self.match(SetlXgrammarParser.T__1)
            self.state = 427
            localctx._procedureParameters = self.procedureParameters(True)
            self.state = 428
            self.match(SetlXgrammarParser.T__2)
            self.state = 429
            self.match(SetlXgrammarParser.T__3)
            self.state = 430
            localctx._block = self.block()
            self.state = 431
            self.match(SetlXgrammarParser.T__4)
            localctx.pd = Procedure(localctx._procedureParameters.paramList, localctx._block.blk) 
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
        self.enterRule(localctx, 38, self.RULE_procedureParameters)

        localctx.paramList = []
            
        self._la = 0 # Token type
        try:
            self.state = 466
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,31,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 434
                localctx.pp1 = self.procedureParameter(localctx.enableRw)
                localctx.paramList.append(localctx.pp1.param) 
                self.state = 442
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,28,self._ctx)
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1:
                        self.state = 436
                        self.match(SetlXgrammarParser.T__27)
                        self.state = 437
                        localctx.pp2 = self.procedureParameter(localctx.enableRw)
                        localctx.paramList.append(localctx.pp2.param)  
                    self.state = 444
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,28,self._ctx)

                self.state = 451
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==SetlXgrammarParser.T__27:
                    self.state = 445
                    self.match(SetlXgrammarParser.T__27)
                    self.state = 446
                    localctx.dp1 = self.procedureDefaultParameter()
                    localctx.paramList.append(localctx.dp1.param) 
                    self.state = 453
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 454
                localctx.dp2 = self.procedureDefaultParameter()
                localctx.paramList.append(localctx.dp2.param) 
                self.state = 462
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==SetlXgrammarParser.T__27:
                    self.state = 456
                    self.match(SetlXgrammarParser.T__27)
                    self.state = 457
                    localctx.dp3 = self.procedureDefaultParameter()
                    localctx.paramList.append(localctx.dp3.param) 
                    self.state = 464
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
            self._variable = None # VariableContext
            self.enableRw = enableRw

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
        self.enterRule(localctx, 40, self.RULE_procedureParameter)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 468
            localctx._variable = self.variable()
            localctx.param = Parameter(localctx._variable.v.id) 
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
        self.enterRule(localctx, 42, self.RULE_procedureDefaultParameter)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 471
            localctx._assignableVariable = self.assignableVariable()
            self.state = 472
            self.match(SetlXgrammarParser.T__22)
            self.state = 473
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
        self.enterRule(localctx, 44, self.RULE_call)
        try:
            self.state = 486
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [SetlXgrammarParser.T__1]:
                self.enterOuterAlt(localctx, 1)
                self.state = 476
                self.match(SetlXgrammarParser.T__1)
                self.state = 477
                localctx._callParameters = self.callParameters(localctx.enableIgnore)
                self.state = 478
                self.match(SetlXgrammarParser.T__2)
                localctx.c = FunctionCall(localctx._callParameters.params, localctx._callParameters.ex) 
                pass
            elif token in [SetlXgrammarParser.T__24]:
                self.enterOuterAlt(localctx, 2)
                self.state = 481
                self.match(SetlXgrammarParser.T__24)
                self.state = 482
                localctx._collectionAccessParams = self.collectionAccessParams(localctx.enableIgnore)
                self.state = 483
                self.match(SetlXgrammarParser.T__25)
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
        self.enterRule(localctx, 46, self.RULE_collectionAccessParams)

        params = []
            
        self._la = 0 # Token type
        try:
            self.state = 513
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,36,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 488
                localctx.e1 = self.expr(localctx.enableIgnore)
                self.state = 507
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [SetlXgrammarParser.RANGE_SIGN]:
                    self.state = 489
                    self.match(SetlXgrammarParser.RANGE_SIGN)
                    self.state = 494
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,33,self._ctx)
                    if la_ == 1:
                        self.state = 490
                        localctx.e2 = self.expr(localctx.enableIgnore)
                        localctx.p = Range(localctx.e1.ex,localctx.e2.ex) 
                        pass

                    elif la_ == 2:
                        localctx.p = Range(localctx.e1.ex,None) 
                        pass


                    pass
                elif token in [SetlXgrammarParser.T__27]:
                    self.state = 500 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    while True:
                        self.state = 496
                        self.match(SetlXgrammarParser.T__27)
                        self.state = 497
                        localctx.e3 = self.expr(False)
                        params.append(localctx.e3.ex) 
                        self.state = 502 
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)
                        if not (_la==SetlXgrammarParser.T__27):
                            break

                    localctx.p = params 
                    pass
                elif token in [SetlXgrammarParser.T__25]:
                    localctx.p = localctx.e1.ex 
                    pass
                else:
                    raise NoViableAltException(self)

                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 509
                self.match(SetlXgrammarParser.RANGE_SIGN)
                self.state = 510
                localctx._expr = self.expr(localctx.enableIgnore)
                localctx.p = Range(None,localctx._expr.ex) 
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
        self.enterRule(localctx, 48, self.RULE_callParameters)

        localctx.params = []
        localctx.ex = None
            
        try:
            self.state = 519
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,37,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 515
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
        self.enterRule(localctx, 50, self.RULE_value)

        cb = None
            
        try:
            self.state = 539
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,39,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 521
                self.match(SetlXgrammarParser.T__24)
                self.state = 525
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,38,self._ctx)
                if la_ == 1:
                    self.state = 522
                    localctx._collectionBuilder = self.collectionBuilder(localctx.enableIgnore)
                    cb = localctx._collectionBuilder.cb; 


                self.state = 527
                self.match(SetlXgrammarParser.T__25)
                localctx.v = SetlXList(cb) 
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 529
                localctx._STRING = self.match(SetlXgrammarParser.STRING)
                localctx.v = SetlXString((None if localctx._STRING is None else localctx._STRING.text)) 
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 531
                localctx._LITERAL = self.match(SetlXgrammarParser.LITERAL)
                localctx.v = SetlXLiteral((None if localctx._LITERAL is None else localctx._LITERAL.text)) 
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 533
                localctx._atomicValue = self.atomicValue()
                localctx.v = localctx._atomicValue.av 
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 536
                if not localctx.enableIgnore:
                    from antlr4.error.Errors import FailedPredicateException
                    raise FailedPredicateException(self, "$enableIgnore")
                self.state = 537
                self.match(SetlXgrammarParser.T__26)
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
        self.enterRule(localctx, 52, self.RULE_collectionBuilder)

        exprs = []
            
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 541
            localctx.e1 = self.expr(localctx.enableIgnore)
            self.state = 588
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [SetlXgrammarParser.T__27]:
                self.state = 542
                self.match(SetlXgrammarParser.T__27)
                self.state = 543
                localctx.e2 = self.expr(localctx.enableIgnore)
                self.state = 565
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [SetlXgrammarParser.RANGE_SIGN]:
                    self.state = 544
                    self.match(SetlXgrammarParser.RANGE_SIGN)
                    self.state = 545
                    localctx.e3 = self.expr(localctx.enableIgnore)
                    localctx.cb = Range(localctx.e1.ex, localctx.e2.ex, localctx.e3.ex) 
                    pass
                elif token in [SetlXgrammarParser.T__7, SetlXgrammarParser.T__25, SetlXgrammarParser.T__27]:
                    exprs.append(localctx.e1.ex); exprs.append(localctx.e2.ex) 
                    self.state = 555
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    while _la==SetlXgrammarParser.T__27:
                        self.state = 549
                        self.match(SetlXgrammarParser.T__27)
                        self.state = 550
                        localctx.e3 = self.expr(localctx.enableIgnore)
                        exprs.append(localctx.e3.ex) 
                        self.state = 557
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)

                    self.state = 563
                    self._errHandler.sync(self)
                    token = self._input.LA(1)
                    if token in [SetlXgrammarParser.T__7]:
                        self.state = 558
                        self.match(SetlXgrammarParser.T__7)
                        self.state = 559
                        localctx.e4 = self.expr(False)
                        localctx.cb = ExplicitListWithRest(exprs, localctx.e4.ex) 
                        pass
                    elif token in [SetlXgrammarParser.T__25]:
                        localctx.cb = ExplicitList(exprs)         
                        pass
                    else:
                        raise NoViableAltException(self)

                    pass
                else:
                    raise NoViableAltException(self)

                pass
            elif token in [SetlXgrammarParser.RANGE_SIGN]:
                self.state = 567
                self.match(SetlXgrammarParser.RANGE_SIGN)
                self.state = 568
                localctx.e3 = self.expr(localctx.enableIgnore)
                localctx.cb = Range(localctx.e1.ex, None, localctx.e3.ex) 
                pass
            elif token in [SetlXgrammarParser.T__7, SetlXgrammarParser.T__25]:
                exprs.append(localctx.e1.ex) 
                self.state = 577
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [SetlXgrammarParser.T__7]:
                    self.state = 572
                    self.match(SetlXgrammarParser.T__7)
                    self.state = 573
                    localctx.e2 = self.expr(False)
                    localctx.cb = ExplicitListWithRest(exprs, localctx.e2.ex) 
                    pass
                elif token in [SetlXgrammarParser.T__25]:
                    localctx.cb = ExplicitList(exprs)         
                    pass
                else:
                    raise NoViableAltException(self)

                pass
            elif token in [SetlXgrammarParser.T__47]:
                self.state = 579
                self.match(SetlXgrammarParser.T__47)
                self.state = 580
                localctx._iteratorChain = self.iteratorChain(localctx.enableIgnore)
                self.state = 586
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [SetlXgrammarParser.T__7]:
                    self.state = 581
                    self.match(SetlXgrammarParser.T__7)
                    self.state = 582
                    localctx.c1 = self.condition()
                    localctx.cb = SetlIteration(localctx.e1.ex, localctx._iteratorChain.ic, localctx.c1.cnd) 
                    pass
                elif token in [SetlXgrammarParser.T__25]:
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
        self.enterRule(localctx, 54, self.RULE_iteratorChain)

        localctx.ic = []
            
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 590
            localctx.i1 = self.iterator(localctx.enableIgnore)
            localctx.ic.append(localctx.i1.iter)
            self.state = 598
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==SetlXgrammarParser.T__27:
                self.state = 592
                self.match(SetlXgrammarParser.T__27)
                self.state = 593
                localctx.i2 = self.iterator(localctx.enableIgnore)
                localctx.ic.append(localctx.i2.iter) 
                self.state = 600
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
        self.enterRule(localctx, 56, self.RULE_iterator)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 601
            localctx._assignable = self.assignable(True)
            self.state = 602
            self.match(SetlXgrammarParser.T__36)
            self.state = 603
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
        self.enterRule(localctx, 58, self.RULE_atomicValue)
        try:
            self.state = 616
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [SetlXgrammarParser.NUMBER]:
                self.enterOuterAlt(localctx, 1)
                self.state = 606
                localctx._NUMBER = self.match(SetlXgrammarParser.NUMBER)
                localctx.av = SetlXFraction((None if localctx._NUMBER is None else localctx._NUMBER.text)) 
                pass
            elif token in [SetlXgrammarParser.DOUBLE]:
                self.enterOuterAlt(localctx, 2)
                self.state = 608
                localctx._DOUBLE = self.match(SetlXgrammarParser.DOUBLE)
                localctx.av = float((None if localctx._DOUBLE is None else localctx._DOUBLE.text)) 
                pass
            elif token in [SetlXgrammarParser.T__48]:
                self.enterOuterAlt(localctx, 3)
                self.state = 610
                self.match(SetlXgrammarParser.T__48)
                localctx.av = SetlXOm() 
                pass
            elif token in [SetlXgrammarParser.T__49]:
                self.enterOuterAlt(localctx, 4)
                self.state = 612
                self.match(SetlXgrammarParser.T__49)
                localctx.av = SetlXTrue() 
                pass
            elif token in [SetlXgrammarParser.T__50]:
                self.enterOuterAlt(localctx, 5)
                self.state = 614
                self.match(SetlXgrammarParser.T__50)
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
        self.enterRule(localctx, 60, self.RULE_variable)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 618
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
        self.enterRule(localctx, 62, self.RULE_condition)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 621
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
        self.enterRule(localctx, 64, self.RULE_assignmentList)

        localctx.al = []
            
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 624
            localctx.a1 = self.assignable(True)
            localctx.al.append(localctx.a1.a) 
            self.state = 632
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==SetlXgrammarParser.T__27:
                self.state = 626
                self.match(SetlXgrammarParser.T__27)
                self.state = 627
                localctx.a2 = self.assignable(True)
                localctx.al.append(localctx.a2.a) 
                self.state = 634
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
        self._predicates[25] = self.value_sempred
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
         




