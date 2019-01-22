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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3=")
        buf.write("\u0218\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31")
        buf.write("\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36")
        buf.write("\4\37\t\37\4 \t \3\2\3\2\3\2\7\2D\n\2\f\2\16\2G\13\2\3")
        buf.write("\2\3\2\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3")
        buf.write("\3\3\3\3\3\3\3\3\3\3\3\3\7\3]\n\3\f\3\16\3`\13\3\3\3\3")
        buf.write("\3\3\3\3\3\3\3\3\3\5\3h\n\3\3\3\3\3\3\3\3\3\3\3\3\3\3")
        buf.write("\3\3\3\3\3\5\3s\n\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3")
        buf.write("\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3")
        buf.write("\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3")
        buf.write("\3\3\3\3\3\3\3\3\3\3\3\3\3\5\3\u009f\n\3\3\3\3\3\3\3\3")
        buf.write("\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\5\3\u00af\n")
        buf.write("\3\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4")
        buf.write("\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\5\4\u00ca")
        buf.write("\n\4\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\5\5\u00d4\n\5\3\6")
        buf.write("\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\7\6\u00e1\n\6")
        buf.write("\f\6\16\6\u00e4\13\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\5")
        buf.write("\6\u00ee\n\6\3\7\3\7\3\7\3\b\3\b\3\b\3\t\3\t\3\t\3\t\3")
        buf.write("\t\3\t\7\t\u00fc\n\t\f\t\16\t\u00ff\13\t\3\n\3\n\3\n\3")
        buf.write("\13\3\13\3\13\3\f\3\f\3\f\3\f\3\f\3\f\7\f\u010d\n\f\f")
        buf.write("\f\16\f\u0110\13\f\3\r\3\r\3\r\3\r\3\r\3\r\7\r\u0118\n")
        buf.write("\r\f\r\16\r\u011b\13\r\3\16\3\16\3\16\3\16\3\16\3\16\3")
        buf.write("\16\3\16\3\16\3\16\3\16\3\16\3\16\3\16\3\16\3\16\3\16")
        buf.write("\3\16\3\16\3\16\3\16\3\16\3\16\3\16\3\16\3\16\3\16\3\16")
        buf.write("\3\16\3\16\3\16\3\16\3\16\3\16\5\16\u013f\n\16\3\17\3")
        buf.write("\17\3\17\3\17\3\17\3\17\3\17\3\17\3\17\3\17\7\17\u014b")
        buf.write("\n\17\f\17\16\17\u014e\13\17\3\20\3\20\3\20\3\20\3\20")
        buf.write("\3\20\3\20\3\20\3\20\3\20\3\20\3\20\3\20\3\20\3\20\3\20")
        buf.write("\3\20\3\20\7\20\u0162\n\20\f\20\16\20\u0165\13\20\3\21")
        buf.write("\3\21\3\21\3\22\3\22\3\22\3\22\3\22\3\22\5\22\u0170\n")
        buf.write("\22\3\22\3\22\3\22\3\22\5\22\u0176\n\22\3\23\3\23\3\23")
        buf.write("\3\23\3\23\3\23\3\23\3\23\3\23\3\23\3\23\3\23\3\23\3\23")
        buf.write("\3\23\5\23\u0187\n\23\3\23\3\23\3\23\3\23\3\23\3\23\3")
        buf.write("\23\7\23\u0190\n\23\f\23\16\23\u0193\13\23\3\23\3\23\5")
        buf.write("\23\u0197\n\23\3\23\3\23\3\23\3\23\5\23\u019d\n\23\5\23")
        buf.write("\u019f\n\23\3\24\3\24\3\24\3\24\3\24\3\24\3\24\3\24\3")
        buf.write("\24\3\25\3\25\3\25\3\25\3\25\3\25\7\25\u01b0\n\25\f\25")
        buf.write("\16\25\u01b3\13\25\3\25\3\25\3\25\3\25\7\25\u01b9\n\25")
        buf.write("\f\25\16\25\u01bc\13\25\3\25\3\25\3\25\3\25\3\25\3\25")
        buf.write("\7\25\u01c4\n\25\f\25\16\25\u01c7\13\25\3\25\5\25\u01ca")
        buf.write("\n\25\3\26\3\26\3\26\3\27\3\27\3\27\3\27\3\27\3\30\3\30")
        buf.write("\3\30\3\30\3\30\3\31\3\31\3\31\3\31\5\31\u01dd\n\31\3")
        buf.write("\32\3\32\3\32\3\32\3\32\3\32\3\32\3\32\3\32\3\32\5\32")
        buf.write("\u01e9\n\32\3\33\3\33\3\33\3\33\3\33\3\33\7\33\u01f1\n")
        buf.write("\33\f\33\16\33\u01f4\13\33\3\34\3\34\3\34\3\34\3\34\3")
        buf.write("\35\3\35\3\35\3\35\3\35\3\35\3\35\3\35\3\35\3\35\5\35")
        buf.write("\u0205\n\35\3\36\3\36\3\36\3\37\3\37\3\37\3 \3 \3 \3 ")
        buf.write("\3 \3 \7 \u0213\n \f \16 \u0216\13 \3 \2\2!\2\4\6\b\n")
        buf.write("\f\16\20\22\24\26\30\32\34\36 \"$&(*,.\60\62\64\668:<")
        buf.write(">\2\2\2\u023c\2E\3\2\2\2\4\u00ae\3\2\2\2\6\u00b0\3\2\2")
        buf.write("\2\b\u00cb\3\2\2\2\n\u00ed\3\2\2\2\f\u00ef\3\2\2\2\16")
        buf.write("\u00f2\3\2\2\2\20\u00f5\3\2\2\2\22\u0100\3\2\2\2\24\u0103")
        buf.write("\3\2\2\2\26\u0106\3\2\2\2\30\u0111\3\2\2\2\32\u011c\3")
        buf.write("\2\2\2\34\u0140\3\2\2\2\36\u014f\3\2\2\2 \u0166\3\2\2")
        buf.write("\2\"\u0175\3\2\2\2$\u019e\3\2\2\2&\u01a0\3\2\2\2(\u01c9")
        buf.write("\3\2\2\2*\u01cb\3\2\2\2,\u01ce\3\2\2\2.\u01d3\3\2\2\2")
        buf.write("\60\u01dc\3\2\2\2\62\u01e8\3\2\2\2\64\u01ea\3\2\2\2\66")
        buf.write("\u01f5\3\2\2\28\u0204\3\2\2\2:\u0206\3\2\2\2<\u0209\3")
        buf.write("\2\2\2>\u020c\3\2\2\2@A\5\4\3\2AB\b\2\1\2BD\3\2\2\2C@")
        buf.write("\3\2\2\2DG\3\2\2\2EC\3\2\2\2EF\3\2\2\2FH\3\2\2\2GE\3\2")
        buf.write("\2\2HI\b\2\1\2I\3\3\2\2\2JK\7\3\2\2KL\7\4\2\2LM\5<\37")
        buf.write("\2MN\7\5\2\2NO\7\6\2\2OP\5\2\2\2PQ\7\7\2\2Q^\b\3\1\2R")
        buf.write("S\7\b\2\2ST\7\3\2\2TU\7\4\2\2UV\5<\37\2VW\7\5\2\2WX\7")
        buf.write("\6\2\2XY\5\2\2\2YZ\7\7\2\2Z[\b\3\1\2[]\3\2\2\2\\R\3\2")
        buf.write("\2\2]`\3\2\2\2^\\\3\2\2\2^_\3\2\2\2_g\3\2\2\2`^\3\2\2")
        buf.write("\2ab\7\b\2\2bc\7\6\2\2cd\5\2\2\2de\7\7\2\2ef\b\3\1\2f")
        buf.write("h\3\2\2\2ga\3\2\2\2gh\3\2\2\2hi\3\2\2\2ij\b\3\1\2j\u00af")
        buf.write("\3\2\2\2kl\7\t\2\2lm\7\4\2\2mr\5\64\33\2no\7\n\2\2op\5")
        buf.write("<\37\2pq\b\3\1\2qs\3\2\2\2rn\3\2\2\2rs\3\2\2\2st\3\2\2")
        buf.write("\2tu\7\5\2\2uv\7\6\2\2vw\5\2\2\2wx\7\7\2\2xy\b\3\1\2y")
        buf.write("\u00af\3\2\2\2z{\7\13\2\2{|\7\4\2\2|}\5<\37\2}~\7\5\2")
        buf.write("\2~\177\7\6\2\2\177\u0080\5\2\2\2\u0080\u0081\7\7\2\2")
        buf.write("\u0081\u0082\b\3\1\2\u0082\u00af\3\2\2\2\u0083\u0084\7")
        buf.write("\f\2\2\u0084\u0085\7\6\2\2\u0085\u0086\5\2\2\2\u0086\u0087")
        buf.write("\7\7\2\2\u0087\u0088\7\13\2\2\u0088\u0089\7\4\2\2\u0089")
        buf.write("\u008a\5<\37\2\u008a\u008b\7\5\2\2\u008b\u008c\7\r\2\2")
        buf.write("\u008c\u008d\b\3\1\2\u008d\u00af\3\2\2\2\u008e\u008f\7")
        buf.write("\16\2\2\u008f\u0090\7\r\2\2\u0090\u00af\b\3\1\2\u0091")
        buf.write("\u0092\7\17\2\2\u0092\u0093\7\r\2\2\u0093\u00af\b\3\1")
        buf.write("\2\u0094\u0095\7\20\2\2\u0095\u0096\7\r\2\2\u0096\u00af")
        buf.write("\b\3\1\2\u0097\u0098\7\21\2\2\u0098\u0099\7\r\2\2\u0099")
        buf.write("\u00af\b\3\1\2\u009a\u009e\7\22\2\2\u009b\u009c\5\16\b")
        buf.write("\2\u009c\u009d\b\3\1\2\u009d\u009f\3\2\2\2\u009e\u009b")
        buf.write("\3\2\2\2\u009e\u009f\3\2\2\2\u009f\u00a0\3\2\2\2\u00a0")
        buf.write("\u00a1\7\r\2\2\u00a1\u00af\b\3\1\2\u00a2\u00a3\5\6\4\2")
        buf.write("\u00a3\u00a4\7\r\2\2\u00a4\u00a5\b\3\1\2\u00a5\u00af\3")
        buf.write("\2\2\2\u00a6\u00a7\5\b\5\2\u00a7\u00a8\7\r\2\2\u00a8\u00a9")
        buf.write("\b\3\1\2\u00a9\u00af\3\2\2\2\u00aa\u00ab\5\16\b\2\u00ab")
        buf.write("\u00ac\7\r\2\2\u00ac\u00ad\b\3\1\2\u00ad\u00af\3\2\2\2")
        buf.write("\u00aeJ\3\2\2\2\u00aek\3\2\2\2\u00aez\3\2\2\2\u00ae\u0083")
        buf.write("\3\2\2\2\u00ae\u008e\3\2\2\2\u00ae\u0091\3\2\2\2\u00ae")
        buf.write("\u0094\3\2\2\2\u00ae\u0097\3\2\2\2\u00ae\u009a\3\2\2\2")
        buf.write("\u00ae\u00a2\3\2\2\2\u00ae\u00a6\3\2\2\2\u00ae\u00aa\3")
        buf.write("\2\2\2\u00af\5\3\2\2\2\u00b0\u00c9\5\n\6\2\u00b1\u00b2")
        buf.write("\7\23\2\2\u00b2\u00b3\5\16\b\2\u00b3\u00b4\b\4\1\2\u00b4")
        buf.write("\u00ca\3\2\2\2\u00b5\u00b6\7\24\2\2\u00b6\u00b7\5\16\b")
        buf.write("\2\u00b7\u00b8\b\4\1\2\u00b8\u00ca\3\2\2\2\u00b9\u00ba")
        buf.write("\7\25\2\2\u00ba\u00bb\5\16\b\2\u00bb\u00bc\b\4\1\2\u00bc")
        buf.write("\u00ca\3\2\2\2\u00bd\u00be\7\26\2\2\u00be\u00bf\5\16\b")
        buf.write("\2\u00bf\u00c0\b\4\1\2\u00c0\u00ca\3\2\2\2\u00c1\u00c2")
        buf.write("\7\27\2\2\u00c2\u00c3\5\16\b\2\u00c3\u00c4\b\4\1\2\u00c4")
        buf.write("\u00ca\3\2\2\2\u00c5\u00c6\7\30\2\2\u00c6\u00c7\5\16\b")
        buf.write("\2\u00c7\u00c8\b\4\1\2\u00c8\u00ca\3\2\2\2\u00c9\u00b1")
        buf.write("\3\2\2\2\u00c9\u00b5\3\2\2\2\u00c9\u00b9\3\2\2\2\u00c9")
        buf.write("\u00bd\3\2\2\2\u00c9\u00c1\3\2\2\2\u00c9\u00c5\3\2\2\2")
        buf.write("\u00ca\7\3\2\2\2\u00cb\u00cc\5\n\6\2\u00cc\u00d3\7\31")
        buf.write("\2\2\u00cd\u00ce\5\b\5\2\u00ce\u00cf\b\5\1\2\u00cf\u00d4")
        buf.write("\3\2\2\2\u00d0\u00d1\5\22\n\2\u00d1\u00d2\b\5\1\2\u00d2")
        buf.write("\u00d4\3\2\2\2\u00d3\u00cd\3\2\2\2\u00d3\u00d0\3\2\2\2")
        buf.write("\u00d4\t\3\2\2\2\u00d5\u00d6\5\f\7\2\u00d6\u00e2\b\6\1")
        buf.write("\2\u00d7\u00d8\7\32\2\2\u00d8\u00d9\5:\36\2\u00d9\u00da")
        buf.write("\b\6\1\2\u00da\u00e1\3\2\2\2\u00db\u00dc\7\33\2\2\u00dc")
        buf.write("\u00dd\5\20\t\2\u00dd\u00de\7\34\2\2\u00de\u00df\b\6\1")
        buf.write("\2\u00df\u00e1\3\2\2\2\u00e0\u00d7\3\2\2\2\u00e0\u00db")
        buf.write("\3\2\2\2\u00e1\u00e4\3\2\2\2\u00e2\u00e0\3\2\2\2\u00e2")
        buf.write("\u00e3\3\2\2\2\u00e3\u00ee\3\2\2\2\u00e4\u00e2\3\2\2\2")
        buf.write("\u00e5\u00e6\7\33\2\2\u00e6\u00e7\5> \2\u00e7\u00e8\7")
        buf.write("\34\2\2\u00e8\u00e9\b\6\1\2\u00e9\u00ee\3\2\2\2\u00ea")
        buf.write("\u00eb\6\6\2\3\u00eb\u00ec\7\35\2\2\u00ec\u00ee\b\6\1")
        buf.write("\2\u00ed\u00d5\3\2\2\2\u00ed\u00e5\3\2\2\2\u00ed\u00ea")
        buf.write("\3\2\2\2\u00ee\13\3\2\2\2\u00ef\u00f0\7\65\2\2\u00f0\u00f1")
        buf.write("\b\7\1\2\u00f1\r\3\2\2\2\u00f2\u00f3\5\22\n\2\u00f3\u00f4")
        buf.write("\b\b\1\2\u00f4\17\3\2\2\2\u00f5\u00f6\5\22\n\2\u00f6\u00fd")
        buf.write("\b\t\1\2\u00f7\u00f8\7\36\2\2\u00f8\u00f9\5\22\n\2\u00f9")
        buf.write("\u00fa\b\t\1\2\u00fa\u00fc\3\2\2\2\u00fb\u00f7\3\2\2\2")
        buf.write("\u00fc\u00ff\3\2\2\2\u00fd\u00fb\3\2\2\2\u00fd\u00fe\3")
        buf.write("\2\2\2\u00fe\21\3\2\2\2\u00ff\u00fd\3\2\2\2\u0100\u0101")
        buf.write("\5\24\13\2\u0101\u0102\b\n\1\2\u0102\23\3\2\2\2\u0103")
        buf.write("\u0104\5\26\f\2\u0104\u0105\b\13\1\2\u0105\25\3\2\2\2")
        buf.write("\u0106\u0107\5\30\r\2\u0107\u010e\b\f\1\2\u0108\u0109")
        buf.write("\7\37\2\2\u0109\u010a\5\30\r\2\u010a\u010b\b\f\1\2\u010b")
        buf.write("\u010d\3\2\2\2\u010c\u0108\3\2\2\2\u010d\u0110\3\2\2\2")
        buf.write("\u010e\u010c\3\2\2\2\u010e\u010f\3\2\2\2\u010f\27\3\2")
        buf.write("\2\2\u0110\u010e\3\2\2\2\u0111\u0112\5\32\16\2\u0112\u0119")
        buf.write("\b\r\1\2\u0113\u0114\7 \2\2\u0114\u0115\5\32\16\2\u0115")
        buf.write("\u0116\b\r\1\2\u0116\u0118\3\2\2\2\u0117\u0113\3\2\2\2")
        buf.write("\u0118\u011b\3\2\2\2\u0119\u0117\3\2\2\2\u0119\u011a\3")
        buf.write("\2\2\2\u011a\31\3\2\2\2\u011b\u0119\3\2\2\2\u011c\u011d")
        buf.write("\5\34\17\2\u011d\u013e\b\16\1\2\u011e\u011f\7!\2\2\u011f")
        buf.write("\u0120\5\34\17\2\u0120\u0121\b\16\1\2\u0121\u013f\3\2")
        buf.write("\2\2\u0122\u0123\7\"\2\2\u0123\u0124\5\34\17\2\u0124\u0125")
        buf.write("\b\16\1\2\u0125\u013f\3\2\2\2\u0126\u0127\7#\2\2\u0127")
        buf.write("\u0128\5\34\17\2\u0128\u0129\b\16\1\2\u0129\u013f\3\2")
        buf.write("\2\2\u012a\u012b\7$\2\2\u012b\u012c\5\34\17\2\u012c\u012d")
        buf.write("\b\16\1\2\u012d\u013f\3\2\2\2\u012e\u012f\7%\2\2\u012f")
        buf.write("\u0130\5\34\17\2\u0130\u0131\b\16\1\2\u0131\u013f\3\2")
        buf.write("\2\2\u0132\u0133\7&\2\2\u0133\u0134\5\34\17\2\u0134\u0135")
        buf.write("\b\16\1\2\u0135\u013f\3\2\2\2\u0136\u0137\7\'\2\2\u0137")
        buf.write("\u0138\5\34\17\2\u0138\u0139\b\16\1\2\u0139\u013f\3\2")
        buf.write("\2\2\u013a\u013b\7(\2\2\u013b\u013c\5\34\17\2\u013c\u013d")
        buf.write("\b\16\1\2\u013d\u013f\3\2\2\2\u013e\u011e\3\2\2\2\u013e")
        buf.write("\u0122\3\2\2\2\u013e\u0126\3\2\2\2\u013e\u012a\3\2\2\2")
        buf.write("\u013e\u012e\3\2\2\2\u013e\u0132\3\2\2\2\u013e\u0136\3")
        buf.write("\2\2\2\u013e\u013a\3\2\2\2\u013e\u013f\3\2\2\2\u013f\33")
        buf.write("\3\2\2\2\u0140\u0141\5\36\20\2\u0141\u014c\b\17\1\2\u0142")
        buf.write("\u0143\7)\2\2\u0143\u0144\5\36\20\2\u0144\u0145\b\17\1")
        buf.write("\2\u0145\u014b\3\2\2\2\u0146\u0147\7*\2\2\u0147\u0148")
        buf.write("\5\36\20\2\u0148\u0149\b\17\1\2\u0149\u014b\3\2\2\2\u014a")
        buf.write("\u0142\3\2\2\2\u014a\u0146\3\2\2\2\u014b\u014e\3\2\2\2")
        buf.write("\u014c\u014a\3\2\2\2\u014c\u014d\3\2\2\2\u014d\35\3\2")
        buf.write("\2\2\u014e\u014c\3\2\2\2\u014f\u0150\5 \21\2\u0150\u0163")
        buf.write("\b\20\1\2\u0151\u0152\7+\2\2\u0152\u0153\5 \21\2\u0153")
        buf.write("\u0154\b\20\1\2\u0154\u0162\3\2\2\2\u0155\u0156\7,\2\2")
        buf.write("\u0156\u0157\5 \21\2\u0157\u0158\b\20\1\2\u0158\u0162")
        buf.write("\3\2\2\2\u0159\u015a\7-\2\2\u015a\u015b\5 \21\2\u015b")
        buf.write("\u015c\b\20\1\2\u015c\u0162\3\2\2\2\u015d\u015e\7.\2\2")
        buf.write("\u015e\u015f\5 \21\2\u015f\u0160\b\20\1\2\u0160\u0162")
        buf.write("\3\2\2\2\u0161\u0151\3\2\2\2\u0161\u0155\3\2\2\2\u0161")
        buf.write("\u0159\3\2\2\2\u0161\u015d\3\2\2\2\u0162\u0165\3\2\2\2")
        buf.write("\u0163\u0161\3\2\2\2\u0163\u0164\3\2\2\2\u0164\37\3\2")
        buf.write("\2\2\u0165\u0163\3\2\2\2\u0166\u0167\5\"\22\2\u0167\u0168")
        buf.write("\b\21\1\2\u0168!\3\2\2\2\u0169\u016a\5$\23\2\u016a\u016f")
        buf.write("\b\22\1\2\u016b\u016c\7/\2\2\u016c\u016d\5\"\22\2\u016d")
        buf.write("\u016e\b\22\1\2\u016e\u0170\3\2\2\2\u016f\u016b\3\2\2")
        buf.write("\2\u016f\u0170\3\2\2\2\u0170\u0176\3\2\2\2\u0171\u0172")
        buf.write("\7*\2\2\u0172\u0173\5\"\22\2\u0173\u0174\b\22\1\2\u0174")
        buf.write("\u0176\3\2\2\2\u0175\u0169\3\2\2\2\u0175\u0171\3\2\2\2")
        buf.write("\u0176#\3\2\2\2\u0177\u0178\7\60\2\2\u0178\u0179\5$\23")
        buf.write("\2\u0179\u017a\b\23\1\2\u017a\u019f\3\2\2\2\u017b\u017c")
        buf.write("\7\4\2\2\u017c\u017d\5\22\n\2\u017d\u017e\7\5\2\2\u017e")
        buf.write("\u017f\b\23\1\2\u017f\u0187\3\2\2\2\u0180\u0181\5&\24")
        buf.write("\2\u0181\u0182\b\23\1\2\u0182\u0187\3\2\2\2\u0183\u0184")
        buf.write("\5:\36\2\u0184\u0185\b\23\1\2\u0185\u0187\3\2\2\2\u0186")
        buf.write("\u017b\3\2\2\2\u0186\u0180\3\2\2\2\u0186\u0183\3\2\2\2")
        buf.write("\u0187\u0191\3\2\2\2\u0188\u0189\7\32\2\2\u0189\u018a")
        buf.write("\5:\36\2\u018a\u018b\b\23\1\2\u018b\u0190\3\2\2\2\u018c")
        buf.write("\u018d\5.\30\2\u018d\u018e\b\23\1\2\u018e\u0190\3\2\2")
        buf.write("\2\u018f\u0188\3\2\2\2\u018f\u018c\3\2\2\2\u0190\u0193")
        buf.write("\3\2\2\2\u0191\u018f\3\2\2\2\u0191\u0192\3\2\2\2\u0192")
        buf.write("\u0196\3\2\2\2\u0193\u0191\3\2\2\2\u0194\u0195\7\60\2")
        buf.write("\2\u0195\u0197\b\23\1\2\u0196\u0194\3\2\2\2\u0196\u0197")
        buf.write("\3\2\2\2\u0197\u019f\3\2\2\2\u0198\u0199\5\62\32\2\u0199")
        buf.write("\u019c\b\23\1\2\u019a\u019b\7\60\2\2\u019b\u019d\b\23")
        buf.write("\1\2\u019c\u019a\3\2\2\2\u019c\u019d\3\2\2\2\u019d\u019f")
        buf.write("\3\2\2\2\u019e\u0177\3\2\2\2\u019e\u0186\3\2\2\2\u019e")
        buf.write("\u0198\3\2\2\2\u019f%\3\2\2\2\u01a0\u01a1\7\61\2\2\u01a1")
        buf.write("\u01a2\7\4\2\2\u01a2\u01a3\5(\25\2\u01a3\u01a4\7\5\2\2")
        buf.write("\u01a4\u01a5\7\6\2\2\u01a5\u01a6\5\2\2\2\u01a6\u01a7\7")
        buf.write("\7\2\2\u01a7\u01a8\b\24\1\2\u01a8\'\3\2\2\2\u01a9\u01aa")
        buf.write("\5*\26\2\u01aa\u01b1\b\25\1\2\u01ab\u01ac\7\36\2\2\u01ac")
        buf.write("\u01ad\5*\26\2\u01ad\u01ae\b\25\1\2\u01ae\u01b0\3\2\2")
        buf.write("\2\u01af\u01ab\3\2\2\2\u01b0\u01b3\3\2\2\2\u01b1\u01af")
        buf.write("\3\2\2\2\u01b1\u01b2\3\2\2\2\u01b2\u01ba\3\2\2\2\u01b3")
        buf.write("\u01b1\3\2\2\2\u01b4\u01b5\7\36\2\2\u01b5\u01b6\5,\27")
        buf.write("\2\u01b6\u01b7\b\25\1\2\u01b7\u01b9\3\2\2\2\u01b8\u01b4")
        buf.write("\3\2\2\2\u01b9\u01bc\3\2\2\2\u01ba\u01b8\3\2\2\2\u01ba")
        buf.write("\u01bb\3\2\2\2\u01bb\u01ca\3\2\2\2\u01bc\u01ba\3\2\2\2")
        buf.write("\u01bd\u01be\5,\27\2\u01be\u01c5\b\25\1\2\u01bf\u01c0")
        buf.write("\7\36\2\2\u01c0\u01c1\5,\27\2\u01c1\u01c2\b\25\1\2\u01c2")
        buf.write("\u01c4\3\2\2\2\u01c3\u01bf\3\2\2\2\u01c4\u01c7\3\2\2\2")
        buf.write("\u01c5\u01c3\3\2\2\2\u01c5\u01c6\3\2\2\2\u01c6\u01ca\3")
        buf.write("\2\2\2\u01c7\u01c5\3\2\2\2\u01c8\u01ca\3\2\2\2\u01c9\u01a9")
        buf.write("\3\2\2\2\u01c9\u01bd\3\2\2\2\u01c9\u01c8\3\2\2\2\u01ca")
        buf.write(")\3\2\2\2\u01cb\u01cc\5:\36\2\u01cc\u01cd\b\26\1\2\u01cd")
        buf.write("+\3\2\2\2\u01ce\u01cf\5\f\7\2\u01cf\u01d0\7\31\2\2\u01d0")
        buf.write("\u01d1\5\16\b\2\u01d1\u01d2\b\27\1\2\u01d2-\3\2\2\2\u01d3")
        buf.write("\u01d4\7\4\2\2\u01d4\u01d5\5\60\31\2\u01d5\u01d6\7\5\2")
        buf.write("\2\u01d6\u01d7\b\30\1\2\u01d7/\3\2\2\2\u01d8\u01d9\5\20")
        buf.write("\t\2\u01d9\u01da\b\31\1\2\u01da\u01dd\3\2\2\2\u01db\u01dd")
        buf.write("\3\2\2\2\u01dc\u01d8\3\2\2\2\u01dc\u01db\3\2\2\2\u01dd")
        buf.write("\61\3\2\2\2\u01de\u01df\79\2\2\u01df\u01e9\b\32\1\2\u01e0")
        buf.write("\u01e1\7:\2\2\u01e1\u01e9\b\32\1\2\u01e2\u01e3\58\35\2")
        buf.write("\u01e3\u01e4\b\32\1\2\u01e4\u01e9\3\2\2\2\u01e5\u01e6")
        buf.write("\6\32\3\3\u01e6\u01e7\7\35\2\2\u01e7\u01e9\b\32\1\2\u01e8")
        buf.write("\u01de\3\2\2\2\u01e8\u01e0\3\2\2\2\u01e8\u01e2\3\2\2\2")
        buf.write("\u01e8\u01e5\3\2\2\2\u01e9\63\3\2\2\2\u01ea\u01eb\5\66")
        buf.write("\34\2\u01eb\u01f2\b\33\1\2\u01ec\u01ed\7\36\2\2\u01ed")
        buf.write("\u01ee\5\66\34\2\u01ee\u01ef\b\33\1\2\u01ef\u01f1\3\2")
        buf.write("\2\2\u01f0\u01ec\3\2\2\2\u01f1\u01f4\3\2\2\2\u01f2\u01f0")
        buf.write("\3\2\2\2\u01f2\u01f3\3\2\2\2\u01f3\65\3\2\2\2\u01f4\u01f2")
        buf.write("\3\2\2\2\u01f5\u01f6\5\n\6\2\u01f6\u01f7\7\'\2\2\u01f7")
        buf.write("\u01f8\5\16\b\2\u01f8\u01f9\b\34\1\2\u01f9\67\3\2\2\2")
        buf.write("\u01fa\u01fb\7\66\2\2\u01fb\u0205\b\35\1\2\u01fc\u01fd")
        buf.write("\7\67\2\2\u01fd\u0205\b\35\1\2\u01fe\u01ff\7\62\2\2\u01ff")
        buf.write("\u0205\b\35\1\2\u0200\u0201\7\63\2\2\u0201\u0205\b\35")
        buf.write("\1\2\u0202\u0203\7\64\2\2\u0203\u0205\b\35\1\2\u0204\u01fa")
        buf.write("\3\2\2\2\u0204\u01fc\3\2\2\2\u0204\u01fe\3\2\2\2\u0204")
        buf.write("\u0200\3\2\2\2\u0204\u0202\3\2\2\2\u02059\3\2\2\2\u0206")
        buf.write("\u0207\7\65\2\2\u0207\u0208\b\36\1\2\u0208;\3\2\2\2\u0209")
        buf.write("\u020a\5\16\b\2\u020a\u020b\b\37\1\2\u020b=\3\2\2\2\u020c")
        buf.write("\u020d\5\n\6\2\u020d\u0214\b \1\2\u020e\u020f\7\36\2\2")
        buf.write("\u020f\u0210\5\n\6\2\u0210\u0211\b \1\2\u0211\u0213\3")
        buf.write("\2\2\2\u0212\u020e\3\2\2\2\u0213\u0216\3\2\2\2\u0214\u0212")
        buf.write("\3\2\2\2\u0214\u0215\3\2\2\2\u0215?\3\2\2\2\u0216\u0214")
        buf.write("\3\2\2\2&E^gr\u009e\u00ae\u00c9\u00d3\u00e0\u00e2\u00ed")
        buf.write("\u00fd\u010e\u0119\u013e\u014a\u014c\u0161\u0163\u016f")
        buf.write("\u0175\u0186\u018f\u0191\u0196\u019c\u019e\u01b1\u01ba")
        buf.write("\u01c5\u01c9\u01dc\u01e8\u01f2\u0204\u0214")
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
                     "'!'", "'procedure'", "'om'", "'True'", "'False'", 
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
                      "<INVALID>", "<INVALID>", "<INVALID>", "ID", "NUMBER", 
                      "DOUBLE", "RANGE_SIGN", "STRING", "LITERAL", "LINE_COMMENT", 
                      "MULTI_COMMENT", "WS" ]

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
    RULE_callParameters = 23
    RULE_value = 24
    RULE_iteratorChain = 25
    RULE_iterator = 26
    RULE_atomicValue = 27
    RULE_variable = 28
    RULE_condition = 29
    RULE_assignmentList = 30

    ruleNames =  [ "block", "statement", "assignmentOther", "assignmentDirect", 
                   "assignable", "assignableVariable", "expr", "exprList", 
                   "exprContent", "implication", "disjunction", "conjunction", 
                   "comparison", "setlxSum", "product", "setlxReduce", "prefixOperation", 
                   "factor", "procedure", "procedureParameters", "procedureParameter", 
                   "procedureDefaultParameter", "call", "callParameters", 
                   "value", "iteratorChain", "iterator", "atomicValue", 
                   "variable", "condition", "assignmentList" ]

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
    ID=51
    NUMBER=52
    DOUBLE=53
    RANGE_SIGN=54
    STRING=55
    LITERAL=56
    LINE_COMMENT=57
    MULTI_COMMENT=58
    WS=59

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
            self.state = 67
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,0,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 62
                    localctx._statement = self.statement()
                    stmnts.append(localctx._statement.stmnt) 
                self.state = 69
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
            self.state = 172
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 72
                self.match(SetlXgrammarParser.T__0)
                self.state = 73
                self.match(SetlXgrammarParser.T__1)
                self.state = 74
                localctx.c1 = self.condition()
                self.state = 75
                self.match(SetlXgrammarParser.T__2)
                self.state = 76
                self.match(SetlXgrammarParser.T__3)
                self.state = 77
                localctx.b1 = self.block()
                self.state = 78
                self.match(SetlXgrammarParser.T__4)
                ifList.append(IfThenBranch(localctx.c1.cnd, localctx.b1.blk)) 
                self.state = 92
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,1,self._ctx)
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1:
                        self.state = 80
                        self.match(SetlXgrammarParser.T__5)
                        self.state = 81
                        self.match(SetlXgrammarParser.T__0)
                        self.state = 82
                        self.match(SetlXgrammarParser.T__1)
                        self.state = 83
                        localctx.c2 = self.condition()
                        self.state = 84
                        self.match(SetlXgrammarParser.T__2)
                        self.state = 85
                        self.match(SetlXgrammarParser.T__3)
                        self.state = 86
                        localctx.b2 = self.block()
                        self.state = 87
                        self.match(SetlXgrammarParser.T__4)
                        ifList.append(IfThenElseIfBranch(localctx.c2.cnd, localctx.b2.blk))  
                    self.state = 94
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,1,self._ctx)

                self.state = 101
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
                if la_ == 1:
                    self.state = 95
                    self.match(SetlXgrammarParser.T__5)
                    self.state = 96
                    self.match(SetlXgrammarParser.T__3)
                    self.state = 97
                    localctx.b3 = self.block()
                    self.state = 98
                    self.match(SetlXgrammarParser.T__4)
                    ifList.append(IfThenElseBranch(localctx.b3.blk))                  


                localctx.stmnt = IfThen(ifList) 
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 105
                self.match(SetlXgrammarParser.T__6)
                self.state = 106
                self.match(SetlXgrammarParser.T__1)
                self.state = 107
                localctx._iteratorChain = self.iteratorChain(False)
                self.state = 112
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==SetlXgrammarParser.T__7:
                    self.state = 108
                    self.match(SetlXgrammarParser.T__7)
                    self.state = 109
                    localctx._condition = self.condition()
                    condition = localctx._condition.cnd


                self.state = 114
                self.match(SetlXgrammarParser.T__2)
                self.state = 115
                self.match(SetlXgrammarParser.T__3)
                self.state = 116
                localctx._block = self.block()
                self.state = 117
                self.match(SetlXgrammarParser.T__4)
                localctx.stmnt = For(localctx._iteratorChain.ic, condition, localctx._block.blk) 
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 120
                self.match(SetlXgrammarParser.T__8)
                self.state = 121
                self.match(SetlXgrammarParser.T__1)
                self.state = 122
                localctx._condition = self.condition()
                self.state = 123
                self.match(SetlXgrammarParser.T__2)
                self.state = 124
                self.match(SetlXgrammarParser.T__3)
                self.state = 125
                localctx._block = self.block()
                self.state = 126
                self.match(SetlXgrammarParser.T__4)
                localctx.stmnt = While(localctx._condition.cnd, localctx._block.blk) 
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 129
                self.match(SetlXgrammarParser.T__9)
                self.state = 130
                self.match(SetlXgrammarParser.T__3)
                self.state = 131
                localctx._block = self.block()
                self.state = 132
                self.match(SetlXgrammarParser.T__4)
                self.state = 133
                self.match(SetlXgrammarParser.T__8)
                self.state = 134
                self.match(SetlXgrammarParser.T__1)
                self.state = 135
                localctx._condition = self.condition()
                self.state = 136
                self.match(SetlXgrammarParser.T__2)
                self.state = 137
                self.match(SetlXgrammarParser.T__10)
                localctx.stmnt = DoWhile(localctx._condition.cnd, localctx._block.blk) 
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 140
                self.match(SetlXgrammarParser.T__11)
                self.state = 141
                self.match(SetlXgrammarParser.T__10)
                localctx.stmnt = Backtrack() 
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 143
                self.match(SetlXgrammarParser.T__12)
                self.state = 144
                self.match(SetlXgrammarParser.T__10)
                localctx.stmnt = Break() 
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 146
                self.match(SetlXgrammarParser.T__13)
                self.state = 147
                self.match(SetlXgrammarParser.T__10)
                localctx.stmnt = Continue() 
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 149
                self.match(SetlXgrammarParser.T__14)
                self.state = 150
                self.match(SetlXgrammarParser.T__10)
                localctx.stmnt = Exit() 
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 152
                self.match(SetlXgrammarParser.T__15)
                self.state = 156
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
                if la_ == 1:
                    self.state = 153
                    localctx._expr = self.expr(False)
                    expression = localctx._expr.ex 


                self.state = 158
                self.match(SetlXgrammarParser.T__10)
                localctx.stmnt = Return(expression) 
                pass

            elif la_ == 10:
                self.enterOuterAlt(localctx, 10)
                self.state = 160
                localctx._assignmentOther = self.assignmentOther()
                self.state = 161
                self.match(SetlXgrammarParser.T__10)
                localctx.stmnt = localctx._assignmentOther.assign 
                pass

            elif la_ == 11:
                self.enterOuterAlt(localctx, 11)
                self.state = 164
                localctx._assignmentDirect = self.assignmentDirect()
                self.state = 165
                self.match(SetlXgrammarParser.T__10)
                localctx.stmnt = localctx._assignmentDirect.assign 
                pass

            elif la_ == 12:
                self.enterOuterAlt(localctx, 12)
                self.state = 168
                localctx._expr = self.expr(False)
                self.state = 169
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
            self.state = 174
            localctx._assignable = self.assignable(False)
            self.state = 199
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [SetlXgrammarParser.T__16]:
                self.state = 175
                self.match(SetlXgrammarParser.T__16)
                self.state = 176
                localctx.e = self.expr(False)
                localctx.assign = SumAssignment(localctx._assignable.a, localctx.e.ex) 
                pass
            elif token in [SetlXgrammarParser.T__17]:
                self.state = 179
                self.match(SetlXgrammarParser.T__17)
                self.state = 180
                localctx.e = self.expr(False)
                localctx.assign = DifferenceAssignment(localctx._assignable.a, localctx.e.ex) 
                pass
            elif token in [SetlXgrammarParser.T__18]:
                self.state = 183
                self.match(SetlXgrammarParser.T__18)
                self.state = 184
                localctx.e = self.expr(False)
                localctx.assign = ProductAssignment(localctx._assignable.a, localctx.e.ex) 
                pass
            elif token in [SetlXgrammarParser.T__19]:
                self.state = 187
                self.match(SetlXgrammarParser.T__19)
                self.state = 188
                localctx.e = self.expr(False)
                localctx.assign = QuotientAssignment(localctx._assignable.a, localctx.e.ex) 
                pass
            elif token in [SetlXgrammarParser.T__20]:
                self.state = 191
                self.match(SetlXgrammarParser.T__20)
                self.state = 192
                localctx.e = self.expr(False)
                localctx.assign = IntegerDivisionAssignment(localctx._assignable.a, localctx.e.ex) 
                pass
            elif token in [SetlXgrammarParser.T__21]:
                self.state = 195
                self.match(SetlXgrammarParser.T__21)
                self.state = 196
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
        self.enterRule(localctx, 6, self.RULE_assignmentDirect)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 201
            localctx._assignable = self.assignable(False)
            self.state = 202
            self.match(SetlXgrammarParser.T__22)
            self.state = 209
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,7,self._ctx)
            if la_ == 1:
                self.state = 203
                localctx._assignmentDirect = self.assignmentDirect()
                localctx.assign = Assignment(localctx._assignable.a, localctx._assignmentDirect.assign)
                			
                pass

            elif la_ == 2:
                self.state = 206
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
        self.enterRule(localctx, 8, self.RULE_assignable)
        self._la = 0 # Token type
        try:
            self.state = 235
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,10,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 211
                localctx._assignableVariable = self.assignableVariable()
                localctx.a = localctx._assignableVariable.v
                self.state = 224
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==SetlXgrammarParser.T__23 or _la==SetlXgrammarParser.T__24:
                    self.state = 222
                    self._errHandler.sync(self)
                    token = self._input.LA(1)
                    if token in [SetlXgrammarParser.T__23]:
                        self.state = 213
                        self.match(SetlXgrammarParser.T__23)
                        self.state = 214
                        localctx._variable = self.variable()
                        localctx.a = AssignableMember(localctx.a, localctx._variable.v)
                        pass
                    elif token in [SetlXgrammarParser.T__24]:
                        self.state = 217
                        self.match(SetlXgrammarParser.T__24)
                        self.state = 218
                        self.exprList(False)
                        self.state = 219
                        self.match(SetlXgrammarParser.T__25)
                        localctx.a = AssignableCollectionAccess(localctx.a)
                        pass
                    else:
                        raise NoViableAltException(self)

                    self.state = 226
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 227
                self.match(SetlXgrammarParser.T__24)
                self.state = 228
                localctx._assignmentList = self.assignmentList()
                self.state = 229
                self.match(SetlXgrammarParser.T__25)
                localctx.a = AssignableList(localctx._assignmentList.al)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 232
                if not localctx.enableIgnore:
                    from antlr4.error.Errors import FailedPredicateException
                    raise FailedPredicateException(self, "$enableIgnore")
                self.state = 233
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
            self.state = 237
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
            self.state = 240
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
            self.state = 243
            localctx._exprContent = self.exprContent(localctx.enableIgnore)
            localctx.exprs.append(localctx._exprContent.ex)
            self.state = 251
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==SetlXgrammarParser.T__27:
                self.state = 245
                self.match(SetlXgrammarParser.T__27)
                self.state = 246
                localctx._exprContent = self.exprContent(localctx.enableIgnore)
                localctx.exprs.append(localctx._exprContent.ex)
                self.state = 253
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
            self.state = 254
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
            self.state = 257
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
            self.state = 260
            localctx._conjunction = self.conjunction(localctx.enableIgnore)
            localctx.d = localctx._conjunction.c
            self.state = 268
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==SetlXgrammarParser.T__28:
                self.state = 262
                self.match(SetlXgrammarParser.T__28)
                self.state = 263
                localctx._conjunction = self.conjunction(localctx.enableIgnore)
                localctx.d = Disjunction(localctx.d, localctx._conjunction.c) 
                self.state = 270
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
            self.state = 271
            localctx._comparison = self.comparison(localctx.enableIgnore)
            localctx.c = localctx._comparison.c
            self.state = 279
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==SetlXgrammarParser.T__29:
                self.state = 273
                self.match(SetlXgrammarParser.T__29)
                self.state = 274
                localctx._comparison = self.comparison(localctx.enableIgnore)
                localctx.c = Conjunction(localctx.c, localctx._comparison.c) 
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
            self.state = 282
            localctx.s1 = self.setlxSum(localctx.enableIgnore)
            localctx.c = localctx.s1.s 
            self.state = 316
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [SetlXgrammarParser.T__30]:
                self.state = 284
                self.match(SetlXgrammarParser.T__30)
                self.state = 285
                localctx.s2 = self.setlxSum(localctx.enableIgnore)
                localctx.c = Equal(localctx.s1.s,localctx.s2.s) 
                pass
            elif token in [SetlXgrammarParser.T__31]:
                self.state = 288
                self.match(SetlXgrammarParser.T__31)
                self.state = 289
                localctx.s2 = self.setlxSum(localctx.enableIgnore)
                localctx.c = NotEqual(localctx.s1.s,localctx.s2.s) 
                pass
            elif token in [SetlXgrammarParser.T__32]:
                self.state = 292
                self.match(SetlXgrammarParser.T__32)
                self.state = 293
                localctx.s2 = self.setlxSum(localctx.enableIgnore)
                localctx.c = LessThan(localctx.s1.s,localctx.s2.s) 
                pass
            elif token in [SetlXgrammarParser.T__33]:
                self.state = 296
                self.match(SetlXgrammarParser.T__33)
                self.state = 297
                localctx.s2 = self.setlxSum(localctx.enableIgnore)
                localctx.c = LessOrEqual(localctx.s1.s,localctx.s2.s) 
                pass
            elif token in [SetlXgrammarParser.T__34]:
                self.state = 300
                self.match(SetlXgrammarParser.T__34)
                self.state = 301
                localctx.s2 = self.setlxSum(localctx.enableIgnore)
                localctx.c = GreaterThan(localctx.s1.s,localctx.s2.s) 
                pass
            elif token in [SetlXgrammarParser.T__35]:
                self.state = 304
                self.match(SetlXgrammarParser.T__35)
                self.state = 305
                localctx.s2 = self.setlxSum(localctx.enableIgnore)
                localctx.c = GreaterOrEqual(localctx.s1.s,localctx.s2.s) 
                pass
            elif token in [SetlXgrammarParser.T__36]:
                self.state = 308
                self.match(SetlXgrammarParser.T__36)
                self.state = 309
                localctx.s2 = self.setlxSum(localctx.enableIgnore)
                localctx.c = In(localctx.s1.s,localctx.s2.s) 
                pass
            elif token in [SetlXgrammarParser.T__37]:
                self.state = 312
                self.match(SetlXgrammarParser.T__37)
                self.state = 313
                localctx.s2 = self.setlxSum(localctx.enableIgnore)
                localctx.c = NotIn(localctx.s1.s,localctx.s2.s) 
                pass
            elif token in [SetlXgrammarParser.T__2, SetlXgrammarParser.T__7, SetlXgrammarParser.T__10, SetlXgrammarParser.T__25, SetlXgrammarParser.T__27, SetlXgrammarParser.T__28, SetlXgrammarParser.T__29]:
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
            self.state = 318
            localctx.p1 = self.product(localctx.enableIgnore)
            localctx.s = localctx.p1.p
            self.state = 330
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==SetlXgrammarParser.T__38 or _la==SetlXgrammarParser.T__39:
                self.state = 328
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [SetlXgrammarParser.T__38]:
                    self.state = 320
                    self.match(SetlXgrammarParser.T__38)
                    self.state = 321
                    localctx.p2 = self.product(localctx.enableIgnore)
                    localctx.s = Sum(localctx.p1.p,localctx.p2.p) 
                    pass
                elif token in [SetlXgrammarParser.T__39]:
                    self.state = 324
                    self.match(SetlXgrammarParser.T__39)
                    self.state = 325
                    localctx.p2 = self.product(localctx.enableIgnore)
                    localctx.s = Difference(localctx.p1.p,localctx.p2.p) 
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 332
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
            self.state = 333
            localctx.r1 = self.setlxReduce(localctx.enableIgnore)
            localctx.p = localctx.r1.r
            self.state = 353
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << SetlXgrammarParser.T__40) | (1 << SetlXgrammarParser.T__41) | (1 << SetlXgrammarParser.T__42) | (1 << SetlXgrammarParser.T__43))) != 0):
                self.state = 351
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [SetlXgrammarParser.T__40]:
                    self.state = 335
                    self.match(SetlXgrammarParser.T__40)
                    self.state = 336
                    localctx.r2 = self.setlxReduce(localctx.enableIgnore)
                    localctx.p = Product(localctx.p,localctx.r2.r) 
                    pass
                elif token in [SetlXgrammarParser.T__41]:
                    self.state = 339
                    self.match(SetlXgrammarParser.T__41)
                    self.state = 340
                    localctx.r2 = self.setlxReduce(localctx.enableIgnore)
                    localctx.p = Quotient(localctx.p,localctx.r2.r) 
                    pass
                elif token in [SetlXgrammarParser.T__42]:
                    self.state = 343
                    self.match(SetlXgrammarParser.T__42)
                    self.state = 344
                    localctx.r2 = self.setlxReduce(localctx.enableIgnore)
                    localctx.p = IntegerDivision(localctx.p,localctx.r2.r) 
                    pass
                elif token in [SetlXgrammarParser.T__43]:
                    self.state = 347
                    self.match(SetlXgrammarParser.T__43)
                    self.state = 348
                    localctx.r2 = self.setlxReduce(localctx.enableIgnore)
                    localctx.p = Modulo(localctx.p,localctx.r2.r) 
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 355
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
            self.state = 356
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
            self.state = 371
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,20,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 359
                localctx._factor = self.factor(localctx.enableIgnore)
                localctx.p = localctx._factor.f
                self.state = 365
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==SetlXgrammarParser.T__44:
                    self.state = 361
                    self.match(SetlXgrammarParser.T__44)
                    self.state = 362
                    localctx._prefixOperation = self.prefixOperation(localctx.enableIgnore)
                    localctx.p = Power(localctx.p,localctx._prefixOperation.p) 


                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 367
                self.match(SetlXgrammarParser.T__39)
                self.state = 368
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
            self.state = 412
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,26,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 373
                self.match(SetlXgrammarParser.T__45)
                self.state = 374
                localctx._factor = self.factor(localctx.enableIgnore)
                localctx.f = Not(localctx._factor.f) 
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 388
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [SetlXgrammarParser.T__1]:
                    self.state = 377
                    self.match(SetlXgrammarParser.T__1)
                    self.state = 378
                    localctx._exprContent = self.exprContent(localctx.enableIgnore)
                    self.state = 379
                    self.match(SetlXgrammarParser.T__2)
                    localctx.f = localctx._exprContent.ex 
                    pass
                elif token in [SetlXgrammarParser.T__46]:
                    self.state = 382
                    localctx._procedure = self.procedure()
                    localctx.f = localctx._procedure.pd 
                    pass
                elif token in [SetlXgrammarParser.ID]:
                    self.state = 385
                    localctx._variable = self.variable()
                    localctx.f = localctx._variable.v 
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 399
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==SetlXgrammarParser.T__1 or _la==SetlXgrammarParser.T__23:
                    self.state = 397
                    self._errHandler.sync(self)
                    token = self._input.LA(1)
                    if token in [SetlXgrammarParser.T__23]:
                        self.state = 390
                        self.match(SetlXgrammarParser.T__23)
                        self.state = 391
                        localctx._variable = self.variable()
                        localctx.f = MemberAccess(localctx.f,localctx._variable.v) 
                        pass
                    elif token in [SetlXgrammarParser.T__1]:
                        self.state = 394
                        localctx._call = self.call(localctx.enableIgnore)

                        localctx._call.c.callable = localctx.f
                        localctx.f = localctx._call.c
                                
                        pass
                    else:
                        raise NoViableAltException(self)

                    self.state = 401
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 404
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==SetlXgrammarParser.T__45:
                    self.state = 402
                    self.match(SetlXgrammarParser.T__45)
                    localctx.f = Factorial(localctx.f) 


                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 406
                localctx._value = self.value(localctx.enableIgnore)
                localctx.f = localctx._value.v 
                self.state = 410
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==SetlXgrammarParser.T__45:
                    self.state = 408
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
            self.state = 414
            self.match(SetlXgrammarParser.T__46)
            self.state = 415
            self.match(SetlXgrammarParser.T__1)
            self.state = 416
            localctx._procedureParameters = self.procedureParameters(True)
            self.state = 417
            self.match(SetlXgrammarParser.T__2)
            self.state = 418
            self.match(SetlXgrammarParser.T__3)
            self.state = 419
            localctx._block = self.block()
            self.state = 420
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
            self.state = 455
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,30,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 423
                localctx.pp1 = self.procedureParameter(localctx.enableRw)
                localctx.paramList.append(localctx.pp1.param) 
                self.state = 431
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,27,self._ctx)
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1:
                        self.state = 425
                        self.match(SetlXgrammarParser.T__27)
                        self.state = 426
                        localctx.pp2 = self.procedureParameter(localctx.enableRw)
                        localctx.paramList.append(localctx.pp2.param)  
                    self.state = 433
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,27,self._ctx)

                self.state = 440
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==SetlXgrammarParser.T__27:
                    self.state = 434
                    self.match(SetlXgrammarParser.T__27)
                    self.state = 435
                    localctx.dp1 = self.procedureDefaultParameter()
                    localctx.paramList.append(localctx.dp1.param) 
                    self.state = 442
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 443
                localctx.dp2 = self.procedureDefaultParameter()
                localctx.paramList.append(localctx.dp2.param) 
                self.state = 451
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==SetlXgrammarParser.T__27:
                    self.state = 445
                    self.match(SetlXgrammarParser.T__27)
                    self.state = 446
                    localctx.dp3 = self.procedureDefaultParameter()
                    localctx.paramList.append(localctx.dp3.param) 
                    self.state = 453
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
            self.state = 457
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
            self.state = 460
            localctx._assignableVariable = self.assignableVariable()
            self.state = 461
            self.match(SetlXgrammarParser.T__22)
            self.state = 462
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
        self.enterRule(localctx, 44, self.RULE_call)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 465
            self.match(SetlXgrammarParser.T__1)
            self.state = 466
            localctx._callParameters = self.callParameters(localctx.enableIgnore)
            self.state = 467
            self.match(SetlXgrammarParser.T__2)
            localctx.c = FunctionCall(localctx._callParameters.params, localctx._callParameters.ex) 
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
        self.enterRule(localctx, 46, self.RULE_callParameters)

        localctx.params = []
        localctx.ex = None
            
        try:
            self.state = 474
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,31,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 470
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
        self.enterRule(localctx, 48, self.RULE_value)
        try:
            self.state = 486
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,32,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 476
                localctx._STRING = self.match(SetlXgrammarParser.STRING)
                localctx.v = SetlXString((None if localctx._STRING is None else localctx._STRING.text)) 
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 478
                localctx._LITERAL = self.match(SetlXgrammarParser.LITERAL)
                localctx.v = SetlXLiteral((None if localctx._LITERAL is None else localctx._LITERAL.text)) 
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 480
                localctx._atomicValue = self.atomicValue()
                localctx.v = localctx._atomicValue.av 
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 483
                if not localctx.enableIgnore:
                    from antlr4.error.Errors import FailedPredicateException
                    raise FailedPredicateException(self, "$enableIgnore")
                self.state = 484
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
        self.enterRule(localctx, 50, self.RULE_iteratorChain)

        localctx.ic = []
            
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 488
            localctx.i1 = self.iterator(localctx.enableIgnore)
            localctx.ic.append(localctx.i1.iter)
            self.state = 496
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==SetlXgrammarParser.T__27:
                self.state = 490
                self.match(SetlXgrammarParser.T__27)
                self.state = 491
                localctx.i2 = self.iterator(localctx.enableIgnore)
                localctx.ic.append(localctx.i2.iter) 
                self.state = 498
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
        self.enterRule(localctx, 52, self.RULE_iterator)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 499
            localctx._assignable = self.assignable(True)
            self.state = 500
            self.match(SetlXgrammarParser.T__36)
            self.state = 501
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
        self.enterRule(localctx, 54, self.RULE_atomicValue)
        try:
            self.state = 514
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [SetlXgrammarParser.NUMBER]:
                self.enterOuterAlt(localctx, 1)
                self.state = 504
                localctx._NUMBER = self.match(SetlXgrammarParser.NUMBER)
                localctx.av = SetlXFraction((None if localctx._NUMBER is None else localctx._NUMBER.text)) 
                pass
            elif token in [SetlXgrammarParser.DOUBLE]:
                self.enterOuterAlt(localctx, 2)
                self.state = 506
                localctx._DOUBLE = self.match(SetlXgrammarParser.DOUBLE)
                localctx.av = float((None if localctx._DOUBLE is None else localctx._DOUBLE.text)) 
                pass
            elif token in [SetlXgrammarParser.T__47]:
                self.enterOuterAlt(localctx, 3)
                self.state = 508
                self.match(SetlXgrammarParser.T__47)
                localctx.av = SetlXOm() 
                pass
            elif token in [SetlXgrammarParser.T__48]:
                self.enterOuterAlt(localctx, 4)
                self.state = 510
                self.match(SetlXgrammarParser.T__48)
                localctx.av = TRUE 
                pass
            elif token in [SetlXgrammarParser.T__49]:
                self.enterOuterAlt(localctx, 5)
                self.state = 512
                self.match(SetlXgrammarParser.T__49)
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
        self.enterRule(localctx, 56, self.RULE_variable)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 516
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
        self.enterRule(localctx, 58, self.RULE_condition)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 519
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
        self.enterRule(localctx, 60, self.RULE_assignmentList)

        localctx.al = []
            
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 522
            localctx.a1 = self.assignable(True)
            localctx.al.append(localctx.a1.a) 
            self.state = 530
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==SetlXgrammarParser.T__27:
                self.state = 524
                self.match(SetlXgrammarParser.T__27)
                self.state = 525
                localctx.a2 = self.assignable(True)
                localctx.al.append(localctx.a2.a) 
                self.state = 532
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
        self._predicates[24] = self.value_sempred
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
         




