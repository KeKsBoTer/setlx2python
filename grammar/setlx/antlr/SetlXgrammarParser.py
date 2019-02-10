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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3D")
        buf.write("\u029f\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31")
        buf.write("\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36")
        buf.write("\4\37\t\37\4 \t \4!\t!\4\"\t\"\3\2\3\2\3\2\7\2H\n\2\f")
        buf.write("\2\16\2K\13\2\3\2\3\2\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3")
        buf.write("\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\7\3`\n\3\f\3\16\3")
        buf.write("c\13\3\3\3\3\3\3\3\3\3\3\3\3\3\5\3k\n\3\3\3\3\3\3\3\3")
        buf.write("\3\3\3\3\3\3\3\3\3\3\3\3\3\7\3w\n\3\f\3\16\3z\13\3\3\3")
        buf.write("\3\3\3\3\5\3\177\n\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3")
        buf.write("\3\5\3\u008a\n\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3")
        buf.write("\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3")
        buf.write("\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3")
        buf.write("\3\3\3\3\3\3\3\3\3\3\3\5\3\u00b6\n\3\3\3\3\3\3\3\3\3\3")
        buf.write("\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\5\3\u00c6\n\3\3")
        buf.write("\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4")
        buf.write("\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\5\4\u00e1")
        buf.write("\n\4\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3")
        buf.write("\5\5\5\u00f0\n\5\5\5\u00f2\n\5\3\6\3\6\3\6\3\6\3\6\3\6")
        buf.write("\3\6\3\6\3\6\3\6\3\6\7\6\u00ff\n\6\f\6\16\6\u0102\13\6")
        buf.write("\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\5\6\u010c\n\6\3\7\3\7")
        buf.write("\3\7\3\b\3\b\3\b\3\t\3\t\3\t\3\t\3\t\3\t\7\t\u011a\n\t")
        buf.write("\f\t\16\t\u011d\13\t\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3")
        buf.write("\n\3\n\5\n\u0129\n\n\3\13\3\13\3\13\3\13\3\13\3\13\5\13")
        buf.write("\u0131\n\13\3\f\3\f\3\f\3\f\3\f\3\f\7\f\u0139\n\f\f\f")
        buf.write("\16\f\u013c\13\f\3\r\3\r\3\r\3\r\3\r\3\r\7\r\u0144\n\r")
        buf.write("\f\r\16\r\u0147\13\r\3\16\3\16\3\16\3\16\3\16\3\16\3\16")
        buf.write("\3\16\3\16\3\16\3\16\3\16\3\16\3\16\3\16\3\16\3\16\3\16")
        buf.write("\3\16\3\16\3\16\3\16\3\16\3\16\3\16\3\16\3\16\3\16\3\16")
        buf.write("\3\16\3\16\3\16\3\16\3\16\5\16\u016b\n\16\3\17\3\17\3")
        buf.write("\17\3\17\3\17\3\17\3\17\3\17\3\17\3\17\7\17\u0177\n\17")
        buf.write("\f\17\16\17\u017a\13\17\3\20\3\20\3\20\3\20\3\20\3\20")
        buf.write("\3\20\3\20\3\20\3\20\3\20\3\20\3\20\3\20\3\20\3\20\3\20")
        buf.write("\3\20\7\20\u018e\n\20\f\20\16\20\u0191\13\20\3\21\3\21")
        buf.write("\3\21\3\22\3\22\3\22\3\22\3\22\3\22\5\22\u019c\n\22\3")
        buf.write("\22\3\22\3\22\3\22\5\22\u01a2\n\22\3\23\3\23\3\23\3\23")
        buf.write("\3\23\3\23\3\23\3\23\3\23\3\23\3\23\3\23\3\23\3\23\3\23")
        buf.write("\5\23\u01b3\n\23\3\23\3\23\3\23\3\23\3\23\3\23\3\23\7")
        buf.write("\23\u01bc\n\23\f\23\16\23\u01bf\13\23\3\23\3\23\5\23\u01c3")
        buf.write("\n\23\3\23\3\23\3\23\3\23\5\23\u01c9\n\23\5\23\u01cb\n")
        buf.write("\23\3\24\3\24\3\24\3\24\3\24\3\24\3\24\3\24\3\24\3\25")
        buf.write("\3\25\3\25\3\25\3\25\3\25\7\25\u01dc\n\25\f\25\16\25\u01df")
        buf.write("\13\25\3\25\3\25\3\25\3\25\7\25\u01e5\n\25\f\25\16\25")
        buf.write("\u01e8\13\25\3\25\3\25\3\25\3\25\3\25\3\25\7\25\u01f0")
        buf.write("\n\25\f\25\16\25\u01f3\13\25\3\25\5\25\u01f6\n\25\3\26")
        buf.write("\3\26\3\26\3\27\3\27\3\27\3\27\3\27\3\30\3\30\3\30\3\30")
        buf.write("\3\30\3\30\3\30\3\30\3\30\3\30\5\30\u020a\n\30\3\31\3")
        buf.write("\31\3\31\3\31\3\31\3\31\5\31\u0212\n\31\3\31\3\31\3\31")
        buf.write("\3\31\6\31\u0218\n\31\r\31\16\31\u0219\3\31\3\31\3\31")
        buf.write("\5\31\u021f\n\31\3\31\3\31\3\31\3\31\5\31\u0225\n\31\3")
        buf.write("\32\3\32\3\32\3\32\5\32\u022b\n\32\3\33\3\33\3\33\3\33")
        buf.write("\5\33\u0231\n\33\3\33\3\33\3\33\3\33\3\33\3\33\3\33\3")
        buf.write("\33\3\33\3\33\3\33\3\33\5\33\u023f\n\33\3\34\3\34\3\34")
        buf.write("\3\34\3\34\3\34\3\34\3\34\3\34\3\34\3\34\3\34\7\34\u024d")
        buf.write("\n\34\f\34\16\34\u0250\13\34\3\34\3\34\3\34\3\34\3\34")
        buf.write("\5\34\u0257\n\34\5\34\u0259\n\34\3\34\3\34\3\34\3\34\3")
        buf.write("\34\3\34\3\34\3\34\3\34\3\34\5\34\u0265\n\34\3\34\3\34")
        buf.write("\3\34\3\34\3\34\3\34\3\34\5\34\u026e\n\34\5\34\u0270\n")
        buf.write("\34\3\35\3\35\3\35\3\35\3\35\3\35\7\35\u0278\n\35\f\35")
        buf.write("\16\35\u027b\13\35\3\36\3\36\3\36\3\36\3\36\3\37\3\37")
        buf.write("\3\37\3\37\3\37\3\37\3\37\3\37\3\37\3\37\5\37\u028c\n")
        buf.write("\37\3 \3 \3 \3!\3!\3!\3\"\3\"\3\"\3\"\3\"\3\"\7\"\u029a")
        buf.write("\n\"\f\"\16\"\u029d\13\"\3\"\2\2#\2\4\6\b\n\f\16\20\22")
        buf.write("\24\26\30\32\34\36 \"$&(*,.\60\62\64\668:<>@B\2\2\2\u02d8")
        buf.write("\2I\3\2\2\2\4\u00c5\3\2\2\2\6\u00c7\3\2\2\2\b\u00f1\3")
        buf.write("\2\2\2\n\u010b\3\2\2\2\f\u010d\3\2\2\2\16\u0110\3\2\2")
        buf.write("\2\20\u0113\3\2\2\2\22\u011e\3\2\2\2\24\u012a\3\2\2\2")
        buf.write("\26\u0132\3\2\2\2\30\u013d\3\2\2\2\32\u0148\3\2\2\2\34")
        buf.write("\u016c\3\2\2\2\36\u017b\3\2\2\2 \u0192\3\2\2\2\"\u01a1")
        buf.write("\3\2\2\2$\u01ca\3\2\2\2&\u01cc\3\2\2\2(\u01f5\3\2\2\2")
        buf.write("*\u01f7\3\2\2\2,\u01fa\3\2\2\2.\u0209\3\2\2\2\60\u0224")
        buf.write("\3\2\2\2\62\u022a\3\2\2\2\64\u023e\3\2\2\2\66\u0240\3")
        buf.write("\2\2\28\u0271\3\2\2\2:\u027c\3\2\2\2<\u028b\3\2\2\2>\u028d")
        buf.write("\3\2\2\2@\u0290\3\2\2\2B\u0293\3\2\2\2DE\5\4\3\2EF\b\2")
        buf.write("\1\2FH\3\2\2\2GD\3\2\2\2HK\3\2\2\2IG\3\2\2\2IJ\3\2\2\2")
        buf.write("JL\3\2\2\2KI\3\2\2\2LM\b\2\1\2M\3\3\2\2\2NO\7\3\2\2OP")
        buf.write("\7\4\2\2PQ\5@!\2QR\7\5\2\2RS\7\6\2\2ST\5\2\2\2Ta\7\7\2")
        buf.write("\2UV\7\b\2\2VW\7\3\2\2WX\7\4\2\2XY\5@!\2YZ\7\5\2\2Z[\7")
        buf.write("\6\2\2[\\\5\2\2\2\\]\7\7\2\2]^\b\3\1\2^`\3\2\2\2_U\3\2")
        buf.write("\2\2`c\3\2\2\2a_\3\2\2\2ab\3\2\2\2bj\3\2\2\2ca\3\2\2\2")
        buf.write("de\7\b\2\2ef\7\6\2\2fg\5\2\2\2gh\7\7\2\2hi\b\3\1\2ik\3")
        buf.write("\2\2\2jd\3\2\2\2jk\3\2\2\2kl\3\2\2\2lm\b\3\1\2m\u00c6")
        buf.write("\3\2\2\2no\7\t\2\2ox\7\6\2\2pq\7\n\2\2qr\5@!\2rs\7\13")
        buf.write("\2\2st\5\2\2\2tu\b\3\1\2uw\3\2\2\2vp\3\2\2\2wz\3\2\2\2")
        buf.write("xv\3\2\2\2xy\3\2\2\2y~\3\2\2\2zx\3\2\2\2{|\7\f\2\2|}\7")
        buf.write("\13\2\2}\177\5\2\2\2~{\3\2\2\2~\177\3\2\2\2\177\u0080")
        buf.write("\3\2\2\2\u0080\u0081\7\7\2\2\u0081\u00c6\b\3\1\2\u0082")
        buf.write("\u0083\7\r\2\2\u0083\u0084\7\4\2\2\u0084\u0089\58\35\2")
        buf.write("\u0085\u0086\7\16\2\2\u0086\u0087\5@!\2\u0087\u0088\b")
        buf.write("\3\1\2\u0088\u008a\3\2\2\2\u0089\u0085\3\2\2\2\u0089\u008a")
        buf.write("\3\2\2\2\u008a\u008b\3\2\2\2\u008b\u008c\7\5\2\2\u008c")
        buf.write("\u008d\7\6\2\2\u008d\u008e\5\2\2\2\u008e\u008f\7\7\2\2")
        buf.write("\u008f\u0090\b\3\1\2\u0090\u00c6\3\2\2\2\u0091\u0092\7")
        buf.write("\17\2\2\u0092\u0093\7\4\2\2\u0093\u0094\5@!\2\u0094\u0095")
        buf.write("\7\5\2\2\u0095\u0096\7\6\2\2\u0096\u0097\5\2\2\2\u0097")
        buf.write("\u0098\7\7\2\2\u0098\u0099\b\3\1\2\u0099\u00c6\3\2\2\2")
        buf.write("\u009a\u009b\7\20\2\2\u009b\u009c\7\6\2\2\u009c\u009d")
        buf.write("\5\2\2\2\u009d\u009e\7\7\2\2\u009e\u009f\7\17\2\2\u009f")
        buf.write("\u00a0\7\4\2\2\u00a0\u00a1\5@!\2\u00a1\u00a2\7\5\2\2\u00a2")
        buf.write("\u00a3\7\21\2\2\u00a3\u00a4\b\3\1\2\u00a4\u00c6\3\2\2")
        buf.write("\2\u00a5\u00a6\7\22\2\2\u00a6\u00a7\7\21\2\2\u00a7\u00c6")
        buf.write("\b\3\1\2\u00a8\u00a9\7\23\2\2\u00a9\u00aa\7\21\2\2\u00aa")
        buf.write("\u00c6\b\3\1\2\u00ab\u00ac\7\24\2\2\u00ac\u00ad\7\21\2")
        buf.write("\2\u00ad\u00c6\b\3\1\2\u00ae\u00af\7\25\2\2\u00af\u00b0")
        buf.write("\7\21\2\2\u00b0\u00c6\b\3\1\2\u00b1\u00b5\7\26\2\2\u00b2")
        buf.write("\u00b3\5\16\b\2\u00b3\u00b4\b\3\1\2\u00b4\u00b6\3\2\2")
        buf.write("\2\u00b5\u00b2\3\2\2\2\u00b5\u00b6\3\2\2\2\u00b6\u00b7")
        buf.write("\3\2\2\2\u00b7\u00b8\7\21\2\2\u00b8\u00c6\b\3\1\2\u00b9")
        buf.write("\u00ba\5\6\4\2\u00ba\u00bb\7\21\2\2\u00bb\u00bc\b\3\1")
        buf.write("\2\u00bc\u00c6\3\2\2\2\u00bd\u00be\5\b\5\2\u00be\u00bf")
        buf.write("\7\21\2\2\u00bf\u00c0\b\3\1\2\u00c0\u00c6\3\2\2\2\u00c1")
        buf.write("\u00c2\5\16\b\2\u00c2\u00c3\7\21\2\2\u00c3\u00c4\b\3\1")
        buf.write("\2\u00c4\u00c6\3\2\2\2\u00c5N\3\2\2\2\u00c5n\3\2\2\2\u00c5")
        buf.write("\u0082\3\2\2\2\u00c5\u0091\3\2\2\2\u00c5\u009a\3\2\2\2")
        buf.write("\u00c5\u00a5\3\2\2\2\u00c5\u00a8\3\2\2\2\u00c5\u00ab\3")
        buf.write("\2\2\2\u00c5\u00ae\3\2\2\2\u00c5\u00b1\3\2\2\2\u00c5\u00b9")
        buf.write("\3\2\2\2\u00c5\u00bd\3\2\2\2\u00c5\u00c1\3\2\2\2\u00c6")
        buf.write("\5\3\2\2\2\u00c7\u00e0\5\n\6\2\u00c8\u00c9\7\27\2\2\u00c9")
        buf.write("\u00ca\5\16\b\2\u00ca\u00cb\b\4\1\2\u00cb\u00e1\3\2\2")
        buf.write("\2\u00cc\u00cd\7\30\2\2\u00cd\u00ce\5\16\b\2\u00ce\u00cf")
        buf.write("\b\4\1\2\u00cf\u00e1\3\2\2\2\u00d0\u00d1\7\31\2\2\u00d1")
        buf.write("\u00d2\5\16\b\2\u00d2\u00d3\b\4\1\2\u00d3\u00e1\3\2\2")
        buf.write("\2\u00d4\u00d5\7\32\2\2\u00d5\u00d6\5\16\b\2\u00d6\u00d7")
        buf.write("\b\4\1\2\u00d7\u00e1\3\2\2\2\u00d8\u00d9\7\33\2\2\u00d9")
        buf.write("\u00da\5\16\b\2\u00da\u00db\b\4\1\2\u00db\u00e1\3\2\2")
        buf.write("\2\u00dc\u00dd\7\34\2\2\u00dd\u00de\5\16\b\2\u00de\u00df")
        buf.write("\b\4\1\2\u00df\u00e1\3\2\2\2\u00e0\u00c8\3\2\2\2\u00e0")
        buf.write("\u00cc\3\2\2\2\u00e0\u00d0\3\2\2\2\u00e0\u00d4\3\2\2\2")
        buf.write("\u00e0\u00d8\3\2\2\2\u00e0\u00dc\3\2\2\2\u00e1\7\3\2\2")
        buf.write("\2\u00e2\u00e3\5> \2\u00e3\u00e4\7\35\2\2\u00e4\u00e5")
        buf.write("\5&\24\2\u00e5\u00e6\b\5\1\2\u00e6\u00f2\3\2\2\2\u00e7")
        buf.write("\u00e8\5\n\6\2\u00e8\u00ef\7\35\2\2\u00e9\u00ea\5\b\5")
        buf.write("\2\u00ea\u00eb\b\5\1\2\u00eb\u00f0\3\2\2\2\u00ec\u00ed")
        buf.write("\5\22\n\2\u00ed\u00ee\b\5\1\2\u00ee\u00f0\3\2\2\2\u00ef")
        buf.write("\u00e9\3\2\2\2\u00ef\u00ec\3\2\2\2\u00f0\u00f2\3\2\2\2")
        buf.write("\u00f1\u00e2\3\2\2\2\u00f1\u00e7\3\2\2\2\u00f2\t\3\2\2")
        buf.write("\2\u00f3\u00f4\5\f\7\2\u00f4\u0100\b\6\1\2\u00f5\u00f6")
        buf.write("\7\36\2\2\u00f6\u00f7\5> \2\u00f7\u00f8\b\6\1\2\u00f8")
        buf.write("\u00ff\3\2\2\2\u00f9\u00fa\7\37\2\2\u00fa\u00fb\5\20\t")
        buf.write("\2\u00fb\u00fc\7 \2\2\u00fc\u00fd\b\6\1\2\u00fd\u00ff")
        buf.write("\3\2\2\2\u00fe\u00f5\3\2\2\2\u00fe\u00f9\3\2\2\2\u00ff")
        buf.write("\u0102\3\2\2\2\u0100\u00fe\3\2\2\2\u0100\u0101\3\2\2\2")
        buf.write("\u0101\u010c\3\2\2\2\u0102\u0100\3\2\2\2\u0103\u0104\7")
        buf.write("\37\2\2\u0104\u0105\5B\"\2\u0105\u0106\7 \2\2\u0106\u0107")
        buf.write("\b\6\1\2\u0107\u010c\3\2\2\2\u0108\u0109\6\6\2\3\u0109")
        buf.write("\u010a\7!\2\2\u010a\u010c\b\6\1\2\u010b\u00f3\3\2\2\2")
        buf.write("\u010b\u0103\3\2\2\2\u010b\u0108\3\2\2\2\u010c\13\3\2")
        buf.write("\2\2\u010d\u010e\7<\2\2\u010e\u010f\b\7\1\2\u010f\r\3")
        buf.write("\2\2\2\u0110\u0111\5\22\n\2\u0111\u0112\b\b\1\2\u0112")
        buf.write("\17\3\2\2\2\u0113\u0114\5\22\n\2\u0114\u011b\b\t\1\2\u0115")
        buf.write("\u0116\7\"\2\2\u0116\u0117\5\22\n\2\u0117\u0118\b\t\1")
        buf.write("\2\u0118\u011a\3\2\2\2\u0119\u0115\3\2\2\2\u011a\u011d")
        buf.write("\3\2\2\2\u011b\u0119\3\2\2\2\u011b\u011c\3\2\2\2\u011c")
        buf.write("\21\3\2\2\2\u011d\u011b\3\2\2\2\u011e\u011f\5\24\13\2")
        buf.write("\u011f\u0128\b\n\1\2\u0120\u0121\7#\2\2\u0121\u0122\5")
        buf.write("\24\13\2\u0122\u0123\b\n\1\2\u0123\u0129\3\2\2\2\u0124")
        buf.write("\u0125\7$\2\2\u0125\u0126\5\24\13\2\u0126\u0127\b\n\1")
        buf.write("\2\u0127\u0129\3\2\2\2\u0128\u0120\3\2\2\2\u0128\u0124")
        buf.write("\3\2\2\2\u0128\u0129\3\2\2\2\u0129\23\3\2\2\2\u012a\u012b")
        buf.write("\5\26\f\2\u012b\u0130\b\13\1\2\u012c\u012d\7%\2\2\u012d")
        buf.write("\u012e\5\24\13\2\u012e\u012f\b\13\1\2\u012f\u0131\3\2")
        buf.write("\2\2\u0130\u012c\3\2\2\2\u0130\u0131\3\2\2\2\u0131\25")
        buf.write("\3\2\2\2\u0132\u0133\5\30\r\2\u0133\u013a\b\f\1\2\u0134")
        buf.write("\u0135\7&\2\2\u0135\u0136\5\30\r\2\u0136\u0137\b\f\1\2")
        buf.write("\u0137\u0139\3\2\2\2\u0138\u0134\3\2\2\2\u0139\u013c\3")
        buf.write("\2\2\2\u013a\u0138\3\2\2\2\u013a\u013b\3\2\2\2\u013b\27")
        buf.write("\3\2\2\2\u013c\u013a\3\2\2\2\u013d\u013e\5\32\16\2\u013e")
        buf.write("\u0145\b\r\1\2\u013f\u0140\7\'\2\2\u0140\u0141\5\32\16")
        buf.write("\2\u0141\u0142\b\r\1\2\u0142\u0144\3\2\2\2\u0143\u013f")
        buf.write("\3\2\2\2\u0144\u0147\3\2\2\2\u0145\u0143\3\2\2\2\u0145")
        buf.write("\u0146\3\2\2\2\u0146\31\3\2\2\2\u0147\u0145\3\2\2\2\u0148")
        buf.write("\u0149\5\34\17\2\u0149\u016a\b\16\1\2\u014a\u014b\7(\2")
        buf.write("\2\u014b\u014c\5\34\17\2\u014c\u014d\b\16\1\2\u014d\u016b")
        buf.write("\3\2\2\2\u014e\u014f\7)\2\2\u014f\u0150\5\34\17\2\u0150")
        buf.write("\u0151\b\16\1\2\u0151\u016b\3\2\2\2\u0152\u0153\7*\2\2")
        buf.write("\u0153\u0154\5\34\17\2\u0154\u0155\b\16\1\2\u0155\u016b")
        buf.write("\3\2\2\2\u0156\u0157\7+\2\2\u0157\u0158\5\34\17\2\u0158")
        buf.write("\u0159\b\16\1\2\u0159\u016b\3\2\2\2\u015a\u015b\7,\2\2")
        buf.write("\u015b\u015c\5\34\17\2\u015c\u015d\b\16\1\2\u015d\u016b")
        buf.write("\3\2\2\2\u015e\u015f\7-\2\2\u015f\u0160\5\34\17\2\u0160")
        buf.write("\u0161\b\16\1\2\u0161\u016b\3\2\2\2\u0162\u0163\7.\2\2")
        buf.write("\u0163\u0164\5\34\17\2\u0164\u0165\b\16\1\2\u0165\u016b")
        buf.write("\3\2\2\2\u0166\u0167\7/\2\2\u0167\u0168\5\34\17\2\u0168")
        buf.write("\u0169\b\16\1\2\u0169\u016b\3\2\2\2\u016a\u014a\3\2\2")
        buf.write("\2\u016a\u014e\3\2\2\2\u016a\u0152\3\2\2\2\u016a\u0156")
        buf.write("\3\2\2\2\u016a\u015a\3\2\2\2\u016a\u015e\3\2\2\2\u016a")
        buf.write("\u0162\3\2\2\2\u016a\u0166\3\2\2\2\u016a\u016b\3\2\2\2")
        buf.write("\u016b\33\3\2\2\2\u016c\u016d\5\36\20\2\u016d\u0178\b")
        buf.write("\17\1\2\u016e\u016f\7\60\2\2\u016f\u0170\5\36\20\2\u0170")
        buf.write("\u0171\b\17\1\2\u0171\u0177\3\2\2\2\u0172\u0173\7\61\2")
        buf.write("\2\u0173\u0174\5\36\20\2\u0174\u0175\b\17\1\2\u0175\u0177")
        buf.write("\3\2\2\2\u0176\u016e\3\2\2\2\u0176\u0172\3\2\2\2\u0177")
        buf.write("\u017a\3\2\2\2\u0178\u0176\3\2\2\2\u0178\u0179\3\2\2\2")
        buf.write("\u0179\35\3\2\2\2\u017a\u0178\3\2\2\2\u017b\u017c\5 \21")
        buf.write("\2\u017c\u018f\b\20\1\2\u017d\u017e\7\62\2\2\u017e\u017f")
        buf.write("\5 \21\2\u017f\u0180\b\20\1\2\u0180\u018e\3\2\2\2\u0181")
        buf.write("\u0182\7\63\2\2\u0182\u0183\5 \21\2\u0183\u0184\b\20\1")
        buf.write("\2\u0184\u018e\3\2\2\2\u0185\u0186\7\64\2\2\u0186\u0187")
        buf.write("\5 \21\2\u0187\u0188\b\20\1\2\u0188\u018e\3\2\2\2\u0189")
        buf.write("\u018a\7\65\2\2\u018a\u018b\5 \21\2\u018b\u018c\b\20\1")
        buf.write("\2\u018c\u018e\3\2\2\2\u018d\u017d\3\2\2\2\u018d\u0181")
        buf.write("\3\2\2\2\u018d\u0185\3\2\2\2\u018d\u0189\3\2\2\2\u018e")
        buf.write("\u0191\3\2\2\2\u018f\u018d\3\2\2\2\u018f\u0190\3\2\2\2")
        buf.write("\u0190\37\3\2\2\2\u0191\u018f\3\2\2\2\u0192\u0193\5\"")
        buf.write("\22\2\u0193\u0194\b\21\1\2\u0194!\3\2\2\2\u0195\u0196")
        buf.write("\5$\23\2\u0196\u019b\b\22\1\2\u0197\u0198\7\66\2\2\u0198")
        buf.write("\u0199\5\"\22\2\u0199\u019a\b\22\1\2\u019a\u019c\3\2\2")
        buf.write("\2\u019b\u0197\3\2\2\2\u019b\u019c\3\2\2\2\u019c\u01a2")
        buf.write("\3\2\2\2\u019d\u019e\7\61\2\2\u019e\u019f\5\"\22\2\u019f")
        buf.write("\u01a0\b\22\1\2\u01a0\u01a2\3\2\2\2\u01a1\u0195\3\2\2")
        buf.write("\2\u01a1\u019d\3\2\2\2\u01a2#\3\2\2\2\u01a3\u01a4\7\67")
        buf.write("\2\2\u01a4\u01a5\5$\23\2\u01a5\u01a6\b\23\1\2\u01a6\u01cb")
        buf.write("\3\2\2\2\u01a7\u01a8\7\4\2\2\u01a8\u01a9\5\22\n\2\u01a9")
        buf.write("\u01aa\7\5\2\2\u01aa\u01ab\b\23\1\2\u01ab\u01b3\3\2\2")
        buf.write("\2\u01ac\u01ad\5&\24\2\u01ad\u01ae\b\23\1\2\u01ae\u01b3")
        buf.write("\3\2\2\2\u01af\u01b0\5> \2\u01b0\u01b1\b\23\1\2\u01b1")
        buf.write("\u01b3\3\2\2\2\u01b2\u01a7\3\2\2\2\u01b2\u01ac\3\2\2\2")
        buf.write("\u01b2\u01af\3\2\2\2\u01b3\u01bd\3\2\2\2\u01b4\u01b5\7")
        buf.write("\36\2\2\u01b5\u01b6\5> \2\u01b6\u01b7\b\23\1\2\u01b7\u01bc")
        buf.write("\3\2\2\2\u01b8\u01b9\5.\30\2\u01b9\u01ba\b\23\1\2\u01ba")
        buf.write("\u01bc\3\2\2\2\u01bb\u01b4\3\2\2\2\u01bb\u01b8\3\2\2\2")
        buf.write("\u01bc\u01bf\3\2\2\2\u01bd\u01bb\3\2\2\2\u01bd\u01be\3")
        buf.write("\2\2\2\u01be\u01c2\3\2\2\2\u01bf\u01bd\3\2\2\2\u01c0\u01c1")
        buf.write("\7\67\2\2\u01c1\u01c3\b\23\1\2\u01c2\u01c0\3\2\2\2\u01c2")
        buf.write("\u01c3\3\2\2\2\u01c3\u01cb\3\2\2\2\u01c4\u01c5\5\64\33")
        buf.write("\2\u01c5\u01c8\b\23\1\2\u01c6\u01c7\7\67\2\2\u01c7\u01c9")
        buf.write("\b\23\1\2\u01c8\u01c6\3\2\2\2\u01c8\u01c9\3\2\2\2\u01c9")
        buf.write("\u01cb\3\2\2\2\u01ca\u01a3\3\2\2\2\u01ca\u01b2\3\2\2\2")
        buf.write("\u01ca\u01c4\3\2\2\2\u01cb%\3\2\2\2\u01cc\u01cd\78\2\2")
        buf.write("\u01cd\u01ce\7\4\2\2\u01ce\u01cf\5(\25\2\u01cf\u01d0\7")
        buf.write("\5\2\2\u01d0\u01d1\7\6\2\2\u01d1\u01d2\5\2\2\2\u01d2\u01d3")
        buf.write("\7\7\2\2\u01d3\u01d4\b\24\1\2\u01d4\'\3\2\2\2\u01d5\u01d6")
        buf.write("\5*\26\2\u01d6\u01dd\b\25\1\2\u01d7\u01d8\7\"\2\2\u01d8")
        buf.write("\u01d9\5*\26\2\u01d9\u01da\b\25\1\2\u01da\u01dc\3\2\2")
        buf.write("\2\u01db\u01d7\3\2\2\2\u01dc\u01df\3\2\2\2\u01dd\u01db")
        buf.write("\3\2\2\2\u01dd\u01de\3\2\2\2\u01de\u01e6\3\2\2\2\u01df")
        buf.write("\u01dd\3\2\2\2\u01e0\u01e1\7\"\2\2\u01e1\u01e2\5,\27\2")
        buf.write("\u01e2\u01e3\b\25\1\2\u01e3\u01e5\3\2\2\2\u01e4\u01e0")
        buf.write("\3\2\2\2\u01e5\u01e8\3\2\2\2\u01e6\u01e4\3\2\2\2\u01e6")
        buf.write("\u01e7\3\2\2\2\u01e7\u01f6\3\2\2\2\u01e8\u01e6\3\2\2\2")
        buf.write("\u01e9\u01ea\5,\27\2\u01ea\u01f1\b\25\1\2\u01eb\u01ec")
        buf.write("\7\"\2\2\u01ec\u01ed\5,\27\2\u01ed\u01ee\b\25\1\2\u01ee")
        buf.write("\u01f0\3\2\2\2\u01ef\u01eb\3\2\2\2\u01f0\u01f3\3\2\2\2")
        buf.write("\u01f1\u01ef\3\2\2\2\u01f1\u01f2\3\2\2\2\u01f2\u01f6\3")
        buf.write("\2\2\2\u01f3\u01f1\3\2\2\2\u01f4\u01f6\3\2\2\2\u01f5\u01d5")
        buf.write("\3\2\2\2\u01f5\u01e9\3\2\2\2\u01f5\u01f4\3\2\2\2\u01f6")
        buf.write(")\3\2\2\2\u01f7\u01f8\5> \2\u01f8\u01f9\b\26\1\2\u01f9")
        buf.write("+\3\2\2\2\u01fa\u01fb\5\f\7\2\u01fb\u01fc\7\35\2\2\u01fc")
        buf.write("\u01fd\5\16\b\2\u01fd\u01fe\b\27\1\2\u01fe-\3\2\2\2\u01ff")
        buf.write("\u0200\7\4\2\2\u0200\u0201\5\62\32\2\u0201\u0202\7\5\2")
        buf.write("\2\u0202\u0203\b\30\1\2\u0203\u020a\3\2\2\2\u0204\u0205")
        buf.write("\7\37\2\2\u0205\u0206\5\60\31\2\u0206\u0207\7 \2\2\u0207")
        buf.write("\u0208\b\30\1\2\u0208\u020a\3\2\2\2\u0209\u01ff\3\2\2")
        buf.write("\2\u0209\u0204\3\2\2\2\u020a/\3\2\2\2\u020b\u021e\5\16")
        buf.write("\b\2\u020c\u0211\7?\2\2\u020d\u020e\5\16\b\2\u020e\u020f")
        buf.write("\b\31\1\2\u020f\u0212\3\2\2\2\u0210\u0212\b\31\1\2\u0211")
        buf.write("\u020d\3\2\2\2\u0211\u0210\3\2\2\2\u0212\u021f\3\2\2\2")
        buf.write("\u0213\u0214\7\"\2\2\u0214\u0215\5\16\b\2\u0215\u0216")
        buf.write("\b\31\1\2\u0216\u0218\3\2\2\2\u0217\u0213\3\2\2\2\u0218")
        buf.write("\u0219\3\2\2\2\u0219\u0217\3\2\2\2\u0219\u021a\3\2\2\2")
        buf.write("\u021a\u021b\3\2\2\2\u021b\u021c\b\31\1\2\u021c\u021f")
        buf.write("\3\2\2\2\u021d\u021f\b\31\1\2\u021e\u020c\3\2\2\2\u021e")
        buf.write("\u0217\3\2\2\2\u021e\u021d\3\2\2\2\u021f\u0225\3\2\2\2")
        buf.write("\u0220\u0221\7?\2\2\u0221\u0222\5\16\b\2\u0222\u0223\b")
        buf.write("\31\1\2\u0223\u0225\3\2\2\2\u0224\u020b\3\2\2\2\u0224")
        buf.write("\u0220\3\2\2\2\u0225\61\3\2\2\2\u0226\u0227\5\20\t\2\u0227")
        buf.write("\u0228\b\32\1\2\u0228\u022b\3\2\2\2\u0229\u022b\3\2\2")
        buf.write("\2\u022a\u0226\3\2\2\2\u022a\u0229\3\2\2\2\u022b\63\3")
        buf.write("\2\2\2\u022c\u0230\7\37\2\2\u022d\u022e\5\66\34\2\u022e")
        buf.write("\u022f\b\33\1\2\u022f\u0231\3\2\2\2\u0230\u022d\3\2\2")
        buf.write("\2\u0230\u0231\3\2\2\2\u0231\u0232\3\2\2\2\u0232\u0233")
        buf.write("\7 \2\2\u0233\u023f\b\33\1\2\u0234\u0235\7@\2\2\u0235")
        buf.write("\u023f\b\33\1\2\u0236\u0237\7A\2\2\u0237\u023f\b\33\1")
        buf.write("\2\u0238\u0239\5<\37\2\u0239\u023a\b\33\1\2\u023a\u023f")
        buf.write("\3\2\2\2\u023b\u023c\6\33\3\3\u023c\u023d\7!\2\2\u023d")
        buf.write("\u023f\b\33\1\2\u023e\u022c\3\2\2\2\u023e\u0234\3\2\2")
        buf.write("\2\u023e\u0236\3\2\2\2\u023e\u0238\3\2\2\2\u023e\u023b")
        buf.write("\3\2\2\2\u023f\65\3\2\2\2\u0240\u026f\5\16\b\2\u0241\u0242")
        buf.write("\7\"\2\2\u0242\u0258\5\16\b\2\u0243\u0244\7?\2\2\u0244")
        buf.write("\u0245\5\16\b\2\u0245\u0246\b\34\1\2\u0246\u0259\3\2\2")
        buf.write("\2\u0247\u024e\b\34\1\2\u0248\u0249\7\"\2\2\u0249\u024a")
        buf.write("\5\16\b\2\u024a\u024b\b\34\1\2\u024b\u024d\3\2\2\2\u024c")
        buf.write("\u0248\3\2\2\2\u024d\u0250\3\2\2\2\u024e\u024c\3\2\2\2")
        buf.write("\u024e\u024f\3\2\2\2\u024f\u0256\3\2\2\2\u0250\u024e\3")
        buf.write("\2\2\2\u0251\u0252\7\16\2\2\u0252\u0253\5\16\b\2\u0253")
        buf.write("\u0254\b\34\1\2\u0254\u0257\3\2\2\2\u0255\u0257\b\34\1")
        buf.write("\2\u0256\u0251\3\2\2\2\u0256\u0255\3\2\2\2\u0257\u0259")
        buf.write("\3\2\2\2\u0258\u0243\3\2\2\2\u0258\u0247\3\2\2\2\u0259")
        buf.write("\u0270\3\2\2\2\u025a\u025b\7?\2\2\u025b\u025c\5\16\b\2")
        buf.write("\u025c\u025d\b\34\1\2\u025d\u0270\3\2\2\2\u025e\u0264")
        buf.write("\b\34\1\2\u025f\u0260\7\16\2\2\u0260\u0261\5\16\b\2\u0261")
        buf.write("\u0262\b\34\1\2\u0262\u0265\3\2\2\2\u0263\u0265\b\34\1")
        buf.write("\2\u0264\u025f\3\2\2\2\u0264\u0263\3\2\2\2\u0265\u0270")
        buf.write("\3\2\2\2\u0266\u0267\7\13\2\2\u0267\u026d\58\35\2\u0268")
        buf.write("\u0269\7\16\2\2\u0269\u026a\5@!\2\u026a\u026b\b\34\1\2")
        buf.write("\u026b\u026e\3\2\2\2\u026c\u026e\b\34\1\2\u026d\u0268")
        buf.write("\3\2\2\2\u026d\u026c\3\2\2\2\u026e\u0270\3\2\2\2\u026f")
        buf.write("\u0241\3\2\2\2\u026f\u025a\3\2\2\2\u026f\u025e\3\2\2\2")
        buf.write("\u026f\u0266\3\2\2\2\u0270\67\3\2\2\2\u0271\u0272\5:\36")
        buf.write("\2\u0272\u0279\b\35\1\2\u0273\u0274\7\"\2\2\u0274\u0275")
        buf.write("\5:\36\2\u0275\u0276\b\35\1\2\u0276\u0278\3\2\2\2\u0277")
        buf.write("\u0273\3\2\2\2\u0278\u027b\3\2\2\2\u0279\u0277\3\2\2\2")
        buf.write("\u0279\u027a\3\2\2\2\u027a9\3\2\2\2\u027b\u0279\3\2\2")
        buf.write("\2\u027c\u027d\5\n\6\2\u027d\u027e\7.\2\2\u027e\u027f")
        buf.write("\5\16\b\2\u027f\u0280\b\36\1\2\u0280;\3\2\2\2\u0281\u0282")
        buf.write("\7=\2\2\u0282\u028c\b\37\1\2\u0283\u0284\7>\2\2\u0284")
        buf.write("\u028c\b\37\1\2\u0285\u0286\79\2\2\u0286\u028c\b\37\1")
        buf.write("\2\u0287\u0288\7:\2\2\u0288\u028c\b\37\1\2\u0289\u028a")
        buf.write("\7;\2\2\u028a\u028c\b\37\1\2\u028b\u0281\3\2\2\2\u028b")
        buf.write("\u0283\3\2\2\2\u028b\u0285\3\2\2\2\u028b\u0287\3\2\2\2")
        buf.write("\u028b\u0289\3\2\2\2\u028c=\3\2\2\2\u028d\u028e\7<\2\2")
        buf.write("\u028e\u028f\b \1\2\u028f?\3\2\2\2\u0290\u0291\5\16\b")
        buf.write("\2\u0291\u0292\b!\1\2\u0292A\3\2\2\2\u0293\u0294\5\n\6")
        buf.write("\2\u0294\u029b\b\"\1\2\u0295\u0296\7\"\2\2\u0296\u0297")
        buf.write("\5\n\6\2\u0297\u0298\b\"\1\2\u0298\u029a\3\2\2\2\u0299")
        buf.write("\u0295\3\2\2\2\u029a\u029d\3\2\2\2\u029b\u0299\3\2\2\2")
        buf.write("\u029b\u029c\3\2\2\2\u029cC\3\2\2\2\u029d\u029b\3\2\2")
        buf.write("\2\67Iajx~\u0089\u00b5\u00c5\u00e0\u00ef\u00f1\u00fe\u0100")
        buf.write("\u010b\u011b\u0128\u0130\u013a\u0145\u016a\u0176\u0178")
        buf.write("\u018d\u018f\u019b\u01a1\u01b2\u01bb\u01bd\u01c2\u01c8")
        buf.write("\u01ca\u01dd\u01e6\u01f1\u01f5\u0209\u0211\u0219\u021e")
        buf.write("\u0224\u022a\u0230\u023e\u024e\u0256\u0258\u0264\u026d")
        buf.write("\u026f\u0279\u028b\u029b")
        return buf.getvalue()


class SetlXgrammarParser ( Parser ):

    grammarFileName = "SetlXgrammar.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'if'", "'('", "')'", "'{'", "'}'", "'else'", 
                     "'switch'", "'case'", "':'", "'default'", "'for'", 
                     "'|'", "'while'", "'do'", "';'", "'backtrack'", "'break'", 
                     "'continue'", "'exit'", "'return'", "'+='", "'-='", 
                     "'*='", "'/='", "'\\='", "'%='", "':='", "'.'", "'['", 
                     "']'", "'_'", "','", "'<==>'", "'<!=>'", "'=>'", "'||'", 
                     "'&&'", "'=='", "'!='", "'<'", "'<='", "'>'", "'>='", 
                     "'in'", "'notin'", "'+'", "'-'", "'*'", "'/'", "'\\'", 
                     "'%'", "'**'", "'!'", "'procedure'", "'om'", "'true'", 
                     "'false'", "<INVALID>", "<INVALID>", "<INVALID>", "'..'" ]

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
                      "<INVALID>", "<INVALID>", "ID", "NUMBER", "DOUBLE", 
                      "RANGE_SIGN", "STRING", "LITERAL", "LINE_COMMENT", 
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
    T__51=52
    T__52=53
    T__53=54
    T__54=55
    T__55=56
    T__56=57
    ID=58
    NUMBER=59
    DOUBLE=60
    RANGE_SIGN=61
    STRING=62
    LITERAL=63
    LINE_COMMENT=64
    MULTI_COMMENT=65
    WS=66

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

        else_list = []
        caseList = []
        expression = None
        condition = None
            
        self._la = 0 # Token type
        try:
            self.state = 195
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,7,self._ctx)
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
                self.state = 95
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,1,self._ctx)
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1:
                        self.state = 83
                        self.match(SetlXgrammarParser.T__5)
                        self.state = 84
                        self.match(SetlXgrammarParser.T__0)
                        self.state = 85
                        self.match(SetlXgrammarParser.T__1)
                        self.state = 86
                        localctx.c2 = self.condition()
                        self.state = 87
                        self.match(SetlXgrammarParser.T__2)
                        self.state = 88
                        self.match(SetlXgrammarParser.T__3)
                        self.state = 89
                        localctx.b2 = self.block()
                        self.state = 90
                        self.match(SetlXgrammarParser.T__4)
                        else_list.append(IfThenBranch(localctx.c2.cnd,localctx.b2.blk)) 
                        			 
                    self.state = 97
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,1,self._ctx)

                self.state = 104
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
                if la_ == 1:
                    self.state = 98
                    self.match(SetlXgrammarParser.T__5)
                    self.state = 99
                    self.match(SetlXgrammarParser.T__3)
                    self.state = 100
                    localctx.b3 = self.block()
                    self.state = 101
                    self.match(SetlXgrammarParser.T__4)
                    else_list.append(localctx.b3.blk) 


                localctx.stmnt = IfThen(localctx.c1.cnd,localctx.b1.blk,else_list) 
                		
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 108
                self.match(SetlXgrammarParser.T__6)
                self.state = 109
                self.match(SetlXgrammarParser.T__3)
                self.state = 118
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==SetlXgrammarParser.T__7:
                    self.state = 110
                    self.match(SetlXgrammarParser.T__7)
                    self.state = 111
                    localctx.c1 = self.condition()
                    self.state = 112
                    self.match(SetlXgrammarParser.T__8)
                    self.state = 113
                    localctx.b1 = self.block()
                    caseList.append((localctx.c1.cnd, localctx.b1.blk)) 
                    self.state = 120
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 124
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==SetlXgrammarParser.T__9:
                    self.state = 121
                    self.match(SetlXgrammarParser.T__9)
                    self.state = 122
                    self.match(SetlXgrammarParser.T__8)
                    self.state = 123
                    localctx.b2 = self.block()


                self.state = 126
                self.match(SetlXgrammarParser.T__4)
                localctx.stmnt = Switch(caseList,localctx.b2.blk) 
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 128
                self.match(SetlXgrammarParser.T__10)
                self.state = 129
                self.match(SetlXgrammarParser.T__1)
                self.state = 130
                localctx._iteratorChain = self.iteratorChain(False)
                self.state = 135
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==SetlXgrammarParser.T__11:
                    self.state = 131
                    self.match(SetlXgrammarParser.T__11)
                    self.state = 132
                    localctx._condition = self.condition()
                    condition = localctx._condition.cnd


                self.state = 137
                self.match(SetlXgrammarParser.T__2)
                self.state = 138
                self.match(SetlXgrammarParser.T__3)
                self.state = 139
                localctx._block = self.block()
                self.state = 140
                self.match(SetlXgrammarParser.T__4)
                localctx.stmnt = For(localctx._iteratorChain.ic, condition, localctx._block.blk) 
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 143
                self.match(SetlXgrammarParser.T__12)
                self.state = 144
                self.match(SetlXgrammarParser.T__1)
                self.state = 145
                localctx._condition = self.condition()
                self.state = 146
                self.match(SetlXgrammarParser.T__2)
                self.state = 147
                self.match(SetlXgrammarParser.T__3)
                self.state = 148
                localctx._block = self.block()
                self.state = 149
                self.match(SetlXgrammarParser.T__4)
                localctx.stmnt = While(localctx._condition.cnd, localctx._block.blk) 
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 152
                self.match(SetlXgrammarParser.T__13)
                self.state = 153
                self.match(SetlXgrammarParser.T__3)
                self.state = 154
                localctx._block = self.block()
                self.state = 155
                self.match(SetlXgrammarParser.T__4)
                self.state = 156
                self.match(SetlXgrammarParser.T__12)
                self.state = 157
                self.match(SetlXgrammarParser.T__1)
                self.state = 158
                localctx._condition = self.condition()
                self.state = 159
                self.match(SetlXgrammarParser.T__2)
                self.state = 160
                self.match(SetlXgrammarParser.T__14)
                localctx.stmnt = DoWhile(localctx._condition.cnd, localctx._block.blk) 
                		
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 163
                self.match(SetlXgrammarParser.T__15)
                self.state = 164
                self.match(SetlXgrammarParser.T__14)
                localctx.stmnt = Backtrack() 
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 166
                self.match(SetlXgrammarParser.T__16)
                self.state = 167
                self.match(SetlXgrammarParser.T__14)
                localctx.stmnt = Break() 
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 169
                self.match(SetlXgrammarParser.T__17)
                self.state = 170
                self.match(SetlXgrammarParser.T__14)
                localctx.stmnt = Continue() 
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 172
                self.match(SetlXgrammarParser.T__18)
                self.state = 173
                self.match(SetlXgrammarParser.T__14)
                localctx.stmnt = Exit() 
                pass

            elif la_ == 10:
                self.enterOuterAlt(localctx, 10)
                self.state = 175
                self.match(SetlXgrammarParser.T__19)
                self.state = 179
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,6,self._ctx)
                if la_ == 1:
                    self.state = 176
                    localctx._expr = self.expr(False)
                    expression = localctx._expr.ex 


                self.state = 181
                self.match(SetlXgrammarParser.T__14)
                localctx.stmnt = Return(expression) 
                pass

            elif la_ == 11:
                self.enterOuterAlt(localctx, 11)
                self.state = 183
                localctx._assignmentOther = self.assignmentOther()
                self.state = 184
                self.match(SetlXgrammarParser.T__14)
                localctx.stmnt = localctx._assignmentOther.assign 
                pass

            elif la_ == 12:
                self.enterOuterAlt(localctx, 12)
                self.state = 187
                localctx._assignmentDirect = self.assignmentDirect()
                self.state = 188
                self.match(SetlXgrammarParser.T__14)
                localctx.stmnt = localctx._assignmentDirect.assign 
                pass

            elif la_ == 13:
                self.enterOuterAlt(localctx, 13)
                self.state = 191
                localctx._expr = self.expr(False)
                self.state = 192
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
            self.state = 197
            localctx._assignable = self.assignable(False)
            self.state = 222
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [SetlXgrammarParser.T__20]:
                self.state = 198
                self.match(SetlXgrammarParser.T__20)
                self.state = 199
                localctx.e = self.expr(False)
                localctx.assign = SumAssignment(localctx._assignable.a, localctx.e.ex) 
                pass
            elif token in [SetlXgrammarParser.T__21]:
                self.state = 202
                self.match(SetlXgrammarParser.T__21)
                self.state = 203
                localctx.e = self.expr(False)
                localctx.assign = DifferenceAssignment(localctx._assignable.a, localctx.e.ex) 
                pass
            elif token in [SetlXgrammarParser.T__22]:
                self.state = 206
                self.match(SetlXgrammarParser.T__22)
                self.state = 207
                localctx.e = self.expr(False)
                localctx.assign = ProductAssignment(localctx._assignable.a, localctx.e.ex) 
                pass
            elif token in [SetlXgrammarParser.T__23]:
                self.state = 210
                self.match(SetlXgrammarParser.T__23)
                self.state = 211
                localctx.e = self.expr(False)
                localctx.assign = QuotientAssignment(localctx._assignable.a, localctx.e.ex) 
                pass
            elif token in [SetlXgrammarParser.T__24]:
                self.state = 214
                self.match(SetlXgrammarParser.T__24)
                self.state = 215
                localctx.e = self.expr(False)
                localctx.assign = IntegerDivisionAssignment(localctx._assignable.a, localctx.e.ex) 
                pass
            elif token in [SetlXgrammarParser.T__25]:
                self.state = 218
                self.match(SetlXgrammarParser.T__25)
                self.state = 219
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
            self.state = 239
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,10,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 224
                localctx._variable = self.variable()
                self.state = 225
                self.match(SetlXgrammarParser.T__26)
                self.state = 226
                localctx._procedure = self.procedure()

                localctx._procedure.pd.name = localctx._variable.v.id
                localctx.assign = localctx._procedure.pd
                    
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 229
                localctx._assignable = self.assignable(False)
                self.state = 230
                self.match(SetlXgrammarParser.T__26)
                self.state = 237
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,9,self._ctx)
                if la_ == 1:
                    self.state = 231
                    localctx._assignmentDirect = self.assignmentDirect()
                    localctx.assign = Assignment(localctx._assignable.a, localctx._assignmentDirect.assign) 
                    pass

                elif la_ == 2:
                    self.state = 234
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
            self.state = 265
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,13,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 241
                localctx._assignableVariable = self.assignableVariable()
                localctx.a = localctx._assignableVariable.v
                self.state = 254
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==SetlXgrammarParser.T__27 or _la==SetlXgrammarParser.T__28:
                    self.state = 252
                    self._errHandler.sync(self)
                    token = self._input.LA(1)
                    if token in [SetlXgrammarParser.T__27]:
                        self.state = 243
                        self.match(SetlXgrammarParser.T__27)
                        self.state = 244
                        localctx._variable = self.variable()
                        localctx.a = AssignableMember(localctx.a, localctx._variable.v)
                        pass
                    elif token in [SetlXgrammarParser.T__28]:
                        self.state = 247
                        self.match(SetlXgrammarParser.T__28)
                        self.state = 248
                        self.exprList(False)
                        self.state = 249
                        self.match(SetlXgrammarParser.T__29)
                        localctx.a = AssignableCollectionAccess(localctx.a)
                        pass
                    else:
                        raise NoViableAltException(self)

                    self.state = 256
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 257
                self.match(SetlXgrammarParser.T__28)
                self.state = 258
                localctx._assignmentList = self.assignmentList()
                self.state = 259
                self.match(SetlXgrammarParser.T__29)
                localctx.a = AssignableList(localctx._assignmentList.al)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 262
                if not localctx.enableIgnore:
                    from antlr4.error.Errors import FailedPredicateException
                    raise FailedPredicateException(self, "$enableIgnore")
                self.state = 263
                self.match(SetlXgrammarParser.T__30)
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
            self.state = 267
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
            self.state = 270
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
            self.state = 273
            localctx._exprContent = self.exprContent(localctx.enableIgnore)
            localctx.exprs.append(localctx._exprContent.ex)
            self.state = 281
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==SetlXgrammarParser.T__31:
                self.state = 275
                self.match(SetlXgrammarParser.T__31)
                self.state = 276
                localctx._exprContent = self.exprContent(localctx.enableIgnore)
                localctx.exprs.append(localctx._exprContent.ex)
                self.state = 283
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
            self.enterOuterAlt(localctx, 1)
            self.state = 284
            localctx._implication = self.implication(localctx.enableIgnore)
            localctx.ex = localctx._implication.i
            self.state = 294
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [SetlXgrammarParser.T__32]:
                self.state = 286
                self.match(SetlXgrammarParser.T__32)
                self.state = 287
                localctx._implication = self.implication(localctx.enableIgnore)
                localctx.ex = BooleanEqual(localctx.ex,localctx._implication.i) 
                pass
            elif token in [SetlXgrammarParser.T__33]:
                self.state = 290
                self.match(SetlXgrammarParser.T__33)
                self.state = 291
                localctx._implication = self.implication(localctx.enableIgnore)
                localctx.ex = BooleanNotEqual(localctx.ex,localctx._implication.i) 
                pass
            elif token in [SetlXgrammarParser.T__2, SetlXgrammarParser.T__8, SetlXgrammarParser.T__11, SetlXgrammarParser.T__14, SetlXgrammarParser.T__29, SetlXgrammarParser.T__31, SetlXgrammarParser.RANGE_SIGN]:
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
        self.enterRule(localctx, 18, self.RULE_implication)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 296
            localctx._disjunction = self.disjunction(localctx.enableIgnore)
            localctx.i = localctx._disjunction.d
            self.state = 302
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==SetlXgrammarParser.T__34:
                self.state = 298
                self.match(SetlXgrammarParser.T__34)
                self.state = 299
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
        self.enterRule(localctx, 20, self.RULE_disjunction)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 304
            localctx._conjunction = self.conjunction(localctx.enableIgnore)
            localctx.d = localctx._conjunction.c
            self.state = 312
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==SetlXgrammarParser.T__35:
                self.state = 306
                self.match(SetlXgrammarParser.T__35)
                self.state = 307
                localctx._conjunction = self.conjunction(localctx.enableIgnore)
                localctx.d = Disjunction(localctx.d, localctx._conjunction.c) 
                self.state = 314
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
            self.state = 315
            localctx._comparison = self.comparison(localctx.enableIgnore)
            localctx.c = localctx._comparison.c
            self.state = 323
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==SetlXgrammarParser.T__36:
                self.state = 317
                self.match(SetlXgrammarParser.T__36)
                self.state = 318
                localctx._comparison = self.comparison(localctx.enableIgnore)
                localctx.c = Conjunction(localctx.c, localctx._comparison.c) 
                self.state = 325
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
            self.state = 326
            localctx.s1 = self.setlxSum(localctx.enableIgnore)
            localctx.c = localctx.s1.s 
            self.state = 360
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [SetlXgrammarParser.T__37]:
                self.state = 328
                self.match(SetlXgrammarParser.T__37)
                self.state = 329
                localctx.s2 = self.setlxSum(localctx.enableIgnore)
                localctx.c = Equal(localctx.s1.s,localctx.s2.s) 
                pass
            elif token in [SetlXgrammarParser.T__38]:
                self.state = 332
                self.match(SetlXgrammarParser.T__38)
                self.state = 333
                localctx.s2 = self.setlxSum(localctx.enableIgnore)
                localctx.c = NotEqual(localctx.s1.s,localctx.s2.s) 
                pass
            elif token in [SetlXgrammarParser.T__39]:
                self.state = 336
                self.match(SetlXgrammarParser.T__39)
                self.state = 337
                localctx.s2 = self.setlxSum(localctx.enableIgnore)
                localctx.c = LessThan(localctx.s1.s,localctx.s2.s) 
                pass
            elif token in [SetlXgrammarParser.T__40]:
                self.state = 340
                self.match(SetlXgrammarParser.T__40)
                self.state = 341
                localctx.s2 = self.setlxSum(localctx.enableIgnore)
                localctx.c = LessOrEqual(localctx.s1.s,localctx.s2.s) 
                pass
            elif token in [SetlXgrammarParser.T__41]:
                self.state = 344
                self.match(SetlXgrammarParser.T__41)
                self.state = 345
                localctx.s2 = self.setlxSum(localctx.enableIgnore)
                localctx.c = GreaterThan(localctx.s1.s,localctx.s2.s) 
                pass
            elif token in [SetlXgrammarParser.T__42]:
                self.state = 348
                self.match(SetlXgrammarParser.T__42)
                self.state = 349
                localctx.s2 = self.setlxSum(localctx.enableIgnore)
                localctx.c = GreaterOrEqual(localctx.s1.s,localctx.s2.s) 
                pass
            elif token in [SetlXgrammarParser.T__43]:
                self.state = 352
                self.match(SetlXgrammarParser.T__43)
                self.state = 353
                localctx.s2 = self.setlxSum(localctx.enableIgnore)
                localctx.c = In(localctx.s1.s,localctx.s2.s) 
                pass
            elif token in [SetlXgrammarParser.T__44]:
                self.state = 356
                self.match(SetlXgrammarParser.T__44)
                self.state = 357
                localctx.s2 = self.setlxSum(localctx.enableIgnore)
                localctx.c = NotIn(localctx.s1.s,localctx.s2.s) 
                pass
            elif token in [SetlXgrammarParser.T__2, SetlXgrammarParser.T__8, SetlXgrammarParser.T__11, SetlXgrammarParser.T__14, SetlXgrammarParser.T__29, SetlXgrammarParser.T__31, SetlXgrammarParser.T__32, SetlXgrammarParser.T__33, SetlXgrammarParser.T__34, SetlXgrammarParser.T__35, SetlXgrammarParser.T__36, SetlXgrammarParser.RANGE_SIGN]:
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
            self.state = 362
            localctx.p1 = self.product(localctx.enableIgnore)
            localctx.s = localctx.p1.p
            self.state = 374
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==SetlXgrammarParser.T__45 or _la==SetlXgrammarParser.T__46:
                self.state = 372
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [SetlXgrammarParser.T__45]:
                    self.state = 364
                    self.match(SetlXgrammarParser.T__45)
                    self.state = 365
                    localctx.p2 = self.product(localctx.enableIgnore)
                    localctx.s = Sum(localctx.p1.p,localctx.p2.p) 
                    pass
                elif token in [SetlXgrammarParser.T__46]:
                    self.state = 368
                    self.match(SetlXgrammarParser.T__46)
                    self.state = 369
                    localctx.p2 = self.product(localctx.enableIgnore)
                    localctx.s = Difference(localctx.p1.p,localctx.p2.p) 
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 376
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
            self.state = 377
            localctx.r1 = self.setlxReduce(localctx.enableIgnore)
            localctx.p = localctx.r1.r
            self.state = 397
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << SetlXgrammarParser.T__47) | (1 << SetlXgrammarParser.T__48) | (1 << SetlXgrammarParser.T__49) | (1 << SetlXgrammarParser.T__50))) != 0):
                self.state = 395
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [SetlXgrammarParser.T__47]:
                    self.state = 379
                    self.match(SetlXgrammarParser.T__47)
                    self.state = 380
                    localctx.r2 = self.setlxReduce(localctx.enableIgnore)
                    localctx.p = Product(localctx.p,localctx.r2.r) 
                    pass
                elif token in [SetlXgrammarParser.T__48]:
                    self.state = 383
                    self.match(SetlXgrammarParser.T__48)
                    self.state = 384
                    localctx.r2 = self.setlxReduce(localctx.enableIgnore)
                    localctx.p = Quotient(localctx.p,localctx.r2.r) 
                    pass
                elif token in [SetlXgrammarParser.T__49]:
                    self.state = 387
                    self.match(SetlXgrammarParser.T__49)
                    self.state = 388
                    localctx.r2 = self.setlxReduce(localctx.enableIgnore)
                    localctx.p = IntegerDivision(localctx.p,localctx.r2.r) 
                    pass
                elif token in [SetlXgrammarParser.T__50]:
                    self.state = 391
                    self.match(SetlXgrammarParser.T__50)
                    self.state = 392
                    localctx.r2 = self.setlxReduce(localctx.enableIgnore)
                    localctx.p = Modulo(localctx.p,localctx.r2.r) 
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 399
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
            self.state = 400
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
            self.state = 415
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,25,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 403
                localctx._factor = self.factor(localctx.enableIgnore)
                localctx.p = localctx._factor.f
                self.state = 409
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==SetlXgrammarParser.T__51:
                    self.state = 405
                    self.match(SetlXgrammarParser.T__51)
                    self.state = 406
                    localctx._prefixOperation = self.prefixOperation(localctx.enableIgnore)
                    localctx.p = Power(localctx.p,localctx._prefixOperation.p) 


                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 411
                self.match(SetlXgrammarParser.T__46)
                self.state = 412
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
            self.state = 456
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,31,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 417
                self.match(SetlXgrammarParser.T__52)
                self.state = 418
                localctx._factor = self.factor(localctx.enableIgnore)
                localctx.f = Not(localctx._factor.f) 
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 432
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [SetlXgrammarParser.T__1]:
                    self.state = 421
                    self.match(SetlXgrammarParser.T__1)
                    self.state = 422
                    localctx._exprContent = self.exprContent(localctx.enableIgnore)
                    self.state = 423
                    self.match(SetlXgrammarParser.T__2)
                    localctx.f = localctx._exprContent.ex 
                    pass
                elif token in [SetlXgrammarParser.T__53]:
                    self.state = 426
                    localctx._procedure = self.procedure()
                    localctx.f = localctx._procedure.pd 
                    pass
                elif token in [SetlXgrammarParser.ID]:
                    self.state = 429
                    localctx._variable = self.variable()
                    localctx.f = localctx._variable.v 
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 443
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << SetlXgrammarParser.T__1) | (1 << SetlXgrammarParser.T__27) | (1 << SetlXgrammarParser.T__28))) != 0):
                    self.state = 441
                    self._errHandler.sync(self)
                    token = self._input.LA(1)
                    if token in [SetlXgrammarParser.T__27]:
                        self.state = 434
                        self.match(SetlXgrammarParser.T__27)
                        self.state = 435
                        localctx._variable = self.variable()
                        localctx.f = MemberAccess(localctx.f,localctx._variable.v) 
                        pass
                    elif token in [SetlXgrammarParser.T__1, SetlXgrammarParser.T__28]:
                        self.state = 438
                        localctx._call = self.call(localctx.enableIgnore)

                        localctx._call.c.callable = localctx.f
                        localctx.f = localctx._call.c
                                
                        pass
                    else:
                        raise NoViableAltException(self)

                    self.state = 445
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 448
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==SetlXgrammarParser.T__52:
                    self.state = 446
                    self.match(SetlXgrammarParser.T__52)
                    localctx.f = Factorial(localctx.f) 


                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 450
                localctx._value = self.value(localctx.enableIgnore)
                localctx.f = localctx._value.v 
                self.state = 454
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==SetlXgrammarParser.T__52:
                    self.state = 452
                    self.match(SetlXgrammarParser.T__52)
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
            self.state = 458
            self.match(SetlXgrammarParser.T__53)
            self.state = 459
            self.match(SetlXgrammarParser.T__1)
            self.state = 460
            localctx._procedureParameters = self.procedureParameters(True)
            self.state = 461
            self.match(SetlXgrammarParser.T__2)
            self.state = 462
            self.match(SetlXgrammarParser.T__3)
            self.state = 463
            localctx._block = self.block()
            self.state = 464
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
            self.state = 499
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,35,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 467
                localctx.pp1 = self.procedureParameter(localctx.enableRw)
                localctx.paramList.append(localctx.pp1.param) 
                self.state = 475
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,32,self._ctx)
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1:
                        self.state = 469
                        self.match(SetlXgrammarParser.T__31)
                        self.state = 470
                        localctx.pp2 = self.procedureParameter(localctx.enableRw)
                        localctx.paramList.append(localctx.pp2.param)  
                    self.state = 477
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,32,self._ctx)

                self.state = 484
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==SetlXgrammarParser.T__31:
                    self.state = 478
                    self.match(SetlXgrammarParser.T__31)
                    self.state = 479
                    localctx.dp1 = self.procedureDefaultParameter()
                    localctx.paramList.append(localctx.dp1.param) 
                    self.state = 486
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 487
                localctx.dp2 = self.procedureDefaultParameter()
                localctx.paramList.append(localctx.dp2.param) 
                self.state = 495
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==SetlXgrammarParser.T__31:
                    self.state = 489
                    self.match(SetlXgrammarParser.T__31)
                    self.state = 490
                    localctx.dp3 = self.procedureDefaultParameter()
                    localctx.paramList.append(localctx.dp3.param) 
                    self.state = 497
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
            self.state = 501
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
            self.state = 504
            localctx._assignableVariable = self.assignableVariable()
            self.state = 505
            self.match(SetlXgrammarParser.T__26)
            self.state = 506
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
            self.state = 519
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [SetlXgrammarParser.T__1]:
                self.enterOuterAlt(localctx, 1)
                self.state = 509
                self.match(SetlXgrammarParser.T__1)
                self.state = 510
                localctx._callParameters = self.callParameters(localctx.enableIgnore)
                self.state = 511
                self.match(SetlXgrammarParser.T__2)
                localctx.c = FunctionCall(localctx._callParameters.params, localctx._callParameters.ex) 
                		
                pass
            elif token in [SetlXgrammarParser.T__28]:
                self.enterOuterAlt(localctx, 2)
                self.state = 514
                self.match(SetlXgrammarParser.T__28)
                self.state = 515
                localctx._collectionAccessParams = self.collectionAccessParams(localctx.enableIgnore)
                self.state = 516
                self.match(SetlXgrammarParser.T__29)
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
            self.state = 546
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,40,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 521
                localctx.e1 = self.expr(localctx.enableIgnore)
                self.state = 540
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [SetlXgrammarParser.RANGE_SIGN]:
                    self.state = 522
                    self.match(SetlXgrammarParser.RANGE_SIGN)
                    self.state = 527
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,37,self._ctx)
                    if la_ == 1:
                        self.state = 523
                        localctx.e2 = self.expr(localctx.enableIgnore)
                        localctx.p = ListRange(localctx.e1.ex,localctx.e2.ex) 
                        pass

                    elif la_ == 2:
                        localctx.p = ListRange(localctx.e1.ex,None) 
                        pass


                    pass
                elif token in [SetlXgrammarParser.T__31]:
                    self.state = 533 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    while True:
                        self.state = 529
                        self.match(SetlXgrammarParser.T__31)
                        self.state = 530
                        localctx.e3 = self.expr(False)
                        params.append(localctx.e3.ex) 
                        self.state = 535 
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)
                        if not (_la==SetlXgrammarParser.T__31):
                            break

                    localctx.p = params 
                    pass
                elif token in [SetlXgrammarParser.T__29]:
                    localctx.p = localctx.e1.ex 
                    pass
                else:
                    raise NoViableAltException(self)

                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 542
                self.match(SetlXgrammarParser.RANGE_SIGN)
                self.state = 543
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
        self.enterRule(localctx, 48, self.RULE_callParameters)

        localctx.params = []
        localctx.ex = None
            
        try:
            self.state = 552
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,41,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 548
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
            self.state = 572
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,43,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 554
                self.match(SetlXgrammarParser.T__28)
                self.state = 558
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,42,self._ctx)
                if la_ == 1:
                    self.state = 555
                    localctx._collectionBuilder = self.collectionBuilder(localctx.enableIgnore)
                    cb = localctx._collectionBuilder.cb; 


                self.state = 560
                self.match(SetlXgrammarParser.T__29)
                localctx.v = SetlXList(cb) 
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 562
                localctx._STRING = self.match(SetlXgrammarParser.STRING)
                localctx.v = SetlXString((None if localctx._STRING is None else localctx._STRING.text)) 
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 564
                localctx._LITERAL = self.match(SetlXgrammarParser.LITERAL)
                localctx.v = SetlXLiteral((None if localctx._LITERAL is None else localctx._LITERAL.text)) 
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 566
                localctx._atomicValue = self.atomicValue()
                localctx.v = localctx._atomicValue.av 
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 569
                if not localctx.enableIgnore:
                    from antlr4.error.Errors import FailedPredicateException
                    raise FailedPredicateException(self, "$enableIgnore")
                self.state = 570
                self.match(SetlXgrammarParser.T__30)
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
            self.state = 574
            localctx.e1 = self.expr(localctx.enableIgnore)
            self.state = 621
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [SetlXgrammarParser.T__31]:
                self.state = 575
                self.match(SetlXgrammarParser.T__31)
                self.state = 576
                localctx.e2 = self.expr(localctx.enableIgnore)
                self.state = 598
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [SetlXgrammarParser.RANGE_SIGN]:
                    self.state = 577
                    self.match(SetlXgrammarParser.RANGE_SIGN)
                    self.state = 578
                    localctx.e3 = self.expr(localctx.enableIgnore)
                    localctx.cb = Range(localctx.e1.ex, localctx.e2.ex, localctx.e3.ex) 
                    pass
                elif token in [SetlXgrammarParser.T__11, SetlXgrammarParser.T__29, SetlXgrammarParser.T__31]:
                    exprs.append(localctx.e1.ex); exprs.append(localctx.e2.ex) 
                    self.state = 588
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    while _la==SetlXgrammarParser.T__31:
                        self.state = 582
                        self.match(SetlXgrammarParser.T__31)
                        self.state = 583
                        localctx.e3 = self.expr(localctx.enableIgnore)
                        exprs.append(localctx.e3.ex) 
                        self.state = 590
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)

                    self.state = 596
                    self._errHandler.sync(self)
                    token = self._input.LA(1)
                    if token in [SetlXgrammarParser.T__11]:
                        self.state = 591
                        self.match(SetlXgrammarParser.T__11)
                        self.state = 592
                        localctx.e4 = self.expr(False)
                        localctx.cb = ExplicitListWithRest(exprs, localctx.e4.ex) 
                        pass
                    elif token in [SetlXgrammarParser.T__29]:
                        localctx.cb = ExplicitList(exprs)         
                        pass
                    else:
                        raise NoViableAltException(self)

                    pass
                else:
                    raise NoViableAltException(self)

                pass
            elif token in [SetlXgrammarParser.RANGE_SIGN]:
                self.state = 600
                self.match(SetlXgrammarParser.RANGE_SIGN)
                self.state = 601
                localctx.e3 = self.expr(localctx.enableIgnore)
                localctx.cb = Range(localctx.e1.ex, None, localctx.e3.ex) 
                pass
            elif token in [SetlXgrammarParser.T__11, SetlXgrammarParser.T__29]:
                exprs.append(localctx.e1.ex) 
                self.state = 610
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [SetlXgrammarParser.T__11]:
                    self.state = 605
                    self.match(SetlXgrammarParser.T__11)
                    self.state = 606
                    localctx.e2 = self.expr(False)
                    localctx.cb = ExplicitListWithRest(exprs, localctx.e2.ex) 
                    pass
                elif token in [SetlXgrammarParser.T__29]:
                    localctx.cb = ExplicitList(exprs)         
                    pass
                else:
                    raise NoViableAltException(self)

                pass
            elif token in [SetlXgrammarParser.T__8]:
                self.state = 612
                self.match(SetlXgrammarParser.T__8)
                self.state = 613
                localctx._iteratorChain = self.iteratorChain(localctx.enableIgnore)
                self.state = 619
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [SetlXgrammarParser.T__11]:
                    self.state = 614
                    self.match(SetlXgrammarParser.T__11)
                    self.state = 615
                    localctx.c1 = self.condition()
                    localctx.cb = SetlIteration(localctx.e1.ex, localctx._iteratorChain.ic, localctx.c1.cnd) 
                    pass
                elif token in [SetlXgrammarParser.T__29]:
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
            self.state = 623
            localctx.i1 = self.iterator(localctx.enableIgnore)
            localctx.ic.append(localctx.i1.iter)
            self.state = 631
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==SetlXgrammarParser.T__31:
                self.state = 625
                self.match(SetlXgrammarParser.T__31)
                self.state = 626
                localctx.i2 = self.iterator(localctx.enableIgnore)
                localctx.ic.append(localctx.i2.iter) 
                self.state = 633
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
            self.state = 634
            localctx._assignable = self.assignable(True)
            self.state = 635
            self.match(SetlXgrammarParser.T__43)
            self.state = 636
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
            self.state = 649
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [SetlXgrammarParser.NUMBER]:
                self.enterOuterAlt(localctx, 1)
                self.state = 639
                localctx._NUMBER = self.match(SetlXgrammarParser.NUMBER)
                localctx.av = SetlXFraction((None if localctx._NUMBER is None else localctx._NUMBER.text)) 
                pass
            elif token in [SetlXgrammarParser.DOUBLE]:
                self.enterOuterAlt(localctx, 2)
                self.state = 641
                localctx._DOUBLE = self.match(SetlXgrammarParser.DOUBLE)
                localctx.av = float((None if localctx._DOUBLE is None else localctx._DOUBLE.text)) 
                pass
            elif token in [SetlXgrammarParser.T__54]:
                self.enterOuterAlt(localctx, 3)
                self.state = 643
                self.match(SetlXgrammarParser.T__54)
                localctx.av = SetlXOm() 
                pass
            elif token in [SetlXgrammarParser.T__55]:
                self.enterOuterAlt(localctx, 4)
                self.state = 645
                self.match(SetlXgrammarParser.T__55)
                localctx.av = SetlXTrue() 
                pass
            elif token in [SetlXgrammarParser.T__56]:
                self.enterOuterAlt(localctx, 5)
                self.state = 647
                self.match(SetlXgrammarParser.T__56)
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
            self.state = 651
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
            self.state = 654
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
            self.state = 657
            localctx.a1 = self.assignable(True)
            localctx.al.append(localctx.a1.a) 
            self.state = 665
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==SetlXgrammarParser.T__31:
                self.state = 659
                self.match(SetlXgrammarParser.T__31)
                self.state = 660
                localctx.a2 = self.assignable(True)
                localctx.al.append(localctx.a2.a) 
                self.state = 667
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
         




