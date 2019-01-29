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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3A")
        buf.write("\u028b\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31")
        buf.write("\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36")
        buf.write("\4\37\t\37\4 \t \4!\t!\4\"\t\"\3\2\3\2\3\2\7\2H\n\2\f")
        buf.write("\2\16\2K\13\2\3\2\3\2\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3")
        buf.write("\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\7\3`\n\3\f\3\16\3")
        buf.write("c\13\3\3\3\3\3\3\3\3\3\3\3\3\3\5\3k\n\3\3\3\3\3\3\3\3")
        buf.write("\3\3\3\3\3\3\3\3\3\3\3\5\3v\n\3\3\3\3\3\3\3\3\3\3\3\3")
        buf.write("\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3")
        buf.write("\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3")
        buf.write("\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\5\3\u00a2\n\3\3")
        buf.write("\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3")
        buf.write("\5\3\u00b2\n\3\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4")
        buf.write("\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3")
        buf.write("\4\3\4\5\4\u00cd\n\4\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3")
        buf.write("\5\3\5\3\5\3\5\3\5\5\5\u00dc\n\5\5\5\u00de\n\5\3\6\3\6")
        buf.write("\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\7\6\u00eb\n\6\f\6")
        buf.write("\16\6\u00ee\13\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\5\6\u00f8")
        buf.write("\n\6\3\7\3\7\3\7\3\b\3\b\3\b\3\t\3\t\3\t\3\t\3\t\3\t\7")
        buf.write("\t\u0106\n\t\f\t\16\t\u0109\13\t\3\n\3\n\3\n\3\n\3\n\3")
        buf.write("\n\3\n\3\n\3\n\3\n\5\n\u0115\n\n\3\13\3\13\3\13\3\13\3")
        buf.write("\13\3\13\5\13\u011d\n\13\3\f\3\f\3\f\3\f\3\f\3\f\7\f\u0125")
        buf.write("\n\f\f\f\16\f\u0128\13\f\3\r\3\r\3\r\3\r\3\r\3\r\7\r\u0130")
        buf.write("\n\r\f\r\16\r\u0133\13\r\3\16\3\16\3\16\3\16\3\16\3\16")
        buf.write("\3\16\3\16\3\16\3\16\3\16\3\16\3\16\3\16\3\16\3\16\3\16")
        buf.write("\3\16\3\16\3\16\3\16\3\16\3\16\3\16\3\16\3\16\3\16\3\16")
        buf.write("\3\16\3\16\3\16\3\16\3\16\3\16\5\16\u0157\n\16\3\17\3")
        buf.write("\17\3\17\3\17\3\17\3\17\3\17\3\17\3\17\3\17\7\17\u0163")
        buf.write("\n\17\f\17\16\17\u0166\13\17\3\20\3\20\3\20\3\20\3\20")
        buf.write("\3\20\3\20\3\20\3\20\3\20\3\20\3\20\3\20\3\20\3\20\3\20")
        buf.write("\3\20\3\20\7\20\u017a\n\20\f\20\16\20\u017d\13\20\3\21")
        buf.write("\3\21\3\21\3\22\3\22\3\22\3\22\3\22\3\22\5\22\u0188\n")
        buf.write("\22\3\22\3\22\3\22\3\22\5\22\u018e\n\22\3\23\3\23\3\23")
        buf.write("\3\23\3\23\3\23\3\23\3\23\3\23\3\23\3\23\3\23\3\23\3\23")
        buf.write("\3\23\5\23\u019f\n\23\3\23\3\23\3\23\3\23\3\23\3\23\3")
        buf.write("\23\7\23\u01a8\n\23\f\23\16\23\u01ab\13\23\3\23\3\23\5")
        buf.write("\23\u01af\n\23\3\23\3\23\3\23\3\23\5\23\u01b5\n\23\5\23")
        buf.write("\u01b7\n\23\3\24\3\24\3\24\3\24\3\24\3\24\3\24\3\24\3")
        buf.write("\24\3\25\3\25\3\25\3\25\3\25\3\25\7\25\u01c8\n\25\f\25")
        buf.write("\16\25\u01cb\13\25\3\25\3\25\3\25\3\25\7\25\u01d1\n\25")
        buf.write("\f\25\16\25\u01d4\13\25\3\25\3\25\3\25\3\25\3\25\3\25")
        buf.write("\7\25\u01dc\n\25\f\25\16\25\u01df\13\25\3\25\5\25\u01e2")
        buf.write("\n\25\3\26\3\26\3\26\3\27\3\27\3\27\3\27\3\27\3\30\3\30")
        buf.write("\3\30\3\30\3\30\3\30\3\30\3\30\3\30\3\30\5\30\u01f6\n")
        buf.write("\30\3\31\3\31\3\31\3\31\3\31\3\31\5\31\u01fe\n\31\3\31")
        buf.write("\3\31\3\31\3\31\6\31\u0204\n\31\r\31\16\31\u0205\3\31")
        buf.write("\3\31\3\31\5\31\u020b\n\31\3\31\3\31\3\31\3\31\5\31\u0211")
        buf.write("\n\31\3\32\3\32\3\32\3\32\5\32\u0217\n\32\3\33\3\33\3")
        buf.write("\33\3\33\5\33\u021d\n\33\3\33\3\33\3\33\3\33\3\33\3\33")
        buf.write("\3\33\3\33\3\33\3\33\3\33\3\33\5\33\u022b\n\33\3\34\3")
        buf.write("\34\3\34\3\34\3\34\3\34\3\34\3\34\3\34\3\34\3\34\3\34")
        buf.write("\7\34\u0239\n\34\f\34\16\34\u023c\13\34\3\34\3\34\3\34")
        buf.write("\3\34\3\34\5\34\u0243\n\34\5\34\u0245\n\34\3\34\3\34\3")
        buf.write("\34\3\34\3\34\3\34\3\34\3\34\3\34\3\34\5\34\u0251\n\34")
        buf.write("\3\34\3\34\3\34\3\34\3\34\3\34\3\34\5\34\u025a\n\34\5")
        buf.write("\34\u025c\n\34\3\35\3\35\3\35\3\35\3\35\3\35\7\35\u0264")
        buf.write("\n\35\f\35\16\35\u0267\13\35\3\36\3\36\3\36\3\36\3\36")
        buf.write("\3\37\3\37\3\37\3\37\3\37\3\37\3\37\3\37\3\37\3\37\5\37")
        buf.write("\u0278\n\37\3 \3 \3 \3!\3!\3!\3\"\3\"\3\"\3\"\3\"\3\"")
        buf.write("\7\"\u0286\n\"\f\"\16\"\u0289\13\"\3\"\2\2#\2\4\6\b\n")
        buf.write("\f\16\20\22\24\26\30\32\34\36 \"$&(*,.\60\62\64\668:<")
        buf.write(">@B\2\2\2\u02c1\2I\3\2\2\2\4\u00b1\3\2\2\2\6\u00b3\3\2")
        buf.write("\2\2\b\u00dd\3\2\2\2\n\u00f7\3\2\2\2\f\u00f9\3\2\2\2\16")
        buf.write("\u00fc\3\2\2\2\20\u00ff\3\2\2\2\22\u010a\3\2\2\2\24\u0116")
        buf.write("\3\2\2\2\26\u011e\3\2\2\2\30\u0129\3\2\2\2\32\u0134\3")
        buf.write("\2\2\2\34\u0158\3\2\2\2\36\u0167\3\2\2\2 \u017e\3\2\2")
        buf.write("\2\"\u018d\3\2\2\2$\u01b6\3\2\2\2&\u01b8\3\2\2\2(\u01e1")
        buf.write("\3\2\2\2*\u01e3\3\2\2\2,\u01e6\3\2\2\2.\u01f5\3\2\2\2")
        buf.write("\60\u0210\3\2\2\2\62\u0216\3\2\2\2\64\u022a\3\2\2\2\66")
        buf.write("\u022c\3\2\2\28\u025d\3\2\2\2:\u0268\3\2\2\2<\u0277\3")
        buf.write("\2\2\2>\u0279\3\2\2\2@\u027c\3\2\2\2B\u027f\3\2\2\2DE")
        buf.write("\5\4\3\2EF\b\2\1\2FH\3\2\2\2GD\3\2\2\2HK\3\2\2\2IG\3\2")
        buf.write("\2\2IJ\3\2\2\2JL\3\2\2\2KI\3\2\2\2LM\b\2\1\2M\3\3\2\2")
        buf.write("\2NO\7\3\2\2OP\7\4\2\2PQ\5@!\2QR\7\5\2\2RS\7\6\2\2ST\5")
        buf.write("\2\2\2Ta\7\7\2\2UV\7\b\2\2VW\7\3\2\2WX\7\4\2\2XY\5@!\2")
        buf.write("YZ\7\5\2\2Z[\7\6\2\2[\\\5\2\2\2\\]\7\7\2\2]^\b\3\1\2^")
        buf.write("`\3\2\2\2_U\3\2\2\2`c\3\2\2\2a_\3\2\2\2ab\3\2\2\2bj\3")
        buf.write("\2\2\2ca\3\2\2\2de\7\b\2\2ef\7\6\2\2fg\5\2\2\2gh\7\7\2")
        buf.write("\2hi\b\3\1\2ik\3\2\2\2jd\3\2\2\2jk\3\2\2\2kl\3\2\2\2l")
        buf.write("m\b\3\1\2m\u00b2\3\2\2\2no\7\t\2\2op\7\4\2\2pu\58\35\2")
        buf.write("qr\7\n\2\2rs\5@!\2st\b\3\1\2tv\3\2\2\2uq\3\2\2\2uv\3\2")
        buf.write("\2\2vw\3\2\2\2wx\7\5\2\2xy\7\6\2\2yz\5\2\2\2z{\7\7\2\2")
        buf.write("{|\b\3\1\2|\u00b2\3\2\2\2}~\7\13\2\2~\177\7\4\2\2\177")
        buf.write("\u0080\5@!\2\u0080\u0081\7\5\2\2\u0081\u0082\7\6\2\2\u0082")
        buf.write("\u0083\5\2\2\2\u0083\u0084\7\7\2\2\u0084\u0085\b\3\1\2")
        buf.write("\u0085\u00b2\3\2\2\2\u0086\u0087\7\f\2\2\u0087\u0088\7")
        buf.write("\6\2\2\u0088\u0089\5\2\2\2\u0089\u008a\7\7\2\2\u008a\u008b")
        buf.write("\7\13\2\2\u008b\u008c\7\4\2\2\u008c\u008d\5@!\2\u008d")
        buf.write("\u008e\7\5\2\2\u008e\u008f\7\r\2\2\u008f\u0090\b\3\1\2")
        buf.write("\u0090\u00b2\3\2\2\2\u0091\u0092\7\16\2\2\u0092\u0093")
        buf.write("\7\r\2\2\u0093\u00b2\b\3\1\2\u0094\u0095\7\17\2\2\u0095")
        buf.write("\u0096\7\r\2\2\u0096\u00b2\b\3\1\2\u0097\u0098\7\20\2")
        buf.write("\2\u0098\u0099\7\r\2\2\u0099\u00b2\b\3\1\2\u009a\u009b")
        buf.write("\7\21\2\2\u009b\u009c\7\r\2\2\u009c\u00b2\b\3\1\2\u009d")
        buf.write("\u00a1\7\22\2\2\u009e\u009f\5\16\b\2\u009f\u00a0\b\3\1")
        buf.write("\2\u00a0\u00a2\3\2\2\2\u00a1\u009e\3\2\2\2\u00a1\u00a2")
        buf.write("\3\2\2\2\u00a2\u00a3\3\2\2\2\u00a3\u00a4\7\r\2\2\u00a4")
        buf.write("\u00b2\b\3\1\2\u00a5\u00a6\5\6\4\2\u00a6\u00a7\7\r\2\2")
        buf.write("\u00a7\u00a8\b\3\1\2\u00a8\u00b2\3\2\2\2\u00a9\u00aa\5")
        buf.write("\b\5\2\u00aa\u00ab\7\r\2\2\u00ab\u00ac\b\3\1\2\u00ac\u00b2")
        buf.write("\3\2\2\2\u00ad\u00ae\5\16\b\2\u00ae\u00af\7\r\2\2\u00af")
        buf.write("\u00b0\b\3\1\2\u00b0\u00b2\3\2\2\2\u00b1N\3\2\2\2\u00b1")
        buf.write("n\3\2\2\2\u00b1}\3\2\2\2\u00b1\u0086\3\2\2\2\u00b1\u0091")
        buf.write("\3\2\2\2\u00b1\u0094\3\2\2\2\u00b1\u0097\3\2\2\2\u00b1")
        buf.write("\u009a\3\2\2\2\u00b1\u009d\3\2\2\2\u00b1\u00a5\3\2\2\2")
        buf.write("\u00b1\u00a9\3\2\2\2\u00b1\u00ad\3\2\2\2\u00b2\5\3\2\2")
        buf.write("\2\u00b3\u00cc\5\n\6\2\u00b4\u00b5\7\23\2\2\u00b5\u00b6")
        buf.write("\5\16\b\2\u00b6\u00b7\b\4\1\2\u00b7\u00cd\3\2\2\2\u00b8")
        buf.write("\u00b9\7\24\2\2\u00b9\u00ba\5\16\b\2\u00ba\u00bb\b\4\1")
        buf.write("\2\u00bb\u00cd\3\2\2\2\u00bc\u00bd\7\25\2\2\u00bd\u00be")
        buf.write("\5\16\b\2\u00be\u00bf\b\4\1\2\u00bf\u00cd\3\2\2\2\u00c0")
        buf.write("\u00c1\7\26\2\2\u00c1\u00c2\5\16\b\2\u00c2\u00c3\b\4\1")
        buf.write("\2\u00c3\u00cd\3\2\2\2\u00c4\u00c5\7\27\2\2\u00c5\u00c6")
        buf.write("\5\16\b\2\u00c6\u00c7\b\4\1\2\u00c7\u00cd\3\2\2\2\u00c8")
        buf.write("\u00c9\7\30\2\2\u00c9\u00ca\5\16\b\2\u00ca\u00cb\b\4\1")
        buf.write("\2\u00cb\u00cd\3\2\2\2\u00cc\u00b4\3\2\2\2\u00cc\u00b8")
        buf.write("\3\2\2\2\u00cc\u00bc\3\2\2\2\u00cc\u00c0\3\2\2\2\u00cc")
        buf.write("\u00c4\3\2\2\2\u00cc\u00c8\3\2\2\2\u00cd\7\3\2\2\2\u00ce")
        buf.write("\u00cf\5> \2\u00cf\u00d0\7\31\2\2\u00d0\u00d1\5&\24\2")
        buf.write("\u00d1\u00d2\b\5\1\2\u00d2\u00de\3\2\2\2\u00d3\u00d4\5")
        buf.write("\n\6\2\u00d4\u00db\7\31\2\2\u00d5\u00d6\5\b\5\2\u00d6")
        buf.write("\u00d7\b\5\1\2\u00d7\u00dc\3\2\2\2\u00d8\u00d9\5\22\n")
        buf.write("\2\u00d9\u00da\b\5\1\2\u00da\u00dc\3\2\2\2\u00db\u00d5")
        buf.write("\3\2\2\2\u00db\u00d8\3\2\2\2\u00dc\u00de\3\2\2\2\u00dd")
        buf.write("\u00ce\3\2\2\2\u00dd\u00d3\3\2\2\2\u00de\t\3\2\2\2\u00df")
        buf.write("\u00e0\5\f\7\2\u00e0\u00ec\b\6\1\2\u00e1\u00e2\7\32\2")
        buf.write("\2\u00e2\u00e3\5> \2\u00e3\u00e4\b\6\1\2\u00e4\u00eb\3")
        buf.write("\2\2\2\u00e5\u00e6\7\33\2\2\u00e6\u00e7\5\20\t\2\u00e7")
        buf.write("\u00e8\7\34\2\2\u00e8\u00e9\b\6\1\2\u00e9\u00eb\3\2\2")
        buf.write("\2\u00ea\u00e1\3\2\2\2\u00ea\u00e5\3\2\2\2\u00eb\u00ee")
        buf.write("\3\2\2\2\u00ec\u00ea\3\2\2\2\u00ec\u00ed\3\2\2\2\u00ed")
        buf.write("\u00f8\3\2\2\2\u00ee\u00ec\3\2\2\2\u00ef\u00f0\7\33\2")
        buf.write("\2\u00f0\u00f1\5B\"\2\u00f1\u00f2\7\34\2\2\u00f2\u00f3")
        buf.write("\b\6\1\2\u00f3\u00f8\3\2\2\2\u00f4\u00f5\6\6\2\3\u00f5")
        buf.write("\u00f6\7\35\2\2\u00f6\u00f8\b\6\1\2\u00f7\u00df\3\2\2")
        buf.write("\2\u00f7\u00ef\3\2\2\2\u00f7\u00f4\3\2\2\2\u00f8\13\3")
        buf.write("\2\2\2\u00f9\u00fa\79\2\2\u00fa\u00fb\b\7\1\2\u00fb\r")
        buf.write("\3\2\2\2\u00fc\u00fd\5\22\n\2\u00fd\u00fe\b\b\1\2\u00fe")
        buf.write("\17\3\2\2\2\u00ff\u0100\5\22\n\2\u0100\u0107\b\t\1\2\u0101")
        buf.write("\u0102\7\36\2\2\u0102\u0103\5\22\n\2\u0103\u0104\b\t\1")
        buf.write("\2\u0104\u0106\3\2\2\2\u0105\u0101\3\2\2\2\u0106\u0109")
        buf.write("\3\2\2\2\u0107\u0105\3\2\2\2\u0107\u0108\3\2\2\2\u0108")
        buf.write("\21\3\2\2\2\u0109\u0107\3\2\2\2\u010a\u010b\5\24\13\2")
        buf.write("\u010b\u0114\b\n\1\2\u010c\u010d\7\37\2\2\u010d\u010e")
        buf.write("\5\24\13\2\u010e\u010f\b\n\1\2\u010f\u0115\3\2\2\2\u0110")
        buf.write("\u0111\7 \2\2\u0111\u0112\5\24\13\2\u0112\u0113\b\n\1")
        buf.write("\2\u0113\u0115\3\2\2\2\u0114\u010c\3\2\2\2\u0114\u0110")
        buf.write("\3\2\2\2\u0114\u0115\3\2\2\2\u0115\23\3\2\2\2\u0116\u0117")
        buf.write("\5\26\f\2\u0117\u011c\b\13\1\2\u0118\u0119\7!\2\2\u0119")
        buf.write("\u011a\5\24\13\2\u011a\u011b\b\13\1\2\u011b\u011d\3\2")
        buf.write("\2\2\u011c\u0118\3\2\2\2\u011c\u011d\3\2\2\2\u011d\25")
        buf.write("\3\2\2\2\u011e\u011f\5\30\r\2\u011f\u0126\b\f\1\2\u0120")
        buf.write("\u0121\7\"\2\2\u0121\u0122\5\30\r\2\u0122\u0123\b\f\1")
        buf.write("\2\u0123\u0125\3\2\2\2\u0124\u0120\3\2\2\2\u0125\u0128")
        buf.write("\3\2\2\2\u0126\u0124\3\2\2\2\u0126\u0127\3\2\2\2\u0127")
        buf.write("\27\3\2\2\2\u0128\u0126\3\2\2\2\u0129\u012a\5\32\16\2")
        buf.write("\u012a\u0131\b\r\1\2\u012b\u012c\7#\2\2\u012c\u012d\5")
        buf.write("\32\16\2\u012d\u012e\b\r\1\2\u012e\u0130\3\2\2\2\u012f")
        buf.write("\u012b\3\2\2\2\u0130\u0133\3\2\2\2\u0131\u012f\3\2\2\2")
        buf.write("\u0131\u0132\3\2\2\2\u0132\31\3\2\2\2\u0133\u0131\3\2")
        buf.write("\2\2\u0134\u0135\5\34\17\2\u0135\u0156\b\16\1\2\u0136")
        buf.write("\u0137\7$\2\2\u0137\u0138\5\34\17\2\u0138\u0139\b\16\1")
        buf.write("\2\u0139\u0157\3\2\2\2\u013a\u013b\7%\2\2\u013b\u013c")
        buf.write("\5\34\17\2\u013c\u013d\b\16\1\2\u013d\u0157\3\2\2\2\u013e")
        buf.write("\u013f\7&\2\2\u013f\u0140\5\34\17\2\u0140\u0141\b\16\1")
        buf.write("\2\u0141\u0157\3\2\2\2\u0142\u0143\7\'\2\2\u0143\u0144")
        buf.write("\5\34\17\2\u0144\u0145\b\16\1\2\u0145\u0157\3\2\2\2\u0146")
        buf.write("\u0147\7(\2\2\u0147\u0148\5\34\17\2\u0148\u0149\b\16\1")
        buf.write("\2\u0149\u0157\3\2\2\2\u014a\u014b\7)\2\2\u014b\u014c")
        buf.write("\5\34\17\2\u014c\u014d\b\16\1\2\u014d\u0157\3\2\2\2\u014e")
        buf.write("\u014f\7*\2\2\u014f\u0150\5\34\17\2\u0150\u0151\b\16\1")
        buf.write("\2\u0151\u0157\3\2\2\2\u0152\u0153\7+\2\2\u0153\u0154")
        buf.write("\5\34\17\2\u0154\u0155\b\16\1\2\u0155\u0157\3\2\2\2\u0156")
        buf.write("\u0136\3\2\2\2\u0156\u013a\3\2\2\2\u0156\u013e\3\2\2\2")
        buf.write("\u0156\u0142\3\2\2\2\u0156\u0146\3\2\2\2\u0156\u014a\3")
        buf.write("\2\2\2\u0156\u014e\3\2\2\2\u0156\u0152\3\2\2\2\u0156\u0157")
        buf.write("\3\2\2\2\u0157\33\3\2\2\2\u0158\u0159\5\36\20\2\u0159")
        buf.write("\u0164\b\17\1\2\u015a\u015b\7,\2\2\u015b\u015c\5\36\20")
        buf.write("\2\u015c\u015d\b\17\1\2\u015d\u0163\3\2\2\2\u015e\u015f")
        buf.write("\7-\2\2\u015f\u0160\5\36\20\2\u0160\u0161\b\17\1\2\u0161")
        buf.write("\u0163\3\2\2\2\u0162\u015a\3\2\2\2\u0162\u015e\3\2\2\2")
        buf.write("\u0163\u0166\3\2\2\2\u0164\u0162\3\2\2\2\u0164\u0165\3")
        buf.write("\2\2\2\u0165\35\3\2\2\2\u0166\u0164\3\2\2\2\u0167\u0168")
        buf.write("\5 \21\2\u0168\u017b\b\20\1\2\u0169\u016a\7.\2\2\u016a")
        buf.write("\u016b\5 \21\2\u016b\u016c\b\20\1\2\u016c\u017a\3\2\2")
        buf.write("\2\u016d\u016e\7/\2\2\u016e\u016f\5 \21\2\u016f\u0170")
        buf.write("\b\20\1\2\u0170\u017a\3\2\2\2\u0171\u0172\7\60\2\2\u0172")
        buf.write("\u0173\5 \21\2\u0173\u0174\b\20\1\2\u0174\u017a\3\2\2")
        buf.write("\2\u0175\u0176\7\61\2\2\u0176\u0177\5 \21\2\u0177\u0178")
        buf.write("\b\20\1\2\u0178\u017a\3\2\2\2\u0179\u0169\3\2\2\2\u0179")
        buf.write("\u016d\3\2\2\2\u0179\u0171\3\2\2\2\u0179\u0175\3\2\2\2")
        buf.write("\u017a\u017d\3\2\2\2\u017b\u0179\3\2\2\2\u017b\u017c\3")
        buf.write("\2\2\2\u017c\37\3\2\2\2\u017d\u017b\3\2\2\2\u017e\u017f")
        buf.write("\5\"\22\2\u017f\u0180\b\21\1\2\u0180!\3\2\2\2\u0181\u0182")
        buf.write("\5$\23\2\u0182\u0187\b\22\1\2\u0183\u0184\7\62\2\2\u0184")
        buf.write("\u0185\5\"\22\2\u0185\u0186\b\22\1\2\u0186\u0188\3\2\2")
        buf.write("\2\u0187\u0183\3\2\2\2\u0187\u0188\3\2\2\2\u0188\u018e")
        buf.write("\3\2\2\2\u0189\u018a\7-\2\2\u018a\u018b\5\"\22\2\u018b")
        buf.write("\u018c\b\22\1\2\u018c\u018e\3\2\2\2\u018d\u0181\3\2\2")
        buf.write("\2\u018d\u0189\3\2\2\2\u018e#\3\2\2\2\u018f\u0190\7\63")
        buf.write("\2\2\u0190\u0191\5$\23\2\u0191\u0192\b\23\1\2\u0192\u01b7")
        buf.write("\3\2\2\2\u0193\u0194\7\4\2\2\u0194\u0195\5\22\n\2\u0195")
        buf.write("\u0196\7\5\2\2\u0196\u0197\b\23\1\2\u0197\u019f\3\2\2")
        buf.write("\2\u0198\u0199\5&\24\2\u0199\u019a\b\23\1\2\u019a\u019f")
        buf.write("\3\2\2\2\u019b\u019c\5> \2\u019c\u019d\b\23\1\2\u019d")
        buf.write("\u019f\3\2\2\2\u019e\u0193\3\2\2\2\u019e\u0198\3\2\2\2")
        buf.write("\u019e\u019b\3\2\2\2\u019f\u01a9\3\2\2\2\u01a0\u01a1\7")
        buf.write("\32\2\2\u01a1\u01a2\5> \2\u01a2\u01a3\b\23\1\2\u01a3\u01a8")
        buf.write("\3\2\2\2\u01a4\u01a5\5.\30\2\u01a5\u01a6\b\23\1\2\u01a6")
        buf.write("\u01a8\3\2\2\2\u01a7\u01a0\3\2\2\2\u01a7\u01a4\3\2\2\2")
        buf.write("\u01a8\u01ab\3\2\2\2\u01a9\u01a7\3\2\2\2\u01a9\u01aa\3")
        buf.write("\2\2\2\u01aa\u01ae\3\2\2\2\u01ab\u01a9\3\2\2\2\u01ac\u01ad")
        buf.write("\7\63\2\2\u01ad\u01af\b\23\1\2\u01ae\u01ac\3\2\2\2\u01ae")
        buf.write("\u01af\3\2\2\2\u01af\u01b7\3\2\2\2\u01b0\u01b1\5\64\33")
        buf.write("\2\u01b1\u01b4\b\23\1\2\u01b2\u01b3\7\63\2\2\u01b3\u01b5")
        buf.write("\b\23\1\2\u01b4\u01b2\3\2\2\2\u01b4\u01b5\3\2\2\2\u01b5")
        buf.write("\u01b7\3\2\2\2\u01b6\u018f\3\2\2\2\u01b6\u019e\3\2\2\2")
        buf.write("\u01b6\u01b0\3\2\2\2\u01b7%\3\2\2\2\u01b8\u01b9\7\64\2")
        buf.write("\2\u01b9\u01ba\7\4\2\2\u01ba\u01bb\5(\25\2\u01bb\u01bc")
        buf.write("\7\5\2\2\u01bc\u01bd\7\6\2\2\u01bd\u01be\5\2\2\2\u01be")
        buf.write("\u01bf\7\7\2\2\u01bf\u01c0\b\24\1\2\u01c0\'\3\2\2\2\u01c1")
        buf.write("\u01c2\5*\26\2\u01c2\u01c9\b\25\1\2\u01c3\u01c4\7\36\2")
        buf.write("\2\u01c4\u01c5\5*\26\2\u01c5\u01c6\b\25\1\2\u01c6\u01c8")
        buf.write("\3\2\2\2\u01c7\u01c3\3\2\2\2\u01c8\u01cb\3\2\2\2\u01c9")
        buf.write("\u01c7\3\2\2\2\u01c9\u01ca\3\2\2\2\u01ca\u01d2\3\2\2\2")
        buf.write("\u01cb\u01c9\3\2\2\2\u01cc\u01cd\7\36\2\2\u01cd\u01ce")
        buf.write("\5,\27\2\u01ce\u01cf\b\25\1\2\u01cf\u01d1\3\2\2\2\u01d0")
        buf.write("\u01cc\3\2\2\2\u01d1\u01d4\3\2\2\2\u01d2\u01d0\3\2\2\2")
        buf.write("\u01d2\u01d3\3\2\2\2\u01d3\u01e2\3\2\2\2\u01d4\u01d2\3")
        buf.write("\2\2\2\u01d5\u01d6\5,\27\2\u01d6\u01dd\b\25\1\2\u01d7")
        buf.write("\u01d8\7\36\2\2\u01d8\u01d9\5,\27\2\u01d9\u01da\b\25\1")
        buf.write("\2\u01da\u01dc\3\2\2\2\u01db\u01d7\3\2\2\2\u01dc\u01df")
        buf.write("\3\2\2\2\u01dd\u01db\3\2\2\2\u01dd\u01de\3\2\2\2\u01de")
        buf.write("\u01e2\3\2\2\2\u01df\u01dd\3\2\2\2\u01e0\u01e2\3\2\2\2")
        buf.write("\u01e1\u01c1\3\2\2\2\u01e1\u01d5\3\2\2\2\u01e1\u01e0\3")
        buf.write("\2\2\2\u01e2)\3\2\2\2\u01e3\u01e4\5> \2\u01e4\u01e5\b")
        buf.write("\26\1\2\u01e5+\3\2\2\2\u01e6\u01e7\5\f\7\2\u01e7\u01e8")
        buf.write("\7\31\2\2\u01e8\u01e9\5\16\b\2\u01e9\u01ea\b\27\1\2\u01ea")
        buf.write("-\3\2\2\2\u01eb\u01ec\7\4\2\2\u01ec\u01ed\5\62\32\2\u01ed")
        buf.write("\u01ee\7\5\2\2\u01ee\u01ef\b\30\1\2\u01ef\u01f6\3\2\2")
        buf.write("\2\u01f0\u01f1\7\33\2\2\u01f1\u01f2\5\60\31\2\u01f2\u01f3")
        buf.write("\7\34\2\2\u01f3\u01f4\b\30\1\2\u01f4\u01f6\3\2\2\2\u01f5")
        buf.write("\u01eb\3\2\2\2\u01f5\u01f0\3\2\2\2\u01f6/\3\2\2\2\u01f7")
        buf.write("\u020a\5\16\b\2\u01f8\u01fd\7<\2\2\u01f9\u01fa\5\16\b")
        buf.write("\2\u01fa\u01fb\b\31\1\2\u01fb\u01fe\3\2\2\2\u01fc\u01fe")
        buf.write("\b\31\1\2\u01fd\u01f9\3\2\2\2\u01fd\u01fc\3\2\2\2\u01fe")
        buf.write("\u020b\3\2\2\2\u01ff\u0200\7\36\2\2\u0200\u0201\5\16\b")
        buf.write("\2\u0201\u0202\b\31\1\2\u0202\u0204\3\2\2\2\u0203\u01ff")
        buf.write("\3\2\2\2\u0204\u0205\3\2\2\2\u0205\u0203\3\2\2\2\u0205")
        buf.write("\u0206\3\2\2\2\u0206\u0207\3\2\2\2\u0207\u0208\b\31\1")
        buf.write("\2\u0208\u020b\3\2\2\2\u0209\u020b\b\31\1\2\u020a\u01f8")
        buf.write("\3\2\2\2\u020a\u0203\3\2\2\2\u020a\u0209\3\2\2\2\u020b")
        buf.write("\u0211\3\2\2\2\u020c\u020d\7<\2\2\u020d\u020e\5\16\b\2")
        buf.write("\u020e\u020f\b\31\1\2\u020f\u0211\3\2\2\2\u0210\u01f7")
        buf.write("\3\2\2\2\u0210\u020c\3\2\2\2\u0211\61\3\2\2\2\u0212\u0213")
        buf.write("\5\20\t\2\u0213\u0214\b\32\1\2\u0214\u0217\3\2\2\2\u0215")
        buf.write("\u0217\3\2\2\2\u0216\u0212\3\2\2\2\u0216\u0215\3\2\2\2")
        buf.write("\u0217\63\3\2\2\2\u0218\u021c\7\33\2\2\u0219\u021a\5\66")
        buf.write("\34\2\u021a\u021b\b\33\1\2\u021b\u021d\3\2\2\2\u021c\u0219")
        buf.write("\3\2\2\2\u021c\u021d\3\2\2\2\u021d\u021e\3\2\2\2\u021e")
        buf.write("\u021f\7\34\2\2\u021f\u022b\b\33\1\2\u0220\u0221\7=\2")
        buf.write("\2\u0221\u022b\b\33\1\2\u0222\u0223\7>\2\2\u0223\u022b")
        buf.write("\b\33\1\2\u0224\u0225\5<\37\2\u0225\u0226\b\33\1\2\u0226")
        buf.write("\u022b\3\2\2\2\u0227\u0228\6\33\3\3\u0228\u0229\7\35\2")
        buf.write("\2\u0229\u022b\b\33\1\2\u022a\u0218\3\2\2\2\u022a\u0220")
        buf.write("\3\2\2\2\u022a\u0222\3\2\2\2\u022a\u0224\3\2\2\2\u022a")
        buf.write("\u0227\3\2\2\2\u022b\65\3\2\2\2\u022c\u025b\5\16\b\2\u022d")
        buf.write("\u022e\7\36\2\2\u022e\u0244\5\16\b\2\u022f\u0230\7<\2")
        buf.write("\2\u0230\u0231\5\16\b\2\u0231\u0232\b\34\1\2\u0232\u0245")
        buf.write("\3\2\2\2\u0233\u023a\b\34\1\2\u0234\u0235\7\36\2\2\u0235")
        buf.write("\u0236\5\16\b\2\u0236\u0237\b\34\1\2\u0237\u0239\3\2\2")
        buf.write("\2\u0238\u0234\3\2\2\2\u0239\u023c\3\2\2\2\u023a\u0238")
        buf.write("\3\2\2\2\u023a\u023b\3\2\2\2\u023b\u0242\3\2\2\2\u023c")
        buf.write("\u023a\3\2\2\2\u023d\u023e\7\n\2\2\u023e\u023f\5\16\b")
        buf.write("\2\u023f\u0240\b\34\1\2\u0240\u0243\3\2\2\2\u0241\u0243")
        buf.write("\b\34\1\2\u0242\u023d\3\2\2\2\u0242\u0241\3\2\2\2\u0243")
        buf.write("\u0245\3\2\2\2\u0244\u022f\3\2\2\2\u0244\u0233\3\2\2\2")
        buf.write("\u0245\u025c\3\2\2\2\u0246\u0247\7<\2\2\u0247\u0248\5")
        buf.write("\16\b\2\u0248\u0249\b\34\1\2\u0249\u025c\3\2\2\2\u024a")
        buf.write("\u0250\b\34\1\2\u024b\u024c\7\n\2\2\u024c\u024d\5\16\b")
        buf.write("\2\u024d\u024e\b\34\1\2\u024e\u0251\3\2\2\2\u024f\u0251")
        buf.write("\b\34\1\2\u0250\u024b\3\2\2\2\u0250\u024f\3\2\2\2\u0251")
        buf.write("\u025c\3\2\2\2\u0252\u0253\7\65\2\2\u0253\u0259\58\35")
        buf.write("\2\u0254\u0255\7\n\2\2\u0255\u0256\5@!\2\u0256\u0257\b")
        buf.write("\34\1\2\u0257\u025a\3\2\2\2\u0258\u025a\b\34\1\2\u0259")
        buf.write("\u0254\3\2\2\2\u0259\u0258\3\2\2\2\u025a\u025c\3\2\2\2")
        buf.write("\u025b\u022d\3\2\2\2\u025b\u0246\3\2\2\2\u025b\u024a\3")
        buf.write("\2\2\2\u025b\u0252\3\2\2\2\u025c\67\3\2\2\2\u025d\u025e")
        buf.write("\5:\36\2\u025e\u0265\b\35\1\2\u025f\u0260\7\36\2\2\u0260")
        buf.write("\u0261\5:\36\2\u0261\u0262\b\35\1\2\u0262\u0264\3\2\2")
        buf.write("\2\u0263\u025f\3\2\2\2\u0264\u0267\3\2\2\2\u0265\u0263")
        buf.write("\3\2\2\2\u0265\u0266\3\2\2\2\u02669\3\2\2\2\u0267\u0265")
        buf.write("\3\2\2\2\u0268\u0269\5\n\6\2\u0269\u026a\7*\2\2\u026a")
        buf.write("\u026b\5\16\b\2\u026b\u026c\b\36\1\2\u026c;\3\2\2\2\u026d")
        buf.write("\u026e\7:\2\2\u026e\u0278\b\37\1\2\u026f\u0270\7;\2\2")
        buf.write("\u0270\u0278\b\37\1\2\u0271\u0272\7\66\2\2\u0272\u0278")
        buf.write("\b\37\1\2\u0273\u0274\7\67\2\2\u0274\u0278\b\37\1\2\u0275")
        buf.write("\u0276\78\2\2\u0276\u0278\b\37\1\2\u0277\u026d\3\2\2\2")
        buf.write("\u0277\u026f\3\2\2\2\u0277\u0271\3\2\2\2\u0277\u0273\3")
        buf.write("\2\2\2\u0277\u0275\3\2\2\2\u0278=\3\2\2\2\u0279\u027a")
        buf.write("\79\2\2\u027a\u027b\b \1\2\u027b?\3\2\2\2\u027c\u027d")
        buf.write("\5\16\b\2\u027d\u027e\b!\1\2\u027eA\3\2\2\2\u027f\u0280")
        buf.write("\5\n\6\2\u0280\u0287\b\"\1\2\u0281\u0282\7\36\2\2\u0282")
        buf.write("\u0283\5\n\6\2\u0283\u0284\b\"\1\2\u0284\u0286\3\2\2\2")
        buf.write("\u0285\u0281\3\2\2\2\u0286\u0289\3\2\2\2\u0287\u0285\3")
        buf.write("\2\2\2\u0287\u0288\3\2\2\2\u0288C\3\2\2\2\u0289\u0287")
        buf.write("\3\2\2\2\65Iaju\u00a1\u00b1\u00cc\u00db\u00dd\u00ea\u00ec")
        buf.write("\u00f7\u0107\u0114\u011c\u0126\u0131\u0156\u0162\u0164")
        buf.write("\u0179\u017b\u0187\u018d\u019e\u01a7\u01a9\u01ae\u01b4")
        buf.write("\u01b6\u01c9\u01d2\u01dd\u01e1\u01f5\u01fd\u0205\u020a")
        buf.write("\u0210\u0216\u021c\u022a\u023a\u0242\u0244\u0250\u0259")
        buf.write("\u025b\u0265\u0277\u0287")
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
                     "'['", "']'", "'_'", "','", "'<==>'", "'<!=>'", "'=>'", 
                     "'||'", "'&&'", "'=='", "'!='", "'<'", "'<='", "'>'", 
                     "'>='", "'in'", "'notin'", "'+'", "'-'", "'*'", "'/'", 
                     "'\\'", "'%'", "'**'", "'!'", "'procedure'", "':'", 
                     "'om'", "'True'", "'False'", "<INVALID>", "<INVALID>", 
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
    ID=55
    NUMBER=56
    DOUBLE=57
    RANGE_SIGN=58
    STRING=59
    LITERAL=60
    LINE_COMMENT=61
    MULTI_COMMENT=62
    WS=63

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
        expression = None
        condition = None
            
        self._la = 0 # Token type
        try:
            self.state = 175
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
                self.match(SetlXgrammarParser.T__1)
                self.state = 110
                localctx._iteratorChain = self.iteratorChain(False)
                self.state = 115
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==SetlXgrammarParser.T__7:
                    self.state = 111
                    self.match(SetlXgrammarParser.T__7)
                    self.state = 112
                    localctx._condition = self.condition()
                    condition = localctx._condition.cnd


                self.state = 117
                self.match(SetlXgrammarParser.T__2)
                self.state = 118
                self.match(SetlXgrammarParser.T__3)
                self.state = 119
                localctx._block = self.block()
                self.state = 120
                self.match(SetlXgrammarParser.T__4)
                localctx.stmnt = For(localctx._iteratorChain.ic, condition, localctx._block.blk) 
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 123
                self.match(SetlXgrammarParser.T__8)
                self.state = 124
                self.match(SetlXgrammarParser.T__1)
                self.state = 125
                localctx._condition = self.condition()
                self.state = 126
                self.match(SetlXgrammarParser.T__2)
                self.state = 127
                self.match(SetlXgrammarParser.T__3)
                self.state = 128
                localctx._block = self.block()
                self.state = 129
                self.match(SetlXgrammarParser.T__4)
                localctx.stmnt = While(localctx._condition.cnd, localctx._block.blk) 
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 132
                self.match(SetlXgrammarParser.T__9)
                self.state = 133
                self.match(SetlXgrammarParser.T__3)
                self.state = 134
                localctx._block = self.block()
                self.state = 135
                self.match(SetlXgrammarParser.T__4)
                self.state = 136
                self.match(SetlXgrammarParser.T__8)
                self.state = 137
                self.match(SetlXgrammarParser.T__1)
                self.state = 138
                localctx._condition = self.condition()
                self.state = 139
                self.match(SetlXgrammarParser.T__2)
                self.state = 140
                self.match(SetlXgrammarParser.T__10)
                localctx.stmnt = DoWhile(localctx._condition.cnd, localctx._block.blk) 
                		
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 143
                self.match(SetlXgrammarParser.T__11)
                self.state = 144
                self.match(SetlXgrammarParser.T__10)
                localctx.stmnt = Backtrack() 
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 146
                self.match(SetlXgrammarParser.T__12)
                self.state = 147
                self.match(SetlXgrammarParser.T__10)
                localctx.stmnt = Break() 
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 149
                self.match(SetlXgrammarParser.T__13)
                self.state = 150
                self.match(SetlXgrammarParser.T__10)
                localctx.stmnt = Continue() 
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 152
                self.match(SetlXgrammarParser.T__14)
                self.state = 153
                self.match(SetlXgrammarParser.T__10)
                localctx.stmnt = Exit() 
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 155
                self.match(SetlXgrammarParser.T__15)
                self.state = 159
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
                if la_ == 1:
                    self.state = 156
                    localctx._expr = self.expr(False)
                    expression = localctx._expr.ex 


                self.state = 161
                self.match(SetlXgrammarParser.T__10)
                localctx.stmnt = Return(expression) 
                pass

            elif la_ == 10:
                self.enterOuterAlt(localctx, 10)
                self.state = 163
                localctx._assignmentOther = self.assignmentOther()
                self.state = 164
                self.match(SetlXgrammarParser.T__10)
                localctx.stmnt = localctx._assignmentOther.assign 
                pass

            elif la_ == 11:
                self.enterOuterAlt(localctx, 11)
                self.state = 167
                localctx._assignmentDirect = self.assignmentDirect()
                self.state = 168
                self.match(SetlXgrammarParser.T__10)
                localctx.stmnt = localctx._assignmentDirect.assign 
                pass

            elif la_ == 12:
                self.enterOuterAlt(localctx, 12)
                self.state = 171
                localctx._expr = self.expr(False)
                self.state = 172
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
            self.state = 177
            localctx._assignable = self.assignable(False)
            self.state = 202
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [SetlXgrammarParser.T__16]:
                self.state = 178
                self.match(SetlXgrammarParser.T__16)
                self.state = 179
                localctx.e = self.expr(False)
                localctx.assign = SumAssignment(localctx._assignable.a, localctx.e.ex) 
                pass
            elif token in [SetlXgrammarParser.T__17]:
                self.state = 182
                self.match(SetlXgrammarParser.T__17)
                self.state = 183
                localctx.e = self.expr(False)
                localctx.assign = DifferenceAssignment(localctx._assignable.a, localctx.e.ex) 
                pass
            elif token in [SetlXgrammarParser.T__18]:
                self.state = 186
                self.match(SetlXgrammarParser.T__18)
                self.state = 187
                localctx.e = self.expr(False)
                localctx.assign = ProductAssignment(localctx._assignable.a, localctx.e.ex) 
                pass
            elif token in [SetlXgrammarParser.T__19]:
                self.state = 190
                self.match(SetlXgrammarParser.T__19)
                self.state = 191
                localctx.e = self.expr(False)
                localctx.assign = QuotientAssignment(localctx._assignable.a, localctx.e.ex) 
                pass
            elif token in [SetlXgrammarParser.T__20]:
                self.state = 194
                self.match(SetlXgrammarParser.T__20)
                self.state = 195
                localctx.e = self.expr(False)
                localctx.assign = IntegerDivisionAssignment(localctx._assignable.a, localctx.e.ex) 
                pass
            elif token in [SetlXgrammarParser.T__21]:
                self.state = 198
                self.match(SetlXgrammarParser.T__21)
                self.state = 199
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
            self.state = 219
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,8,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 204
                localctx._variable = self.variable()
                self.state = 205
                self.match(SetlXgrammarParser.T__22)
                self.state = 206
                localctx._procedure = self.procedure()

                localctx._procedure.pd.name = localctx._variable.v.id
                localctx.assign = localctx._procedure.pd
                    
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 209
                localctx._assignable = self.assignable(False)
                self.state = 210
                self.match(SetlXgrammarParser.T__22)
                self.state = 217
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,7,self._ctx)
                if la_ == 1:
                    self.state = 211
                    localctx._assignmentDirect = self.assignmentDirect()
                    localctx.assign = Assignment(localctx._assignable.a, localctx._assignmentDirect.assign)
                    			
                    pass

                elif la_ == 2:
                    self.state = 214
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
            self.state = 245
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,11,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 221
                localctx._assignableVariable = self.assignableVariable()
                localctx.a = localctx._assignableVariable.v
                self.state = 234
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==SetlXgrammarParser.T__23 or _la==SetlXgrammarParser.T__24:
                    self.state = 232
                    self._errHandler.sync(self)
                    token = self._input.LA(1)
                    if token in [SetlXgrammarParser.T__23]:
                        self.state = 223
                        self.match(SetlXgrammarParser.T__23)
                        self.state = 224
                        localctx._variable = self.variable()
                        localctx.a = AssignableMember(localctx.a, localctx._variable.v)
                        pass
                    elif token in [SetlXgrammarParser.T__24]:
                        self.state = 227
                        self.match(SetlXgrammarParser.T__24)
                        self.state = 228
                        self.exprList(False)
                        self.state = 229
                        self.match(SetlXgrammarParser.T__25)
                        localctx.a = AssignableCollectionAccess(localctx.a)
                        pass
                    else:
                        raise NoViableAltException(self)

                    self.state = 236
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 237
                self.match(SetlXgrammarParser.T__24)
                self.state = 238
                localctx._assignmentList = self.assignmentList()
                self.state = 239
                self.match(SetlXgrammarParser.T__25)
                localctx.a = AssignableList(localctx._assignmentList.al)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 242
                if not localctx.enableIgnore:
                    from antlr4.error.Errors import FailedPredicateException
                    raise FailedPredicateException(self, "$enableIgnore")
                self.state = 243
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
            self.state = 247
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
            self.state = 250
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
            self.state = 253
            localctx._exprContent = self.exprContent(localctx.enableIgnore)
            localctx.exprs.append(localctx._exprContent.ex)
            self.state = 261
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==SetlXgrammarParser.T__27:
                self.state = 255
                self.match(SetlXgrammarParser.T__27)
                self.state = 256
                localctx._exprContent = self.exprContent(localctx.enableIgnore)
                localctx.exprs.append(localctx._exprContent.ex)
                self.state = 263
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
            self.state = 264
            localctx._implication = self.implication(localctx.enableIgnore)
            localctx.ex = localctx._implication.i
            self.state = 274
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [SetlXgrammarParser.T__28]:
                self.state = 266
                self.match(SetlXgrammarParser.T__28)
                self.state = 267
                localctx._implication = self.implication(localctx.enableIgnore)
                localctx.ex = BooleanEqual(localctx.ex,localctx._implication.i) 
                pass
            elif token in [SetlXgrammarParser.T__29]:
                self.state = 270
                self.match(SetlXgrammarParser.T__29)
                self.state = 271
                localctx._implication = self.implication(localctx.enableIgnore)
                localctx.ex = BooleanNotEqual(localctx.ex,localctx._implication.i) 
                pass
            elif token in [SetlXgrammarParser.T__2, SetlXgrammarParser.T__7, SetlXgrammarParser.T__10, SetlXgrammarParser.T__25, SetlXgrammarParser.T__27, SetlXgrammarParser.T__50, SetlXgrammarParser.RANGE_SIGN]:
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
            self.state = 276
            localctx._disjunction = self.disjunction(localctx.enableIgnore)
            localctx.i = localctx._disjunction.d
            self.state = 282
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==SetlXgrammarParser.T__30:
                self.state = 278
                self.match(SetlXgrammarParser.T__30)
                self.state = 279
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
            self.state = 284
            localctx._conjunction = self.conjunction(localctx.enableIgnore)
            localctx.d = localctx._conjunction.c
            self.state = 292
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==SetlXgrammarParser.T__31:
                self.state = 286
                self.match(SetlXgrammarParser.T__31)
                self.state = 287
                localctx._conjunction = self.conjunction(localctx.enableIgnore)
                localctx.d = Disjunction(localctx.d, localctx._conjunction.c) 
                self.state = 294
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
            self.state = 295
            localctx._comparison = self.comparison(localctx.enableIgnore)
            localctx.c = localctx._comparison.c
            self.state = 303
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==SetlXgrammarParser.T__32:
                self.state = 297
                self.match(SetlXgrammarParser.T__32)
                self.state = 298
                localctx._comparison = self.comparison(localctx.enableIgnore)
                localctx.c = Conjunction(localctx.c, localctx._comparison.c) 
                self.state = 305
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
            self.state = 306
            localctx.s1 = self.setlxSum(localctx.enableIgnore)
            localctx.c = localctx.s1.s 
            self.state = 340
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [SetlXgrammarParser.T__33]:
                self.state = 308
                self.match(SetlXgrammarParser.T__33)
                self.state = 309
                localctx.s2 = self.setlxSum(localctx.enableIgnore)
                localctx.c = Equal(localctx.s1.s,localctx.s2.s) 
                pass
            elif token in [SetlXgrammarParser.T__34]:
                self.state = 312
                self.match(SetlXgrammarParser.T__34)
                self.state = 313
                localctx.s2 = self.setlxSum(localctx.enableIgnore)
                localctx.c = NotEqual(localctx.s1.s,localctx.s2.s) 
                pass
            elif token in [SetlXgrammarParser.T__35]:
                self.state = 316
                self.match(SetlXgrammarParser.T__35)
                self.state = 317
                localctx.s2 = self.setlxSum(localctx.enableIgnore)
                localctx.c = LessThan(localctx.s1.s,localctx.s2.s) 
                pass
            elif token in [SetlXgrammarParser.T__36]:
                self.state = 320
                self.match(SetlXgrammarParser.T__36)
                self.state = 321
                localctx.s2 = self.setlxSum(localctx.enableIgnore)
                localctx.c = LessOrEqual(localctx.s1.s,localctx.s2.s) 
                pass
            elif token in [SetlXgrammarParser.T__37]:
                self.state = 324
                self.match(SetlXgrammarParser.T__37)
                self.state = 325
                localctx.s2 = self.setlxSum(localctx.enableIgnore)
                localctx.c = GreaterThan(localctx.s1.s,localctx.s2.s) 
                pass
            elif token in [SetlXgrammarParser.T__38]:
                self.state = 328
                self.match(SetlXgrammarParser.T__38)
                self.state = 329
                localctx.s2 = self.setlxSum(localctx.enableIgnore)
                localctx.c = GreaterOrEqual(localctx.s1.s,localctx.s2.s) 
                pass
            elif token in [SetlXgrammarParser.T__39]:
                self.state = 332
                self.match(SetlXgrammarParser.T__39)
                self.state = 333
                localctx.s2 = self.setlxSum(localctx.enableIgnore)
                localctx.c = In(localctx.s1.s,localctx.s2.s) 
                pass
            elif token in [SetlXgrammarParser.T__40]:
                self.state = 336
                self.match(SetlXgrammarParser.T__40)
                self.state = 337
                localctx.s2 = self.setlxSum(localctx.enableIgnore)
                localctx.c = NotIn(localctx.s1.s,localctx.s2.s) 
                pass
            elif token in [SetlXgrammarParser.T__2, SetlXgrammarParser.T__7, SetlXgrammarParser.T__10, SetlXgrammarParser.T__25, SetlXgrammarParser.T__27, SetlXgrammarParser.T__28, SetlXgrammarParser.T__29, SetlXgrammarParser.T__30, SetlXgrammarParser.T__31, SetlXgrammarParser.T__32, SetlXgrammarParser.T__50, SetlXgrammarParser.RANGE_SIGN]:
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
            self.state = 342
            localctx.p1 = self.product(localctx.enableIgnore)
            localctx.s = localctx.p1.p
            self.state = 354
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==SetlXgrammarParser.T__41 or _la==SetlXgrammarParser.T__42:
                self.state = 352
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [SetlXgrammarParser.T__41]:
                    self.state = 344
                    self.match(SetlXgrammarParser.T__41)
                    self.state = 345
                    localctx.p2 = self.product(localctx.enableIgnore)
                    localctx.s = Sum(localctx.p1.p,localctx.p2.p) 
                    pass
                elif token in [SetlXgrammarParser.T__42]:
                    self.state = 348
                    self.match(SetlXgrammarParser.T__42)
                    self.state = 349
                    localctx.p2 = self.product(localctx.enableIgnore)
                    localctx.s = Difference(localctx.p1.p,localctx.p2.p) 
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 356
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
            self.state = 357
            localctx.r1 = self.setlxReduce(localctx.enableIgnore)
            localctx.p = localctx.r1.r
            self.state = 377
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << SetlXgrammarParser.T__43) | (1 << SetlXgrammarParser.T__44) | (1 << SetlXgrammarParser.T__45) | (1 << SetlXgrammarParser.T__46))) != 0):
                self.state = 375
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [SetlXgrammarParser.T__43]:
                    self.state = 359
                    self.match(SetlXgrammarParser.T__43)
                    self.state = 360
                    localctx.r2 = self.setlxReduce(localctx.enableIgnore)
                    localctx.p = Product(localctx.p,localctx.r2.r) 
                    pass
                elif token in [SetlXgrammarParser.T__44]:
                    self.state = 363
                    self.match(SetlXgrammarParser.T__44)
                    self.state = 364
                    localctx.r2 = self.setlxReduce(localctx.enableIgnore)
                    localctx.p = Quotient(localctx.p,localctx.r2.r) 
                    pass
                elif token in [SetlXgrammarParser.T__45]:
                    self.state = 367
                    self.match(SetlXgrammarParser.T__45)
                    self.state = 368
                    localctx.r2 = self.setlxReduce(localctx.enableIgnore)
                    localctx.p = IntegerDivision(localctx.p,localctx.r2.r) 
                    pass
                elif token in [SetlXgrammarParser.T__46]:
                    self.state = 371
                    self.match(SetlXgrammarParser.T__46)
                    self.state = 372
                    localctx.r2 = self.setlxReduce(localctx.enableIgnore)
                    localctx.p = Modulo(localctx.p,localctx.r2.r) 
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 379
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
            self.state = 380
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
            self.state = 395
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,23,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 383
                localctx._factor = self.factor(localctx.enableIgnore)
                localctx.p = localctx._factor.f
                self.state = 389
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==SetlXgrammarParser.T__47:
                    self.state = 385
                    self.match(SetlXgrammarParser.T__47)
                    self.state = 386
                    localctx._prefixOperation = self.prefixOperation(localctx.enableIgnore)
                    localctx.p = Power(localctx.p,localctx._prefixOperation.p) 


                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 391
                self.match(SetlXgrammarParser.T__42)
                self.state = 392
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
            self.state = 436
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,29,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 397
                self.match(SetlXgrammarParser.T__48)
                self.state = 398
                localctx._factor = self.factor(localctx.enableIgnore)
                localctx.f = Not(localctx._factor.f) 
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 412
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [SetlXgrammarParser.T__1]:
                    self.state = 401
                    self.match(SetlXgrammarParser.T__1)
                    self.state = 402
                    localctx._exprContent = self.exprContent(localctx.enableIgnore)
                    self.state = 403
                    self.match(SetlXgrammarParser.T__2)
                    localctx.f = localctx._exprContent.ex 
                    pass
                elif token in [SetlXgrammarParser.T__49]:
                    self.state = 406
                    localctx._procedure = self.procedure()
                    localctx.f = localctx._procedure.pd 
                    pass
                elif token in [SetlXgrammarParser.ID]:
                    self.state = 409
                    localctx._variable = self.variable()
                    localctx.f = localctx._variable.v 
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 423
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << SetlXgrammarParser.T__1) | (1 << SetlXgrammarParser.T__23) | (1 << SetlXgrammarParser.T__24))) != 0):
                    self.state = 421
                    self._errHandler.sync(self)
                    token = self._input.LA(1)
                    if token in [SetlXgrammarParser.T__23]:
                        self.state = 414
                        self.match(SetlXgrammarParser.T__23)
                        self.state = 415
                        localctx._variable = self.variable()
                        localctx.f = MemberAccess(localctx.f,localctx._variable.v) 
                        pass
                    elif token in [SetlXgrammarParser.T__1, SetlXgrammarParser.T__24]:
                        self.state = 418
                        localctx._call = self.call(localctx.enableIgnore)

                        localctx._call.c.callable = localctx.f
                        localctx.f = localctx._call.c
                                
                        pass
                    else:
                        raise NoViableAltException(self)

                    self.state = 425
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 428
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==SetlXgrammarParser.T__48:
                    self.state = 426
                    self.match(SetlXgrammarParser.T__48)
                    localctx.f = Factorial(localctx.f) 


                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 430
                localctx._value = self.value(localctx.enableIgnore)
                localctx.f = localctx._value.v 
                self.state = 434
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==SetlXgrammarParser.T__48:
                    self.state = 432
                    self.match(SetlXgrammarParser.T__48)
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
            self.state = 438
            self.match(SetlXgrammarParser.T__49)
            self.state = 439
            self.match(SetlXgrammarParser.T__1)
            self.state = 440
            localctx._procedureParameters = self.procedureParameters(True)
            self.state = 441
            self.match(SetlXgrammarParser.T__2)
            self.state = 442
            self.match(SetlXgrammarParser.T__3)
            self.state = 443
            localctx._block = self.block()
            self.state = 444
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
            self.state = 479
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,33,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 447
                localctx.pp1 = self.procedureParameter(localctx.enableRw)
                localctx.paramList.append(localctx.pp1.param) 
                self.state = 455
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,30,self._ctx)
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1:
                        self.state = 449
                        self.match(SetlXgrammarParser.T__27)
                        self.state = 450
                        localctx.pp2 = self.procedureParameter(localctx.enableRw)
                        localctx.paramList.append(localctx.pp2.param)  
                    self.state = 457
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,30,self._ctx)

                self.state = 464
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==SetlXgrammarParser.T__27:
                    self.state = 458
                    self.match(SetlXgrammarParser.T__27)
                    self.state = 459
                    localctx.dp1 = self.procedureDefaultParameter()
                    localctx.paramList.append(localctx.dp1.param) 
                    self.state = 466
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 467
                localctx.dp2 = self.procedureDefaultParameter()
                localctx.paramList.append(localctx.dp2.param) 
                self.state = 475
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==SetlXgrammarParser.T__27:
                    self.state = 469
                    self.match(SetlXgrammarParser.T__27)
                    self.state = 470
                    localctx.dp3 = self.procedureDefaultParameter()
                    localctx.paramList.append(localctx.dp3.param) 
                    self.state = 477
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
            self.state = 481
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
            self.state = 484
            localctx._assignableVariable = self.assignableVariable()
            self.state = 485
            self.match(SetlXgrammarParser.T__22)
            self.state = 486
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
            self.state = 499
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [SetlXgrammarParser.T__1]:
                self.enterOuterAlt(localctx, 1)
                self.state = 489
                self.match(SetlXgrammarParser.T__1)
                self.state = 490
                localctx._callParameters = self.callParameters(localctx.enableIgnore)
                self.state = 491
                self.match(SetlXgrammarParser.T__2)
                localctx.c = FunctionCall(localctx._callParameters.params, localctx._callParameters.ex) 
                		
                pass
            elif token in [SetlXgrammarParser.T__24]:
                self.enterOuterAlt(localctx, 2)
                self.state = 494
                self.match(SetlXgrammarParser.T__24)
                self.state = 495
                localctx._collectionAccessParams = self.collectionAccessParams(localctx.enableIgnore)
                self.state = 496
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
            self.state = 526
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,38,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 501
                localctx.e1 = self.expr(localctx.enableIgnore)
                self.state = 520
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [SetlXgrammarParser.RANGE_SIGN]:
                    self.state = 502
                    self.match(SetlXgrammarParser.RANGE_SIGN)
                    self.state = 507
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,35,self._ctx)
                    if la_ == 1:
                        self.state = 503
                        localctx.e2 = self.expr(localctx.enableIgnore)
                        localctx.p = ListRange(localctx.e1.ex,localctx.e2.ex) 
                        pass

                    elif la_ == 2:
                        localctx.p = ListRange(localctx.e1.ex,None) 
                        pass


                    pass
                elif token in [SetlXgrammarParser.T__27]:
                    self.state = 513 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    while True:
                        self.state = 509
                        self.match(SetlXgrammarParser.T__27)
                        self.state = 510
                        localctx.e3 = self.expr(False)
                        params.append(localctx.e3.ex) 
                        self.state = 515 
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)
                        if not (_la==SetlXgrammarParser.T__27):
                            break

                    localctx.p = params 
                    pass
                elif token in [SetlXgrammarParser.T__25]:
                    localctx.p = [localctx.e1.ex] 
                    pass
                else:
                    raise NoViableAltException(self)

                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 522
                self.match(SetlXgrammarParser.RANGE_SIGN)
                self.state = 523
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
            self.state = 532
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,39,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 528
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
            self.state = 552
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,41,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 534
                self.match(SetlXgrammarParser.T__24)
                self.state = 538
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,40,self._ctx)
                if la_ == 1:
                    self.state = 535
                    localctx._collectionBuilder = self.collectionBuilder(localctx.enableIgnore)
                    cb = localctx._collectionBuilder.cb; 


                self.state = 540
                self.match(SetlXgrammarParser.T__25)
                localctx.v = SetlXList(cb) 
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 542
                localctx._STRING = self.match(SetlXgrammarParser.STRING)
                localctx.v = SetlXString((None if localctx._STRING is None else localctx._STRING.text)) 
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 544
                localctx._LITERAL = self.match(SetlXgrammarParser.LITERAL)
                localctx.v = SetlXLiteral((None if localctx._LITERAL is None else localctx._LITERAL.text)) 
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 546
                localctx._atomicValue = self.atomicValue()
                localctx.v = localctx._atomicValue.av 
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 549
                if not localctx.enableIgnore:
                    from antlr4.error.Errors import FailedPredicateException
                    raise FailedPredicateException(self, "$enableIgnore")
                self.state = 550
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
            self.state = 554
            localctx.e1 = self.expr(localctx.enableIgnore)
            self.state = 601
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [SetlXgrammarParser.T__27]:
                self.state = 555
                self.match(SetlXgrammarParser.T__27)
                self.state = 556
                localctx.e2 = self.expr(localctx.enableIgnore)
                self.state = 578
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [SetlXgrammarParser.RANGE_SIGN]:
                    self.state = 557
                    self.match(SetlXgrammarParser.RANGE_SIGN)
                    self.state = 558
                    localctx.e3 = self.expr(localctx.enableIgnore)
                    localctx.cb = Range(localctx.e1.ex, localctx.e2.ex, localctx.e3.ex) 
                    pass
                elif token in [SetlXgrammarParser.T__7, SetlXgrammarParser.T__25, SetlXgrammarParser.T__27]:
                    exprs.append(localctx.e1.ex); exprs.append(localctx.e2.ex) 
                    self.state = 568
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    while _la==SetlXgrammarParser.T__27:
                        self.state = 562
                        self.match(SetlXgrammarParser.T__27)
                        self.state = 563
                        localctx.e3 = self.expr(localctx.enableIgnore)
                        exprs.append(localctx.e3.ex) 
                        self.state = 570
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)

                    self.state = 576
                    self._errHandler.sync(self)
                    token = self._input.LA(1)
                    if token in [SetlXgrammarParser.T__7]:
                        self.state = 571
                        self.match(SetlXgrammarParser.T__7)
                        self.state = 572
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
                self.state = 580
                self.match(SetlXgrammarParser.RANGE_SIGN)
                self.state = 581
                localctx.e3 = self.expr(localctx.enableIgnore)
                localctx.cb = Range(localctx.e1.ex, None, localctx.e3.ex) 
                pass
            elif token in [SetlXgrammarParser.T__7, SetlXgrammarParser.T__25]:
                exprs.append(localctx.e1.ex) 
                self.state = 590
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [SetlXgrammarParser.T__7]:
                    self.state = 585
                    self.match(SetlXgrammarParser.T__7)
                    self.state = 586
                    localctx.e2 = self.expr(False)
                    localctx.cb = ExplicitListWithRest(exprs, localctx.e2.ex) 
                    pass
                elif token in [SetlXgrammarParser.T__25]:
                    localctx.cb = ExplicitList(exprs)         
                    pass
                else:
                    raise NoViableAltException(self)

                pass
            elif token in [SetlXgrammarParser.T__50]:
                self.state = 592
                self.match(SetlXgrammarParser.T__50)
                self.state = 593
                localctx._iteratorChain = self.iteratorChain(localctx.enableIgnore)
                self.state = 599
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [SetlXgrammarParser.T__7]:
                    self.state = 594
                    self.match(SetlXgrammarParser.T__7)
                    self.state = 595
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
            self.state = 603
            localctx.i1 = self.iterator(localctx.enableIgnore)
            localctx.ic.append(localctx.i1.iter)
            self.state = 611
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==SetlXgrammarParser.T__27:
                self.state = 605
                self.match(SetlXgrammarParser.T__27)
                self.state = 606
                localctx.i2 = self.iterator(localctx.enableIgnore)
                localctx.ic.append(localctx.i2.iter) 
                self.state = 613
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
            self.state = 614
            localctx._assignable = self.assignable(True)
            self.state = 615
            self.match(SetlXgrammarParser.T__39)
            self.state = 616
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
            self.state = 629
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [SetlXgrammarParser.NUMBER]:
                self.enterOuterAlt(localctx, 1)
                self.state = 619
                localctx._NUMBER = self.match(SetlXgrammarParser.NUMBER)
                localctx.av = SetlXFraction((None if localctx._NUMBER is None else localctx._NUMBER.text)) 
                pass
            elif token in [SetlXgrammarParser.DOUBLE]:
                self.enterOuterAlt(localctx, 2)
                self.state = 621
                localctx._DOUBLE = self.match(SetlXgrammarParser.DOUBLE)
                localctx.av = float((None if localctx._DOUBLE is None else localctx._DOUBLE.text)) 
                pass
            elif token in [SetlXgrammarParser.T__51]:
                self.enterOuterAlt(localctx, 3)
                self.state = 623
                self.match(SetlXgrammarParser.T__51)
                localctx.av = SetlXOm() 
                pass
            elif token in [SetlXgrammarParser.T__52]:
                self.enterOuterAlt(localctx, 4)
                self.state = 625
                self.match(SetlXgrammarParser.T__52)
                localctx.av = SetlXTrue() 
                pass
            elif token in [SetlXgrammarParser.T__53]:
                self.enterOuterAlt(localctx, 5)
                self.state = 627
                self.match(SetlXgrammarParser.T__53)
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
            self.state = 631
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
            self.state = 634
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
            self.state = 637
            localctx.a1 = self.assignable(True)
            localctx.al.append(localctx.a1.a) 
            self.state = 645
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==SetlXgrammarParser.T__27:
                self.state = 639
                self.match(SetlXgrammarParser.T__27)
                self.state = 640
                localctx.a2 = self.assignable(True)
                localctx.al.append(localctx.a2.a) 
                self.state = 647
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
         




