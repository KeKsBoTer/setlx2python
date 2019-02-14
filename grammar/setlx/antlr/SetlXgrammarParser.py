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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3T")
        buf.write("\u035b\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31")
        buf.write("\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36")
        buf.write("\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%\3\2\3")
        buf.write("\2\3\2\7\2N\n\2\f\2\16\2Q\13\2\3\2\3\2\3\3\3\3\3\3\3\3")
        buf.write("\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\5\3b\n\3\3\3\3\3")
        buf.write("\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3")
        buf.write("\3\3\3\3\3\3\3\3\3\7\3x\n\3\f\3\16\3{\13\3\3\3\3\3\3\3")
        buf.write("\3\3\3\3\3\3\5\3\u0083\n\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3")
        buf.write("\3\3\3\3\3\3\7\3\u008f\n\3\f\3\16\3\u0092\13\3\3\3\3\3")
        buf.write("\3\3\5\3\u0097\n\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3")
        buf.write("\5\3\u00a2\n\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3")
        buf.write("\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3")
        buf.write("\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3")
        buf.write("\3\3\3\3\5\3\u00cb\n\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3")
        buf.write("\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\5\3\u00df\n\3")
        buf.write("\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3")
        buf.write("\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\5\3\u00f8\n\3\3")
        buf.write("\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4")
        buf.write("\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\5\4\u0113")
        buf.write("\n\4\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3")
        buf.write("\5\5\5\u0122\n\5\5\5\u0124\n\5\3\6\3\6\3\6\3\6\3\6\3\6")
        buf.write("\3\6\3\6\3\6\3\6\3\6\7\6\u0131\n\6\f\6\16\6\u0134\13\6")
        buf.write("\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\5\6\u013e\n\6\3\7\3\7")
        buf.write("\3\7\3\b\3\b\3\b\3\t\3\t\3\t\3\t\3\t\3\t\7\t\u014c\n\t")
        buf.write("\f\t\16\t\u014f\13\t\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3")
        buf.write("\n\3\n\3\n\3\n\3\n\5\n\u015e\n\n\5\n\u0160\n\n\3\13\3")
        buf.write("\13\3\13\3\13\3\13\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\f")
        buf.write("\3\f\7\f\u0171\n\f\f\f\16\f\u0174\13\f\5\f\u0176\n\f\3")
        buf.write("\f\5\f\u0179\n\f\3\r\3\r\3\r\3\r\3\r\3\r\5\r\u0181\n\r")
        buf.write("\3\16\3\16\3\16\3\16\3\16\3\16\7\16\u0189\n\16\f\16\16")
        buf.write("\16\u018c\13\16\3\17\3\17\3\17\3\17\3\17\3\17\7\17\u0194")
        buf.write("\n\17\f\17\16\17\u0197\13\17\3\20\3\20\3\20\3\20\3\20")
        buf.write("\3\20\3\20\3\20\3\20\3\20\3\20\3\20\3\20\3\20\3\20\3\20")
        buf.write("\3\20\3\20\3\20\3\20\3\20\3\20\3\20\3\20\3\20\3\20\3\20")
        buf.write("\3\20\3\20\3\20\3\20\3\20\3\20\3\20\5\20\u01bb\n\20\3")
        buf.write("\21\3\21\3\21\3\21\3\21\3\21\3\21\3\21\3\21\3\21\7\21")
        buf.write("\u01c7\n\21\f\21\16\21\u01ca\13\21\3\22\3\22\3\22\3\22")
        buf.write("\3\22\3\22\3\22\3\22\3\22\3\22\3\22\3\22\3\22\3\22\3\22")
        buf.write("\3\22\3\22\3\22\3\22\3\22\3\22\3\22\7\22\u01e2\n\22\f")
        buf.write("\22\16\22\u01e5\13\22\3\23\3\23\3\23\3\23\3\23\3\23\3")
        buf.write("\23\3\23\3\23\3\23\7\23\u01f1\n\23\f\23\16\23\u01f4\13")
        buf.write("\23\3\24\3\24\3\24\3\24\3\24\3\24\5\24\u01fc\n\24\3\24")
        buf.write("\3\24\3\24\3\24\3\24\3\24\3\24\3\24\3\24\3\24\3\24\3\24")
        buf.write("\3\24\3\24\3\24\3\24\5\24\u020e\n\24\3\25\3\25\3\25\3")
        buf.write("\25\3\25\3\25\3\25\3\25\3\25\3\25\3\25\3\25\3\25\3\25")
        buf.write("\3\25\3\25\3\25\3\25\3\25\3\25\3\25\3\25\3\25\3\25\3\25")
        buf.write("\3\25\3\25\3\25\3\25\3\25\3\25\5\25\u022f\n\25\3\25\3")
        buf.write("\25\3\25\3\25\3\25\3\25\3\25\7\25\u0238\n\25\f\25\16\25")
        buf.write("\u023b\13\25\3\25\3\25\5\25\u023f\n\25\3\25\3\25\3\25")
        buf.write("\3\25\5\25\u0245\n\25\5\25\u0247\n\25\3\26\3\26\3\26\3")
        buf.write("\26\3\26\3\26\3\26\3\26\3\26\3\26\3\26\3\26\3\26\3\26")
        buf.write("\3\26\3\26\3\26\3\26\3\26\3\26\3\26\3\26\3\26\3\26\3\26")
        buf.write("\3\26\3\26\5\26\u0264\n\26\3\27\3\27\3\27\3\27\3\27\3")
        buf.write("\27\7\27\u026c\n\27\f\27\16\27\u026f\13\27\3\27\3\27\3")
        buf.write("\27\3\27\7\27\u0275\n\27\f\27\16\27\u0278\13\27\3\27\3")
        buf.write("\27\3\27\3\27\5\27\u027e\n\27\3\27\3\27\3\27\3\27\3\27")
        buf.write("\3\27\7\27\u0286\n\27\f\27\16\27\u0289\13\27\3\27\3\27")
        buf.write("\3\27\3\27\5\27\u028f\n\27\3\27\3\27\3\27\3\27\5\27\u0295")
        buf.write("\n\27\3\30\3\30\3\30\3\30\3\30\3\30\3\30\3\30\5\30\u029f")
        buf.write("\n\30\3\31\3\31\3\31\3\31\3\31\3\32\3\32\3\32\3\32\3\33")
        buf.write("\3\33\3\33\3\33\3\33\3\33\3\33\3\33\3\33\3\33\5\33\u02b4")
        buf.write("\n\33\3\34\3\34\3\34\3\34\3\34\3\34\5\34\u02bc\n\34\3")
        buf.write("\34\3\34\3\34\3\34\6\34\u02c2\n\34\r\34\16\34\u02c3\3")
        buf.write("\34\3\34\3\34\5\34\u02c9\n\34\3\34\3\34\3\34\3\34\5\34")
        buf.write("\u02cf\n\34\3\35\3\35\3\35\3\35\3\35\3\35\3\35\5\35\u02d8")
        buf.write("\n\35\3\35\3\35\3\35\3\35\3\35\5\35\u02df\n\35\3\36\3")
        buf.write("\36\3\36\3\36\5\36\u02e5\n\36\3\36\3\36\3\36\3\36\3\36")
        buf.write("\3\36\5\36\u02ed\n\36\3\36\3\36\3\36\3\36\3\36\3\36\3")
        buf.write("\36\3\36\3\36\3\36\3\36\3\36\5\36\u02fb\n\36\3\37\3\37")
        buf.write("\3\37\3\37\3\37\3\37\3\37\3\37\3\37\3\37\3\37\3\37\7\37")
        buf.write("\u0309\n\37\f\37\16\37\u030c\13\37\3\37\3\37\3\37\3\37")
        buf.write("\3\37\5\37\u0313\n\37\5\37\u0315\n\37\3\37\3\37\3\37\3")
        buf.write("\37\3\37\3\37\3\37\3\37\3\37\3\37\5\37\u0321\n\37\3\37")
        buf.write("\3\37\3\37\3\37\3\37\3\37\3\37\5\37\u032a\n\37\5\37\u032c")
        buf.write("\n\37\3 \3 \3 \3 \3 \3 \7 \u0334\n \f \16 \u0337\13 \3")
        buf.write("!\3!\3!\3!\3!\3\"\3\"\3\"\3\"\3\"\3\"\3\"\3\"\3\"\3\"")
        buf.write("\5\"\u0348\n\"\3#\3#\3#\3$\3$\3$\3%\3%\3%\3%\3%\3%\7%")
        buf.write("\u0356\n%\f%\16%\u0359\13%\3%\2\2&\2\4\6\b\n\f\16\20\22")
        buf.write("\24\26\30\32\34\36 \"$&(*,.\60\62\64\668:<>@BDFH\2\2\2")
        buf.write("\u03ac\2O\3\2\2\2\4\u00f7\3\2\2\2\6\u00f9\3\2\2\2\b\u0123")
        buf.write("\3\2\2\2\n\u013d\3\2\2\2\f\u013f\3\2\2\2\16\u0142\3\2")
        buf.write("\2\2\20\u0145\3\2\2\2\22\u015f\3\2\2\2\24\u0161\3\2\2")
        buf.write("\2\26\u0178\3\2\2\2\30\u017a\3\2\2\2\32\u0182\3\2\2\2")
        buf.write("\34\u018d\3\2\2\2\36\u0198\3\2\2\2 \u01bc\3\2\2\2\"\u01cb")
        buf.write("\3\2\2\2$\u01e6\3\2\2\2&\u020d\3\2\2\2(\u0246\3\2\2\2")
        buf.write("*\u0263\3\2\2\2,\u0294\3\2\2\2.\u029e\3\2\2\2\60\u02a0")
        buf.write("\3\2\2\2\62\u02a5\3\2\2\2\64\u02b3\3\2\2\2\66\u02ce\3")
        buf.write("\2\2\28\u02de\3\2\2\2:\u02fa\3\2\2\2<\u02fc\3\2\2\2>\u032d")
        buf.write("\3\2\2\2@\u0338\3\2\2\2B\u0347\3\2\2\2D\u0349\3\2\2\2")
        buf.write("F\u034c\3\2\2\2H\u034f\3\2\2\2JK\5\4\3\2KL\b\2\1\2LN\3")
        buf.write("\2\2\2MJ\3\2\2\2NQ\3\2\2\2OM\3\2\2\2OP\3\2\2\2PR\3\2\2")
        buf.write("\2QO\3\2\2\2RS\b\2\1\2S\3\3\2\2\2TU\7\3\2\2UV\7K\2\2V")
        buf.write("W\7\4\2\2WX\5,\27\2XY\7\5\2\2YZ\7\6\2\2Za\5\2\2\2[\\\7")
        buf.write("\7\2\2\\]\7\6\2\2]^\5\2\2\2^_\7\b\2\2_`\b\3\1\2`b\3\2")
        buf.write("\2\2a[\3\2\2\2ab\3\2\2\2bc\3\2\2\2cd\7\b\2\2de\b\3\1\2")
        buf.write("e\u00f8\3\2\2\2fg\7\t\2\2gh\7\4\2\2hi\5F$\2ij\7\5\2\2")
        buf.write("jk\7\6\2\2kl\5\2\2\2ly\7\b\2\2mn\7\n\2\2no\7\t\2\2op\7")
        buf.write("\4\2\2pq\5F$\2qr\7\5\2\2rs\7\6\2\2st\5\2\2\2tu\7\b\2\2")
        buf.write("uv\b\3\1\2vx\3\2\2\2wm\3\2\2\2x{\3\2\2\2yw\3\2\2\2yz\3")
        buf.write("\2\2\2z\u0082\3\2\2\2{y\3\2\2\2|}\7\n\2\2}~\7\6\2\2~\177")
        buf.write("\5\2\2\2\177\u0080\7\b\2\2\u0080\u0081\b\3\1\2\u0081\u0083")
        buf.write("\3\2\2\2\u0082|\3\2\2\2\u0082\u0083\3\2\2\2\u0083\u0084")
        buf.write("\3\2\2\2\u0084\u0085\b\3\1\2\u0085\u00f8\3\2\2\2\u0086")
        buf.write("\u0087\7\13\2\2\u0087\u0090\7\6\2\2\u0088\u0089\7\f\2")
        buf.write("\2\u0089\u008a\5F$\2\u008a\u008b\7\r\2\2\u008b\u008c\5")
        buf.write("\2\2\2\u008c\u008d\b\3\1\2\u008d\u008f\3\2\2\2\u008e\u0088")
        buf.write("\3\2\2\2\u008f\u0092\3\2\2\2\u0090\u008e\3\2\2\2\u0090")
        buf.write("\u0091\3\2\2\2\u0091\u0096\3\2\2\2\u0092\u0090\3\2\2\2")
        buf.write("\u0093\u0094\7\16\2\2\u0094\u0095\7\r\2\2\u0095\u0097")
        buf.write("\5\2\2\2\u0096\u0093\3\2\2\2\u0096\u0097\3\2\2\2\u0097")
        buf.write("\u0098\3\2\2\2\u0098\u0099\7\b\2\2\u0099\u00f8\b\3\1\2")
        buf.write("\u009a\u009b\7\17\2\2\u009b\u009c\7\4\2\2\u009c\u00a1")
        buf.write("\5> \2\u009d\u009e\7\20\2\2\u009e\u009f\5F$\2\u009f\u00a0")
        buf.write("\b\3\1\2\u00a0\u00a2\3\2\2\2\u00a1\u009d\3\2\2\2\u00a1")
        buf.write("\u00a2\3\2\2\2\u00a2\u00a3\3\2\2\2\u00a3\u00a4\7\5\2\2")
        buf.write("\u00a4\u00a5\7\6\2\2\u00a5\u00a6\5\2\2\2\u00a6\u00a7\7")
        buf.write("\b\2\2\u00a7\u00a8\b\3\1\2\u00a8\u00f8\3\2\2\2\u00a9\u00aa")
        buf.write("\7\21\2\2\u00aa\u00ab\7\4\2\2\u00ab\u00ac\5F$\2\u00ac")
        buf.write("\u00ad\7\5\2\2\u00ad\u00ae\7\6\2\2\u00ae\u00af\5\2\2\2")
        buf.write("\u00af\u00b0\7\b\2\2\u00b0\u00b1\b\3\1\2\u00b1\u00f8\3")
        buf.write("\2\2\2\u00b2\u00b3\7\22\2\2\u00b3\u00b4\7\6\2\2\u00b4")
        buf.write("\u00b5\5\2\2\2\u00b5\u00b6\7\b\2\2\u00b6\u00b7\7\21\2")
        buf.write("\2\u00b7\u00b8\7\4\2\2\u00b8\u00b9\5F$\2\u00b9\u00ba\7")
        buf.write("\5\2\2\u00ba\u00bb\7\23\2\2\u00bb\u00bc\b\3\1\2\u00bc")
        buf.write("\u00f8\3\2\2\2\u00bd\u00be\7\24\2\2\u00be\u00bf\7\6\2")
        buf.write("\2\u00bf\u00c0\5\2\2\2\u00c0\u00ca\7\b\2\2\u00c1\u00c2")
        buf.write("\7\25\2\2\u00c2\u00c3\7\4\2\2\u00c3\u00c4\5\f\7\2\u00c4")
        buf.write("\u00c5\7\5\2\2\u00c5\u00c6\7\6\2\2\u00c6\u00c7\5\2\2\2")
        buf.write("\u00c7\u00c8\7\b\2\2\u00c8\u00c9\b\3\1\2\u00c9\u00cb\3")
        buf.write("\2\2\2\u00ca\u00c1\3\2\2\2\u00ca\u00cb\3\2\2\2\u00cb\u00cc")
        buf.write("\3\2\2\2\u00cc\u00cd\b\3\1\2\u00cd\u00f8\3\2\2\2\u00ce")
        buf.write("\u00cf\7\26\2\2\u00cf\u00d0\7\23\2\2\u00d0\u00f8\b\3\1")
        buf.write("\2\u00d1\u00d2\7\27\2\2\u00d2\u00d3\7\23\2\2\u00d3\u00f8")
        buf.write("\b\3\1\2\u00d4\u00d5\7\30\2\2\u00d5\u00d6\7\23\2\2\u00d6")
        buf.write("\u00f8\b\3\1\2\u00d7\u00d8\7\31\2\2\u00d8\u00d9\7\23\2")
        buf.write("\2\u00d9\u00f8\b\3\1\2\u00da\u00de\7\32\2\2\u00db\u00dc")
        buf.write("\5\16\b\2\u00dc\u00dd\b\3\1\2\u00dd\u00df\3\2\2\2\u00de")
        buf.write("\u00db\3\2\2\2\u00de\u00df\3\2\2\2\u00df\u00e0\3\2\2\2")
        buf.write("\u00e0\u00e1\7\23\2\2\u00e1\u00f8\b\3\1\2\u00e2\u00e3")
        buf.write("\7\33\2\2\u00e3\u00e4\7\4\2\2\u00e4\u00e5\5F$\2\u00e5")
        buf.write("\u00e6\7\34\2\2\u00e6\u00e7\5\16\b\2\u00e7\u00e8\7\5\2")
        buf.write("\2\u00e8\u00e9\7\23\2\2\u00e9\u00ea\b\3\1\2\u00ea\u00f8")
        buf.write("\3\2\2\2\u00eb\u00ec\5\6\4\2\u00ec\u00ed\7\23\2\2\u00ed")
        buf.write("\u00ee\b\3\1\2\u00ee\u00f8\3\2\2\2\u00ef\u00f0\5\b\5\2")
        buf.write("\u00f0\u00f1\7\23\2\2\u00f1\u00f2\b\3\1\2\u00f2\u00f8")
        buf.write("\3\2\2\2\u00f3\u00f4\5\16\b\2\u00f4\u00f5\7\23\2\2\u00f5")
        buf.write("\u00f6\b\3\1\2\u00f6\u00f8\3\2\2\2\u00f7T\3\2\2\2\u00f7")
        buf.write("f\3\2\2\2\u00f7\u0086\3\2\2\2\u00f7\u009a\3\2\2\2\u00f7")
        buf.write("\u00a9\3\2\2\2\u00f7\u00b2\3\2\2\2\u00f7\u00bd\3\2\2\2")
        buf.write("\u00f7\u00ce\3\2\2\2\u00f7\u00d1\3\2\2\2\u00f7\u00d4\3")
        buf.write("\2\2\2\u00f7\u00d7\3\2\2\2\u00f7\u00da\3\2\2\2\u00f7\u00e2")
        buf.write("\3\2\2\2\u00f7\u00eb\3\2\2\2\u00f7\u00ef\3\2\2\2\u00f7")
        buf.write("\u00f3\3\2\2\2\u00f8\5\3\2\2\2\u00f9\u0112\5\n\6\2\u00fa")
        buf.write("\u00fb\7\35\2\2\u00fb\u00fc\5\16\b\2\u00fc\u00fd\b\4\1")
        buf.write("\2\u00fd\u0113\3\2\2\2\u00fe\u00ff\7\36\2\2\u00ff\u0100")
        buf.write("\5\16\b\2\u0100\u0101\b\4\1\2\u0101\u0113\3\2\2\2\u0102")
        buf.write("\u0103\7\37\2\2\u0103\u0104\5\16\b\2\u0104\u0105\b\4\1")
        buf.write("\2\u0105\u0113\3\2\2\2\u0106\u0107\7 \2\2\u0107\u0108")
        buf.write("\5\16\b\2\u0108\u0109\b\4\1\2\u0109\u0113\3\2\2\2\u010a")
        buf.write("\u010b\7!\2\2\u010b\u010c\5\16\b\2\u010c\u010d\b\4\1\2")
        buf.write("\u010d\u0113\3\2\2\2\u010e\u010f\7\"\2\2\u010f\u0110\5")
        buf.write("\16\b\2\u0110\u0111\b\4\1\2\u0111\u0113\3\2\2\2\u0112")
        buf.write("\u00fa\3\2\2\2\u0112\u00fe\3\2\2\2\u0112\u0102\3\2\2\2")
        buf.write("\u0112\u0106\3\2\2\2\u0112\u010a\3\2\2\2\u0112\u010e\3")
        buf.write("\2\2\2\u0113\7\3\2\2\2\u0114\u0115\5D#\2\u0115\u0116\7")
        buf.write("#\2\2\u0116\u0117\5*\26\2\u0117\u0118\b\5\1\2\u0118\u0124")
        buf.write("\3\2\2\2\u0119\u011a\5\n\6\2\u011a\u0121\7#\2\2\u011b")
        buf.write("\u011c\5\b\5\2\u011c\u011d\b\5\1\2\u011d\u0122\3\2\2\2")
        buf.write("\u011e\u011f\5\22\n\2\u011f\u0120\b\5\1\2\u0120\u0122")
        buf.write("\3\2\2\2\u0121\u011b\3\2\2\2\u0121\u011e\3\2\2\2\u0122")
        buf.write("\u0124\3\2\2\2\u0123\u0114\3\2\2\2\u0123\u0119\3\2\2\2")
        buf.write("\u0124\t\3\2\2\2\u0125\u0126\5\f\7\2\u0126\u0132\b\6\1")
        buf.write("\2\u0127\u0128\7$\2\2\u0128\u0129\5D#\2\u0129\u012a\b")
        buf.write("\6\1\2\u012a\u0131\3\2\2\2\u012b\u012c\7%\2\2\u012c\u012d")
        buf.write("\5\20\t\2\u012d\u012e\7&\2\2\u012e\u012f\b\6\1\2\u012f")
        buf.write("\u0131\3\2\2\2\u0130\u0127\3\2\2\2\u0130\u012b\3\2\2\2")
        buf.write("\u0131\u0134\3\2\2\2\u0132\u0130\3\2\2\2\u0132\u0133\3")
        buf.write("\2\2\2\u0133\u013e\3\2\2\2\u0134\u0132\3\2\2\2\u0135\u0136")
        buf.write("\7%\2\2\u0136\u0137\5H%\2\u0137\u0138\7&\2\2\u0138\u0139")
        buf.write("\b\6\1\2\u0139\u013e\3\2\2\2\u013a\u013b\6\6\2\3\u013b")
        buf.write("\u013c\7\'\2\2\u013c\u013e\b\6\1\2\u013d\u0125\3\2\2\2")
        buf.write("\u013d\u0135\3\2\2\2\u013d\u013a\3\2\2\2\u013e\13\3\2")
        buf.write("\2\2\u013f\u0140\7K\2\2\u0140\u0141\b\7\1\2\u0141\r\3")
        buf.write("\2\2\2\u0142\u0143\5\22\n\2\u0143\u0144\b\b\1\2\u0144")
        buf.write("\17\3\2\2\2\u0145\u0146\5\22\n\2\u0146\u014d\b\t\1\2\u0147")
        buf.write("\u0148\7\34\2\2\u0148\u0149\5\22\n\2\u0149\u014a\b\t\1")
        buf.write("\2\u014a\u014c\3\2\2\2\u014b\u0147\3\2\2\2\u014c\u014f")
        buf.write("\3\2\2\2\u014d\u014b\3\2\2\2\u014d\u014e\3\2\2\2\u014e")
        buf.write("\21\3\2\2\2\u014f\u014d\3\2\2\2\u0150\u0151\5\24\13\2")
        buf.write("\u0151\u0152\b\n\1\2\u0152\u0160\3\2\2\2\u0153\u0154\5")
        buf.write("\30\r\2\u0154\u015d\b\n\1\2\u0155\u0156\7(\2\2\u0156\u0157")
        buf.write("\5\30\r\2\u0157\u0158\b\n\1\2\u0158\u015e\3\2\2\2\u0159")
        buf.write("\u015a\7)\2\2\u015a\u015b\5\30\r\2\u015b\u015c\b\n\1\2")
        buf.write("\u015c\u015e\3\2\2\2\u015d\u0155\3\2\2\2\u015d\u0159\3")
        buf.write("\2\2\2\u015d\u015e\3\2\2\2\u015e\u0160\3\2\2\2\u015f\u0150")
        buf.write("\3\2\2\2\u015f\u0153\3\2\2\2\u0160\23\3\2\2\2\u0161\u0162")
        buf.write("\5\26\f\2\u0162\u0163\7*\2\2\u0163\u0164\5\16\b\2\u0164")
        buf.write("\u0165\b\13\1\2\u0165\25\3\2\2\2\u0166\u0167\5D#\2\u0167")
        buf.write("\u0168\b\f\1\2\u0168\u0179\3\2\2\2\u0169\u0175\7%\2\2")
        buf.write("\u016a\u016b\5D#\2\u016b\u0172\b\f\1\2\u016c\u016d\7\34")
        buf.write("\2\2\u016d\u016e\5D#\2\u016e\u016f\b\f\1\2\u016f\u0171")
        buf.write("\3\2\2\2\u0170\u016c\3\2\2\2\u0171\u0174\3\2\2\2\u0172")
        buf.write("\u0170\3\2\2\2\u0172\u0173\3\2\2\2\u0173\u0176\3\2\2\2")
        buf.write("\u0174\u0172\3\2\2\2\u0175\u016a\3\2\2\2\u0175\u0176\3")
        buf.write("\2\2\2\u0176\u0177\3\2\2\2\u0177\u0179\7&\2\2\u0178\u0166")
        buf.write("\3\2\2\2\u0178\u0169\3\2\2\2\u0179\27\3\2\2\2\u017a\u017b")
        buf.write("\5\32\16\2\u017b\u0180\b\r\1\2\u017c\u017d\7+\2\2\u017d")
        buf.write("\u017e\5\30\r\2\u017e\u017f\b\r\1\2\u017f\u0181\3\2\2")
        buf.write("\2\u0180\u017c\3\2\2\2\u0180\u0181\3\2\2\2\u0181\31\3")
        buf.write("\2\2\2\u0182\u0183\5\34\17\2\u0183\u018a\b\16\1\2\u0184")
        buf.write("\u0185\7,\2\2\u0185\u0186\5\34\17\2\u0186\u0187\b\16\1")
        buf.write("\2\u0187\u0189\3\2\2\2\u0188\u0184\3\2\2\2\u0189\u018c")
        buf.write("\3\2\2\2\u018a\u0188\3\2\2\2\u018a\u018b\3\2\2\2\u018b")
        buf.write("\33\3\2\2\2\u018c\u018a\3\2\2\2\u018d\u018e\5\36\20\2")
        buf.write("\u018e\u0195\b\17\1\2\u018f\u0190\7-\2\2\u0190\u0191\5")
        buf.write("\36\20\2\u0191\u0192\b\17\1\2\u0192\u0194\3\2\2\2\u0193")
        buf.write("\u018f\3\2\2\2\u0194\u0197\3\2\2\2\u0195\u0193\3\2\2\2")
        buf.write("\u0195\u0196\3\2\2\2\u0196\35\3\2\2\2\u0197\u0195\3\2")
        buf.write("\2\2\u0198\u0199\5 \21\2\u0199\u01ba\b\20\1\2\u019a\u019b")
        buf.write("\7.\2\2\u019b\u019c\5 \21\2\u019c\u019d\b\20\1\2\u019d")
        buf.write("\u01bb\3\2\2\2\u019e\u019f\7/\2\2\u019f\u01a0\5 \21\2")
        buf.write("\u01a0\u01a1\b\20\1\2\u01a1\u01bb\3\2\2\2\u01a2\u01a3")
        buf.write("\7\60\2\2\u01a3\u01a4\5 \21\2\u01a4\u01a5\b\20\1\2\u01a5")
        buf.write("\u01bb\3\2\2\2\u01a6\u01a7\7\61\2\2\u01a7\u01a8\5 \21")
        buf.write("\2\u01a8\u01a9\b\20\1\2\u01a9\u01bb\3\2\2\2\u01aa\u01ab")
        buf.write("\7\62\2\2\u01ab\u01ac\5 \21\2\u01ac\u01ad\b\20\1\2\u01ad")
        buf.write("\u01bb\3\2\2\2\u01ae\u01af\7\63\2\2\u01af\u01b0\5 \21")
        buf.write("\2\u01b0\u01b1\b\20\1\2\u01b1\u01bb\3\2\2\2\u01b2\u01b3")
        buf.write("\7\64\2\2\u01b3\u01b4\5 \21\2\u01b4\u01b5\b\20\1\2\u01b5")
        buf.write("\u01bb\3\2\2\2\u01b6\u01b7\7\65\2\2\u01b7\u01b8\5 \21")
        buf.write("\2\u01b8\u01b9\b\20\1\2\u01b9\u01bb\3\2\2\2\u01ba\u019a")
        buf.write("\3\2\2\2\u01ba\u019e\3\2\2\2\u01ba\u01a2\3\2\2\2\u01ba")
        buf.write("\u01a6\3\2\2\2\u01ba\u01aa\3\2\2\2\u01ba\u01ae\3\2\2\2")
        buf.write("\u01ba\u01b2\3\2\2\2\u01ba\u01b6\3\2\2\2\u01ba\u01bb\3")
        buf.write("\2\2\2\u01bb\37\3\2\2\2\u01bc\u01bd\5\"\22\2\u01bd\u01c8")
        buf.write("\b\21\1\2\u01be\u01bf\7\66\2\2\u01bf\u01c0\5\"\22\2\u01c0")
        buf.write("\u01c1\b\21\1\2\u01c1\u01c7\3\2\2\2\u01c2\u01c3\7\67\2")
        buf.write("\2\u01c3\u01c4\5\"\22\2\u01c4\u01c5\b\21\1\2\u01c5\u01c7")
        buf.write("\3\2\2\2\u01c6\u01be\3\2\2\2\u01c6\u01c2\3\2\2\2\u01c7")
        buf.write("\u01ca\3\2\2\2\u01c8\u01c6\3\2\2\2\u01c8\u01c9\3\2\2\2")
        buf.write("\u01c9!\3\2\2\2\u01ca\u01c8\3\2\2\2\u01cb\u01cc\5$\23")
        buf.write("\2\u01cc\u01e3\b\22\1\2\u01cd\u01ce\78\2\2\u01ce\u01cf")
        buf.write("\5$\23\2\u01cf\u01d0\b\22\1\2\u01d0\u01e2\3\2\2\2\u01d1")
        buf.write("\u01d2\79\2\2\u01d2\u01d3\5$\23\2\u01d3\u01d4\b\22\1\2")
        buf.write("\u01d4\u01e2\3\2\2\2\u01d5\u01d6\7:\2\2\u01d6\u01d7\5")
        buf.write("$\23\2\u01d7\u01d8\b\22\1\2\u01d8\u01e2\3\2\2\2\u01d9")
        buf.write("\u01da\7;\2\2\u01da\u01db\5$\23\2\u01db\u01dc\b\22\1\2")
        buf.write("\u01dc\u01e2\3\2\2\2\u01dd\u01de\7<\2\2\u01de\u01df\5")
        buf.write("$\23\2\u01df\u01e0\b\22\1\2\u01e0\u01e2\3\2\2\2\u01e1")
        buf.write("\u01cd\3\2\2\2\u01e1\u01d1\3\2\2\2\u01e1\u01d5\3\2\2\2")
        buf.write("\u01e1\u01d9\3\2\2\2\u01e1\u01dd\3\2\2\2\u01e2\u01e5\3")
        buf.write("\2\2\2\u01e3\u01e1\3\2\2\2\u01e3\u01e4\3\2\2\2\u01e4#")
        buf.write("\3\2\2\2\u01e5\u01e3\3\2\2\2\u01e6\u01e7\5&\24\2\u01e7")
        buf.write("\u01f2\b\23\1\2\u01e8\u01e9\7=\2\2\u01e9\u01ea\5&\24\2")
        buf.write("\u01ea\u01eb\b\23\1\2\u01eb\u01f1\3\2\2\2\u01ec\u01ed")
        buf.write("\7>\2\2\u01ed\u01ee\5&\24\2\u01ee\u01ef\b\23\1\2\u01ef")
        buf.write("\u01f1\3\2\2\2\u01f0\u01e8\3\2\2\2\u01f0\u01ec\3\2\2\2")
        buf.write("\u01f1\u01f4\3\2\2\2\u01f2\u01f0\3\2\2\2\u01f2\u01f3\3")
        buf.write("\2\2\2\u01f3%\3\2\2\2\u01f4\u01f2\3\2\2\2\u01f5\u01f6")
        buf.write("\5(\25\2\u01f6\u01fb\b\24\1\2\u01f7\u01f8\7?\2\2\u01f8")
        buf.write("\u01f9\5&\24\2\u01f9\u01fa\b\24\1\2\u01fa\u01fc\3\2\2")
        buf.write("\2\u01fb\u01f7\3\2\2\2\u01fb\u01fc\3\2\2\2\u01fc\u020e")
        buf.write("\3\2\2\2\u01fd\u01fe\7=\2\2\u01fe\u01ff\5&\24\2\u01ff")
        buf.write("\u0200\b\24\1\2\u0200\u020e\3\2\2\2\u0201\u0202\7>\2\2")
        buf.write("\u0202\u0203\5&\24\2\u0203\u0204\b\24\1\2\u0204\u020e")
        buf.write("\3\2\2\2\u0205\u0206\7@\2\2\u0206\u0207\5&\24\2\u0207")
        buf.write("\u0208\b\24\1\2\u0208\u020e\3\2\2\2\u0209\u020a\7\67\2")
        buf.write("\2\u020a\u020b\5&\24\2\u020b\u020c\b\24\1\2\u020c\u020e")
        buf.write("\3\2\2\2\u020d\u01f5\3\2\2\2\u020d\u01fd\3\2\2\2\u020d")
        buf.write("\u0201\3\2\2\2\u020d\u0205\3\2\2\2\u020d\u0209\3\2\2\2")
        buf.write("\u020e\'\3\2\2\2\u020f\u0210\7A\2\2\u0210\u0211\5(\25")
        buf.write("\2\u0211\u0212\b\25\1\2\u0212\u0247\3\2\2\2\u0213\u0214")
        buf.write("\7B\2\2\u0214\u0215\7\4\2\2\u0215\u0216\5> \2\u0216\u0217")
        buf.write("\7\20\2\2\u0217\u0218\5F$\2\u0218\u0219\7\5\2\2\u0219")
        buf.write("\u021a\b\25\1\2\u021a\u0247\3\2\2\2\u021b\u021c\7C\2\2")
        buf.write("\u021c\u021d\7\4\2\2\u021d\u021e\5> \2\u021e\u021f\7\20")
        buf.write("\2\2\u021f\u0220\5F$\2\u0220\u0221\7\5\2\2\u0221\u0222")
        buf.write("\b\25\1\2\u0222\u0247\3\2\2\2\u0223\u0224\7\4\2\2\u0224")
        buf.write("\u0225\5\22\n\2\u0225\u0226\7\5\2\2\u0226\u0227\b\25\1")
        buf.write("\2\u0227\u022f\3\2\2\2\u0228\u0229\5*\26\2\u0229\u022a")
        buf.write("\b\25\1\2\u022a\u022f\3\2\2\2\u022b\u022c\5D#\2\u022c")
        buf.write("\u022d\b\25\1\2\u022d\u022f\3\2\2\2\u022e\u0223\3\2\2")
        buf.write("\2\u022e\u0228\3\2\2\2\u022e\u022b\3\2\2\2\u022f\u0239")
        buf.write("\3\2\2\2\u0230\u0231\7$\2\2\u0231\u0232\5D#\2\u0232\u0233")
        buf.write("\b\25\1\2\u0233\u0238\3\2\2\2\u0234\u0235\5\64\33\2\u0235")
        buf.write("\u0236\b\25\1\2\u0236\u0238\3\2\2\2\u0237\u0230\3\2\2")
        buf.write("\2\u0237\u0234\3\2\2\2\u0238\u023b\3\2\2\2\u0239\u0237")
        buf.write("\3\2\2\2\u0239\u023a\3\2\2\2\u023a\u023e\3\2\2\2\u023b")
        buf.write("\u0239\3\2\2\2\u023c\u023d\7A\2\2\u023d\u023f\b\25\1\2")
        buf.write("\u023e\u023c\3\2\2\2\u023e\u023f\3\2\2\2\u023f\u0247\3")
        buf.write("\2\2\2\u0240\u0241\5:\36\2\u0241\u0244\b\25\1\2\u0242")
        buf.write("\u0243\7A\2\2\u0243\u0245\b\25\1\2\u0244\u0242\3\2\2\2")
        buf.write("\u0244\u0245\3\2\2\2\u0245\u0247\3\2\2\2\u0246\u020f\3")
        buf.write("\2\2\2\u0246\u0213\3\2\2\2\u0246\u021b\3\2\2\2\u0246\u022e")
        buf.write("\3\2\2\2\u0246\u0240\3\2\2\2\u0247)\3\2\2\2\u0248\u0249")
        buf.write("\7D\2\2\u0249\u024a\7\4\2\2\u024a\u024b\5,\27\2\u024b")
        buf.write("\u024c\7\5\2\2\u024c\u024d\7\6\2\2\u024d\u024e\5\2\2\2")
        buf.write("\u024e\u024f\7\b\2\2\u024f\u0250\b\26\1\2\u0250\u0264")
        buf.write("\3\2\2\2\u0251\u0252\7E\2\2\u0252\u0253\7\4\2\2\u0253")
        buf.write("\u0254\5,\27\2\u0254\u0255\7\5\2\2\u0255\u0256\7\6\2\2")
        buf.write("\u0256\u0257\5\2\2\2\u0257\u0258\7\b\2\2\u0258\u0259\b")
        buf.write("\26\1\2\u0259\u0264\3\2\2\2\u025a\u025b\7F\2\2\u025b\u025c")
        buf.write("\7\4\2\2\u025c\u025d\5,\27\2\u025d\u025e\7\5\2\2\u025e")
        buf.write("\u025f\7\6\2\2\u025f\u0260\5\2\2\2\u0260\u0261\7\b\2\2")
        buf.write("\u0261\u0262\b\26\1\2\u0262\u0264\3\2\2\2\u0263\u0248")
        buf.write("\3\2\2\2\u0263\u0251\3\2\2\2\u0263\u025a\3\2\2\2\u0264")
        buf.write("+\3\2\2\2\u0265\u0266\5.\30\2\u0266\u026d\b\27\1\2\u0267")
        buf.write("\u0268\7\34\2\2\u0268\u0269\5.\30\2\u0269\u026a\b\27\1")
        buf.write("\2\u026a\u026c\3\2\2\2\u026b\u0267\3\2\2\2\u026c\u026f")
        buf.write("\3\2\2\2\u026d\u026b\3\2\2\2\u026d\u026e\3\2\2\2\u026e")
        buf.write("\u0276\3\2\2\2\u026f\u026d\3\2\2\2\u0270\u0271\7\34\2")
        buf.write("\2\u0271\u0272\5\60\31\2\u0272\u0273\b\27\1\2\u0273\u0275")
        buf.write("\3\2\2\2\u0274\u0270\3\2\2\2\u0275\u0278\3\2\2\2\u0276")
        buf.write("\u0274\3\2\2\2\u0276\u0277\3\2\2\2\u0277\u027d\3\2\2\2")
        buf.write("\u0278\u0276\3\2\2\2\u0279\u027a\7\34\2\2\u027a\u027b")
        buf.write("\5\62\32\2\u027b\u027c\b\27\1\2\u027c\u027e\3\2\2\2\u027d")
        buf.write("\u0279\3\2\2\2\u027d\u027e\3\2\2\2\u027e\u0295\3\2\2\2")
        buf.write("\u027f\u0280\5\60\31\2\u0280\u0287\b\27\1\2\u0281\u0282")
        buf.write("\7\34\2\2\u0282\u0283\5\60\31\2\u0283\u0284\b\27\1\2\u0284")
        buf.write("\u0286\3\2\2\2\u0285\u0281\3\2\2\2\u0286\u0289\3\2\2\2")
        buf.write("\u0287\u0285\3\2\2\2\u0287\u0288\3\2\2\2\u0288\u028e\3")
        buf.write("\2\2\2\u0289\u0287\3\2\2\2\u028a\u028b\7\34\2\2\u028b")
        buf.write("\u028c\5\62\32\2\u028c\u028d\b\27\1\2\u028d\u028f\3\2")
        buf.write("\2\2\u028e\u028a\3\2\2\2\u028e\u028f\3\2\2\2\u028f\u0295")
        buf.write("\3\2\2\2\u0290\u0291\5\62\32\2\u0291\u0292\b\27\1\2\u0292")
        buf.write("\u0295\3\2\2\2\u0293\u0295\3\2\2\2\u0294\u0265\3\2\2\2")
        buf.write("\u0294\u027f\3\2\2\2\u0294\u0290\3\2\2\2\u0294\u0293\3")
        buf.write("\2\2\2\u0295-\3\2\2\2\u0296\u0297\6\30\3\3\u0297\u0298")
        buf.write("\7G\2\2\u0298\u0299\5\f\7\2\u0299\u029a\b\30\1\2\u029a")
        buf.write("\u029f\3\2\2\2\u029b\u029c\5D#\2\u029c\u029d\b\30\1\2")
        buf.write("\u029d\u029f\3\2\2\2\u029e\u0296\3\2\2\2\u029e\u029b\3")
        buf.write("\2\2\2\u029f/\3\2\2\2\u02a0\u02a1\5\f\7\2\u02a1\u02a2")
        buf.write("\7#\2\2\u02a2\u02a3\5\16\b\2\u02a3\u02a4\b\31\1\2\u02a4")
        buf.write("\61\3\2\2\2\u02a5\u02a6\78\2\2\u02a6\u02a7\5D#\2\u02a7")
        buf.write("\u02a8\b\32\1\2\u02a8\63\3\2\2\2\u02a9\u02aa\7\4\2\2\u02aa")
        buf.write("\u02ab\58\35\2\u02ab\u02ac\7\5\2\2\u02ac\u02ad\b\33\1")
        buf.write("\2\u02ad\u02b4\3\2\2\2\u02ae\u02af\7%\2\2\u02af\u02b0")
        buf.write("\5\66\34\2\u02b0\u02b1\7&\2\2\u02b1\u02b2\b\33\1\2\u02b2")
        buf.write("\u02b4\3\2\2\2\u02b3\u02a9\3\2\2\2\u02b3\u02ae\3\2\2\2")
        buf.write("\u02b4\65\3\2\2\2\u02b5\u02c8\5\16\b\2\u02b6\u02bb\7N")
        buf.write("\2\2\u02b7\u02b8\5\16\b\2\u02b8\u02b9\b\34\1\2\u02b9\u02bc")
        buf.write("\3\2\2\2\u02ba\u02bc\b\34\1\2\u02bb\u02b7\3\2\2\2\u02bb")
        buf.write("\u02ba\3\2\2\2\u02bc\u02c9\3\2\2\2\u02bd\u02be\7\34\2")
        buf.write("\2\u02be\u02bf\5\16\b\2\u02bf\u02c0\b\34\1\2\u02c0\u02c2")
        buf.write("\3\2\2\2\u02c1\u02bd\3\2\2\2\u02c2\u02c3\3\2\2\2\u02c3")
        buf.write("\u02c1\3\2\2\2\u02c3\u02c4\3\2\2\2\u02c4\u02c5\3\2\2\2")
        buf.write("\u02c5\u02c6\b\34\1\2\u02c6\u02c9\3\2\2\2\u02c7\u02c9")
        buf.write("\b\34\1\2\u02c8\u02b6\3\2\2\2\u02c8\u02c1\3\2\2\2\u02c8")
        buf.write("\u02c7\3\2\2\2\u02c9\u02cf\3\2\2\2\u02ca\u02cb\7N\2\2")
        buf.write("\u02cb\u02cc\5\16\b\2\u02cc\u02cd\b\34\1\2\u02cd\u02cf")
        buf.write("\3\2\2\2\u02ce\u02b5\3\2\2\2\u02ce\u02ca\3\2\2\2\u02cf")
        buf.write("\67\3\2\2\2\u02d0\u02d1\5\20\t\2\u02d1\u02d7\b\35\1\2")
        buf.write("\u02d2\u02d3\7\34\2\2\u02d3\u02d4\78\2\2\u02d4\u02d5\5")
        buf.write("\22\n\2\u02d5\u02d6\b\35\1\2\u02d6\u02d8\3\2\2\2\u02d7")
        buf.write("\u02d2\3\2\2\2\u02d7\u02d8\3\2\2\2\u02d8\u02df\3\2\2\2")
        buf.write("\u02d9\u02da\78\2\2\u02da\u02db\5\22\n\2\u02db\u02dc\b")
        buf.write("\35\1\2\u02dc\u02df\3\2\2\2\u02dd\u02df\3\2\2\2\u02de")
        buf.write("\u02d0\3\2\2\2\u02de\u02d9\3\2\2\2\u02de\u02dd\3\2\2\2")
        buf.write("\u02df9\3\2\2\2\u02e0\u02e4\7%\2\2\u02e1\u02e2\5<\37\2")
        buf.write("\u02e2\u02e3\b\36\1\2\u02e3\u02e5\3\2\2\2\u02e4\u02e1")
        buf.write("\3\2\2\2\u02e4\u02e5\3\2\2\2\u02e5\u02e6\3\2\2\2\u02e6")
        buf.write("\u02e7\7&\2\2\u02e7\u02fb\b\36\1\2\u02e8\u02ec\7\6\2\2")
        buf.write("\u02e9\u02ea\5<\37\2\u02ea\u02eb\b\36\1\2\u02eb\u02ed")
        buf.write("\3\2\2\2\u02ec\u02e9\3\2\2\2\u02ec\u02ed\3\2\2\2\u02ed")
        buf.write("\u02ee\3\2\2\2\u02ee\u02ef\7\b\2\2\u02ef\u02fb\b\36\1")
        buf.write("\2\u02f0\u02f1\7O\2\2\u02f1\u02fb\b\36\1\2\u02f2\u02f3")
        buf.write("\7P\2\2\u02f3\u02fb\b\36\1\2\u02f4\u02f5\5B\"\2\u02f5")
        buf.write("\u02f6\b\36\1\2\u02f6\u02fb\3\2\2\2\u02f7\u02f8\6\36\4")
        buf.write("\3\u02f8\u02f9\7\'\2\2\u02f9\u02fb\b\36\1\2\u02fa\u02e0")
        buf.write("\3\2\2\2\u02fa\u02e8\3\2\2\2\u02fa\u02f0\3\2\2\2\u02fa")
        buf.write("\u02f2\3\2\2\2\u02fa\u02f4\3\2\2\2\u02fa\u02f7\3\2\2\2")
        buf.write("\u02fb;\3\2\2\2\u02fc\u032b\5\16\b\2\u02fd\u02fe\7\34")
        buf.write("\2\2\u02fe\u0314\5\16\b\2\u02ff\u0300\7N\2\2\u0300\u0301")
        buf.write("\5\16\b\2\u0301\u0302\b\37\1\2\u0302\u0315\3\2\2\2\u0303")
        buf.write("\u030a\b\37\1\2\u0304\u0305\7\34\2\2\u0305\u0306\5\16")
        buf.write("\b\2\u0306\u0307\b\37\1\2\u0307\u0309\3\2\2\2\u0308\u0304")
        buf.write("\3\2\2\2\u0309\u030c\3\2\2\2\u030a\u0308\3\2\2\2\u030a")
        buf.write("\u030b\3\2\2\2\u030b\u0312\3\2\2\2\u030c\u030a\3\2\2\2")
        buf.write("\u030d\u030e\7\20\2\2\u030e\u030f\5\16\b\2\u030f\u0310")
        buf.write("\b\37\1\2\u0310\u0313\3\2\2\2\u0311\u0313\b\37\1\2\u0312")
        buf.write("\u030d\3\2\2\2\u0312\u0311\3\2\2\2\u0313\u0315\3\2\2\2")
        buf.write("\u0314\u02ff\3\2\2\2\u0314\u0303\3\2\2\2\u0315\u032c\3")
        buf.write("\2\2\2\u0316\u0317\7N\2\2\u0317\u0318\5\16\b\2\u0318\u0319")
        buf.write("\b\37\1\2\u0319\u032c\3\2\2\2\u031a\u0320\b\37\1\2\u031b")
        buf.write("\u031c\7\20\2\2\u031c\u031d\5\16\b\2\u031d\u031e\b\37")
        buf.write("\1\2\u031e\u0321\3\2\2\2\u031f\u0321\b\37\1\2\u0320\u031b")
        buf.write("\3\2\2\2\u0320\u031f\3\2\2\2\u0321\u032c\3\2\2\2\u0322")
        buf.write("\u0323\7\r\2\2\u0323\u0329\5> \2\u0324\u0325\7\20\2\2")
        buf.write("\u0325\u0326\5F$\2\u0326\u0327\b\37\1\2\u0327\u032a\3")
        buf.write("\2\2\2\u0328\u032a\b\37\1\2\u0329\u0324\3\2\2\2\u0329")
        buf.write("\u0328\3\2\2\2\u032a\u032c\3\2\2\2\u032b\u02fd\3\2\2\2")
        buf.write("\u032b\u0316\3\2\2\2\u032b\u031a\3\2\2\2\u032b\u0322\3")
        buf.write("\2\2\2\u032c=\3\2\2\2\u032d\u032e\5@!\2\u032e\u0335\b")
        buf.write(" \1\2\u032f\u0330\7\34\2\2\u0330\u0331\5@!\2\u0331\u0332")
        buf.write("\b \1\2\u0332\u0334\3\2\2\2\u0333\u032f\3\2\2\2\u0334")
        buf.write("\u0337\3\2\2\2\u0335\u0333\3\2\2\2\u0335\u0336\3\2\2\2")
        buf.write("\u0336?\3\2\2\2\u0337\u0335\3\2\2\2\u0338\u0339\5\n\6")
        buf.write("\2\u0339\u033a\7\64\2\2\u033a\u033b\5\16\b\2\u033b\u033c")
        buf.write("\b!\1\2\u033cA\3\2\2\2\u033d\u033e\7L\2\2\u033e\u0348")
        buf.write("\b\"\1\2\u033f\u0340\7M\2\2\u0340\u0348\b\"\1\2\u0341")
        buf.write("\u0342\7H\2\2\u0342\u0348\b\"\1\2\u0343\u0344\7I\2\2\u0344")
        buf.write("\u0348\b\"\1\2\u0345\u0346\7J\2\2\u0346\u0348\b\"\1\2")
        buf.write("\u0347\u033d\3\2\2\2\u0347\u033f\3\2\2\2\u0347\u0341\3")
        buf.write("\2\2\2\u0347\u0343\3\2\2\2\u0347\u0345\3\2\2\2\u0348C")
        buf.write("\3\2\2\2\u0349\u034a\7K\2\2\u034a\u034b\b#\1\2\u034bE")
        buf.write("\3\2\2\2\u034c\u034d\5\16\b\2\u034d\u034e\b$\1\2\u034e")
        buf.write("G\3\2\2\2\u034f\u0350\5\n\6\2\u0350\u0357\b%\1\2\u0351")
        buf.write("\u0352\7\34\2\2\u0352\u0353\5\n\6\2\u0353\u0354\b%\1\2")
        buf.write("\u0354\u0356\3\2\2\2\u0355\u0351\3\2\2\2\u0356\u0359\3")
        buf.write("\2\2\2\u0357\u0355\3\2\2\2\u0357\u0358\3\2\2\2\u0358I")
        buf.write("\3\2\2\2\u0359\u0357\3\2\2\2EOay\u0082\u0090\u0096\u00a1")
        buf.write("\u00ca\u00de\u00f7\u0112\u0121\u0123\u0130\u0132\u013d")
        buf.write("\u014d\u015d\u015f\u0172\u0175\u0178\u0180\u018a\u0195")
        buf.write("\u01ba\u01c6\u01c8\u01e1\u01e3\u01f0\u01f2\u01fb\u020d")
        buf.write("\u022e\u0237\u0239\u023e\u0244\u0246\u0263\u026d\u0276")
        buf.write("\u027d\u0287\u028e\u0294\u029e\u02b3\u02bb\u02c3\u02c8")
        buf.write("\u02ce\u02d7\u02de\u02e4\u02ec\u02fa\u030a\u0312\u0314")
        buf.write("\u0320\u0329\u032b\u0335\u0347\u0357")
        return buf.getvalue()


class SetlXgrammarParser ( Parser ):

    grammarFileName = "SetlXgrammar.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'class'", "'('", "')'", "'{'", "'static'", 
                     "'}'", "'if'", "'else'", "'switch'", "'case'", "':'", 
                     "'default'", "'for'", "'|'", "'while'", "'do'", "';'", 
                     "'try'", "'catch'", "'backtrack'", "'break'", "'continue'", 
                     "'exit'", "'return'", "'assert'", "','", "'+='", "'-='", 
                     "'*='", "'/='", "'\\='", "'%='", "':='", "'.'", "'['", 
                     "']'", "'_'", "'<==>'", "'<!=>'", "'|=>'", "'=>'", 
                     "'||'", "'&&'", "'=='", "'!='", "'<'", "'<='", "'>'", 
                     "'>='", "'in'", "'notin'", "'+'", "'-'", "'*'", "'/'", 
                     "'\\'", "'%'", "'><'", "'+/'", "'*/'", "'**'", "'#'", 
                     "'!'", "'forall'", "'exists'", "'procedure'", "'cachedProcedure'", 
                     "'closure'", "'rw'", "'om'", "'true'", "'false'", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "'..'" ]

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
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "ID", "NUMBER", "DOUBLE", "RANGE_SIGN", 
                      "STRING", "LITERAL", "LINE_COMMENT", "MULTI_COMMENT", 
                      "WS", "REMAINDER" ]

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
    RULE_procedureListParameter = 24
    RULE_call = 25
    RULE_collectionAccessParams = 26
    RULE_callParameters = 27
    RULE_value = 28
    RULE_collectionBuilder = 29
    RULE_iteratorChain = 30
    RULE_iterator = 31
    RULE_atomicValue = 32
    RULE_variable = 33
    RULE_condition = 34
    RULE_assignmentList = 35

    ruleNames =  [ "block", "statement", "assignmentOther", "assignmentDirect", 
                   "assignable", "assignableVariable", "expr", "exprList", 
                   "exprContent", "lambdaProcedure", "lambdaParameters", 
                   "implication", "disjunction", "conjunction", "comparison", 
                   "setlxSum", "product", "setlxReduce", "prefixOperation", 
                   "factor", "procedure", "procedureParameters", "procedureParameter", 
                   "procedureDefaultParameter", "procedureListParameter", 
                   "call", "collectionAccessParams", "callParameters", "value", 
                   "collectionBuilder", "iteratorChain", "iterator", "atomicValue", 
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
    T__70=71
    T__71=72
    ID=73
    NUMBER=74
    DOUBLE=75
    RANGE_SIGN=76
    STRING=77
    LITERAL=78
    LINE_COMMENT=79
    MULTI_COMMENT=80
    WS=81
    REMAINDER=82

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
            self.state = 77
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,0,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 72
                    localctx._statement = self.statement()
                    stmnts.append(localctx._statement.stmnt) 
                self.state = 79
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
            self._ID = None # Token
            self._procedureParameters = None # ProcedureParametersContext
            self.b1 = None # BlockContext
            self.b2 = None # BlockContext
            self.c1 = None # ConditionContext
            self.c2 = None # ConditionContext
            self.b3 = None # BlockContext
            self._iteratorChain = None # IteratorChainContext
            self._condition = None # ConditionContext
            self._block = None # BlockContext
            self.v2 = None # AssignableVariableContext
            self._expr = None # ExprContext
            self._assignmentOther = None # AssignmentOtherContext
            self._assignmentDirect = None # AssignmentDirectContext

        def ID(self):
            return self.getToken(SetlXgrammarParser.ID, 0)

        def procedureParameters(self):
            return self.getTypedRuleContext(SetlXgrammarParser.ProcedureParametersContext,0)


        def block(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SetlXgrammarParser.BlockContext)
            else:
                return self.getTypedRuleContext(SetlXgrammarParser.BlockContext,i)


        def condition(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SetlXgrammarParser.ConditionContext)
            else:
                return self.getTypedRuleContext(SetlXgrammarParser.ConditionContext,i)


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
        static = None
            
        self._la = 0 # Token type
        try:
            self.state = 245
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,9,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 82
                self.match(SetlXgrammarParser.T__0)
                self.state = 83
                localctx._ID = self.match(SetlXgrammarParser.ID)
                self.state = 84
                self.match(SetlXgrammarParser.T__1)
                self.state = 85
                localctx._procedureParameters = self.procedureParameters(True)
                self.state = 86
                self.match(SetlXgrammarParser.T__2)
                self.state = 87
                self.match(SetlXgrammarParser.T__3)
                self.state = 88
                localctx.b1 = self.block()
                self.state = 95
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==SetlXgrammarParser.T__4:
                    self.state = 89
                    self.match(SetlXgrammarParser.T__4)
                    self.state = 90
                    self.match(SetlXgrammarParser.T__3)
                    self.state = 91
                    localctx.b2 = self.block()
                    self.state = 92
                    self.match(SetlXgrammarParser.T__5)
                    static = localctx.b2.blk


                self.state = 97
                self.match(SetlXgrammarParser.T__5)
                localctx.stmnt = ClassConstructor((None if localctx._ID is None else localctx._ID.text), localctx._procedureParameters.paramList, localctx.b1.blk, static)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 100
                self.match(SetlXgrammarParser.T__6)
                self.state = 101
                self.match(SetlXgrammarParser.T__1)
                self.state = 102
                localctx.c1 = self.condition()
                self.state = 103
                self.match(SetlXgrammarParser.T__2)
                self.state = 104
                self.match(SetlXgrammarParser.T__3)
                self.state = 105
                localctx.b1 = self.block()
                self.state = 106
                self.match(SetlXgrammarParser.T__5)
                self.state = 119
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,2,self._ctx)
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1:
                        self.state = 107
                        self.match(SetlXgrammarParser.T__7)
                        self.state = 108
                        self.match(SetlXgrammarParser.T__6)
                        self.state = 109
                        self.match(SetlXgrammarParser.T__1)
                        self.state = 110
                        localctx.c2 = self.condition()
                        self.state = 111
                        self.match(SetlXgrammarParser.T__2)
                        self.state = 112
                        self.match(SetlXgrammarParser.T__3)
                        self.state = 113
                        localctx.b2 = self.block()
                        self.state = 114
                        self.match(SetlXgrammarParser.T__5)
                        else_list.append(IfThenBranch(localctx.c2.cnd,localctx.b2.blk)) 
                        			 
                    self.state = 121
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,2,self._ctx)

                self.state = 128
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
                if la_ == 1:
                    self.state = 122
                    self.match(SetlXgrammarParser.T__7)
                    self.state = 123
                    self.match(SetlXgrammarParser.T__3)
                    self.state = 124
                    localctx.b3 = self.block()
                    self.state = 125
                    self.match(SetlXgrammarParser.T__5)
                    else_list.append(localctx.b3.blk) 


                localctx.stmnt = IfThen(localctx.c1.cnd,localctx.b1.blk,else_list) 
                		
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 132
                self.match(SetlXgrammarParser.T__8)
                self.state = 133
                self.match(SetlXgrammarParser.T__3)
                self.state = 142
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==SetlXgrammarParser.T__9:
                    self.state = 134
                    self.match(SetlXgrammarParser.T__9)
                    self.state = 135
                    localctx.c1 = self.condition()
                    self.state = 136
                    self.match(SetlXgrammarParser.T__10)
                    self.state = 137
                    localctx.b1 = self.block()
                    caseList.append((localctx.c1.cnd, localctx.b1.blk)) 
                    self.state = 144
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 148
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==SetlXgrammarParser.T__11:
                    self.state = 145
                    self.match(SetlXgrammarParser.T__11)
                    self.state = 146
                    self.match(SetlXgrammarParser.T__10)
                    self.state = 147
                    localctx.b2 = self.block()


                self.state = 150
                self.match(SetlXgrammarParser.T__5)
                localctx.stmnt = Switch(caseList,localctx.b2.blk) 
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 152
                self.match(SetlXgrammarParser.T__12)
                self.state = 153
                self.match(SetlXgrammarParser.T__1)
                self.state = 154
                localctx._iteratorChain = self.iteratorChain(False)
                self.state = 159
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==SetlXgrammarParser.T__13:
                    self.state = 155
                    self.match(SetlXgrammarParser.T__13)
                    self.state = 156
                    localctx._condition = self.condition()
                    condition = localctx._condition.cnd


                self.state = 161
                self.match(SetlXgrammarParser.T__2)
                self.state = 162
                self.match(SetlXgrammarParser.T__3)
                self.state = 163
                localctx._block = self.block()
                self.state = 164
                self.match(SetlXgrammarParser.T__5)
                localctx.stmnt = For(localctx._iteratorChain.ic, condition, localctx._block.blk) 
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 167
                self.match(SetlXgrammarParser.T__14)
                self.state = 168
                self.match(SetlXgrammarParser.T__1)
                self.state = 169
                localctx._condition = self.condition()
                self.state = 170
                self.match(SetlXgrammarParser.T__2)
                self.state = 171
                self.match(SetlXgrammarParser.T__3)
                self.state = 172
                localctx._block = self.block()
                self.state = 173
                self.match(SetlXgrammarParser.T__5)
                localctx.stmnt = While(localctx._condition.cnd, localctx._block.blk) 
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 176
                self.match(SetlXgrammarParser.T__15)
                self.state = 177
                self.match(SetlXgrammarParser.T__3)
                self.state = 178
                localctx._block = self.block()
                self.state = 179
                self.match(SetlXgrammarParser.T__5)
                self.state = 180
                self.match(SetlXgrammarParser.T__14)
                self.state = 181
                self.match(SetlXgrammarParser.T__1)
                self.state = 182
                localctx._condition = self.condition()
                self.state = 183
                self.match(SetlXgrammarParser.T__2)
                self.state = 184
                self.match(SetlXgrammarParser.T__16)
                localctx.stmnt = DoWhile(localctx._condition.cnd, localctx._block.blk) 
                		
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 187
                self.match(SetlXgrammarParser.T__17)
                self.state = 188
                self.match(SetlXgrammarParser.T__3)
                self.state = 189
                localctx.b1 = self.block()
                self.state = 190
                self.match(SetlXgrammarParser.T__5)
                self.state = 200
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,7,self._ctx)
                if la_ == 1:
                    self.state = 191
                    self.match(SetlXgrammarParser.T__18)
                    self.state = 192
                    self.match(SetlXgrammarParser.T__1)
                    self.state = 193
                    localctx.v2 = self.assignableVariable()
                    self.state = 194
                    self.match(SetlXgrammarParser.T__2)
                    self.state = 195
                    self.match(SetlXgrammarParser.T__3)
                    self.state = 196
                    localctx.b3 = self.block()
                    self.state = 197
                    self.match(SetlXgrammarParser.T__5)
                    tryList.append(TryCatchBranch(localctx.v2.v, localctx.b3.blk))         
                    			


                localctx.stmnt = TryCatch(localctx.b1.blk, tryList) 
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 204
                self.match(SetlXgrammarParser.T__19)
                self.state = 205
                self.match(SetlXgrammarParser.T__16)
                localctx.stmnt = Backtrack() 
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 207
                self.match(SetlXgrammarParser.T__20)
                self.state = 208
                self.match(SetlXgrammarParser.T__16)
                localctx.stmnt = Break() 
                pass

            elif la_ == 10:
                self.enterOuterAlt(localctx, 10)
                self.state = 210
                self.match(SetlXgrammarParser.T__21)
                self.state = 211
                self.match(SetlXgrammarParser.T__16)
                localctx.stmnt = Continue() 
                pass

            elif la_ == 11:
                self.enterOuterAlt(localctx, 11)
                self.state = 213
                self.match(SetlXgrammarParser.T__22)
                self.state = 214
                self.match(SetlXgrammarParser.T__16)
                localctx.stmnt = Exit() 
                pass

            elif la_ == 12:
                self.enterOuterAlt(localctx, 12)
                self.state = 216
                self.match(SetlXgrammarParser.T__23)
                self.state = 220
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,8,self._ctx)
                if la_ == 1:
                    self.state = 217
                    localctx._expr = self.expr(False)
                    expression = localctx._expr.ex 


                self.state = 222
                self.match(SetlXgrammarParser.T__16)
                localctx.stmnt = Return(expression) 
                pass

            elif la_ == 13:
                self.enterOuterAlt(localctx, 13)
                self.state = 224
                self.match(SetlXgrammarParser.T__24)
                self.state = 225
                self.match(SetlXgrammarParser.T__1)
                self.state = 226
                localctx._condition = self.condition()
                self.state = 227
                self.match(SetlXgrammarParser.T__25)
                self.state = 228
                localctx._expr = self.expr(False)
                self.state = 229
                self.match(SetlXgrammarParser.T__2)
                self.state = 230
                self.match(SetlXgrammarParser.T__16)
                localctx.stmnt = Assert(localctx._condition.cnd, localctx._expr.ex)
                pass

            elif la_ == 14:
                self.enterOuterAlt(localctx, 14)
                self.state = 233
                localctx._assignmentOther = self.assignmentOther()
                self.state = 234
                self.match(SetlXgrammarParser.T__16)
                localctx.stmnt = localctx._assignmentOther.assign 
                pass

            elif la_ == 15:
                self.enterOuterAlt(localctx, 15)
                self.state = 237
                localctx._assignmentDirect = self.assignmentDirect()
                self.state = 238
                self.match(SetlXgrammarParser.T__16)
                localctx.stmnt = localctx._assignmentDirect.assign 
                pass

            elif la_ == 16:
                self.enterOuterAlt(localctx, 16)
                self.state = 241
                localctx._expr = self.expr(False)
                self.state = 242
                self.match(SetlXgrammarParser.T__16)
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
            self.state = 247
            localctx._assignable = self.assignable(False)
            self.state = 272
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [SetlXgrammarParser.T__26]:
                self.state = 248
                self.match(SetlXgrammarParser.T__26)
                self.state = 249
                localctx.e = self.expr(False)
                localctx.assign = SumAssignment(localctx._assignable.a, localctx.e.ex) 
                pass
            elif token in [SetlXgrammarParser.T__27]:
                self.state = 252
                self.match(SetlXgrammarParser.T__27)
                self.state = 253
                localctx.e = self.expr(False)
                localctx.assign = DifferenceAssignment(localctx._assignable.a, localctx.e.ex) 
                pass
            elif token in [SetlXgrammarParser.T__28]:
                self.state = 256
                self.match(SetlXgrammarParser.T__28)
                self.state = 257
                localctx.e = self.expr(False)
                localctx.assign = ProductAssignment(localctx._assignable.a, localctx.e.ex) 
                pass
            elif token in [SetlXgrammarParser.T__29]:
                self.state = 260
                self.match(SetlXgrammarParser.T__29)
                self.state = 261
                localctx.e = self.expr(False)
                localctx.assign = QuotientAssignment(localctx._assignable.a, localctx.e.ex) 
                pass
            elif token in [SetlXgrammarParser.T__30]:
                self.state = 264
                self.match(SetlXgrammarParser.T__30)
                self.state = 265
                localctx.e = self.expr(False)
                localctx.assign = IntegerDivisionAssignment(localctx._assignable.a, localctx.e.ex) 
                pass
            elif token in [SetlXgrammarParser.T__31]:
                self.state = 268
                self.match(SetlXgrammarParser.T__31)
                self.state = 269
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
            self.state = 289
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,12,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 274
                localctx._variable = self.variable()
                self.state = 275
                self.match(SetlXgrammarParser.T__32)
                self.state = 276
                localctx._procedure = self.procedure()

                localctx._procedure.pd.name = localctx._variable.v.id
                localctx.assign = localctx._procedure.pd
                    
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 279
                localctx._assignable = self.assignable(False)
                self.state = 280
                self.match(SetlXgrammarParser.T__32)
                self.state = 287
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,11,self._ctx)
                if la_ == 1:
                    self.state = 281
                    localctx._assignmentDirect = self.assignmentDirect()
                    localctx.assign = Assignment(localctx._assignable.a, localctx._assignmentDirect.assign) 
                    pass

                elif la_ == 2:
                    self.state = 284
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
            self.state = 315
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,15,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 291
                localctx._assignableVariable = self.assignableVariable()
                localctx.a = localctx._assignableVariable.v
                self.state = 304
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==SetlXgrammarParser.T__33 or _la==SetlXgrammarParser.T__34:
                    self.state = 302
                    self._errHandler.sync(self)
                    token = self._input.LA(1)
                    if token in [SetlXgrammarParser.T__33]:
                        self.state = 293
                        self.match(SetlXgrammarParser.T__33)
                        self.state = 294
                        localctx._variable = self.variable()
                        localctx.a = AssignableMember(localctx.a, localctx._variable.v)
                        pass
                    elif token in [SetlXgrammarParser.T__34]:
                        self.state = 297
                        self.match(SetlXgrammarParser.T__34)
                        self.state = 298
                        localctx._exprList = self.exprList(False)
                        self.state = 299
                        self.match(SetlXgrammarParser.T__35)
                        localctx.a = AssignableCollectionAccess(localctx.a, localctx._exprList.exprs)
                        pass
                    else:
                        raise NoViableAltException(self)

                    self.state = 306
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 307
                self.match(SetlXgrammarParser.T__34)
                self.state = 308
                localctx._assignmentList = self.assignmentList()
                self.state = 309
                self.match(SetlXgrammarParser.T__35)
                localctx.a = AssignableList(localctx._assignmentList.al)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 312
                if not localctx.enableIgnore:
                    from antlr4.error.Errors import FailedPredicateException
                    raise FailedPredicateException(self, "$enableIgnore")
                self.state = 313
                self.match(SetlXgrammarParser.T__36)
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
            self.state = 317
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
            self.state = 320
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
            
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 323
            localctx._exprContent = self.exprContent(localctx.enableIgnore)
            localctx.exprs.append(localctx._exprContent.ex)
            self.state = 331
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,16,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 325
                    self.match(SetlXgrammarParser.T__25)
                    self.state = 326
                    localctx._exprContent = self.exprContent(localctx.enableIgnore)
                    localctx.exprs.append(localctx._exprContent.ex) 
                self.state = 333
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,16,self._ctx)

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
            self.state = 349
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,18,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 334
                localctx._lambdaProcedure = self.lambdaProcedure()
                localctx.ex = localctx._lambdaProcedure.lp 
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 337
                localctx._implication = self.implication(localctx.enableIgnore)
                localctx.ex = localctx._implication.i
                self.state = 347
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [SetlXgrammarParser.T__37]:
                    self.state = 339
                    self.match(SetlXgrammarParser.T__37)
                    self.state = 340
                    localctx._implication = self.implication(localctx.enableIgnore)
                    localctx.ex = BooleanEqual(localctx.ex,localctx._implication.i) 
                    pass
                elif token in [SetlXgrammarParser.T__38]:
                    self.state = 343
                    self.match(SetlXgrammarParser.T__38)
                    self.state = 344
                    localctx._implication = self.implication(localctx.enableIgnore)
                    localctx.ex = BooleanNotEqual(localctx.ex,localctx._implication.i) 
                    pass
                elif token in [SetlXgrammarParser.T__2, SetlXgrammarParser.T__5, SetlXgrammarParser.T__10, SetlXgrammarParser.T__13, SetlXgrammarParser.T__16, SetlXgrammarParser.T__25, SetlXgrammarParser.T__35, SetlXgrammarParser.RANGE_SIGN]:
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
            self.state = 351
            localctx._lambdaParameters = self.lambdaParameters()

            self.state = 352
            self.match(SetlXgrammarParser.T__39)
            self.state = 353
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
            self.state = 374
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [SetlXgrammarParser.ID]:
                self.enterOuterAlt(localctx, 1)
                self.state = 356
                localctx._variable = self.variable()
                localctx.paramList.append(Parameter(localctx._variable.v.id)) 
                pass
            elif token in [SetlXgrammarParser.T__34]:
                self.enterOuterAlt(localctx, 2)
                self.state = 359
                self.match(SetlXgrammarParser.T__34)
                self.state = 371
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==SetlXgrammarParser.ID:
                    self.state = 360
                    localctx.v1 = self.variable()
                    localctx.paramList.append(Parameter(localctx.v1.v.id))
                    self.state = 368
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    while _la==SetlXgrammarParser.T__25:
                        self.state = 362
                        self.match(SetlXgrammarParser.T__25)
                        self.state = 363
                        localctx.v2 = self.variable()
                        localctx.paramList.append(Parameter(localctx.v2.v.id))
                        self.state = 370
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)



                self.state = 373
                self.match(SetlXgrammarParser.T__35)
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
            self.state = 376
            localctx._disjunction = self.disjunction(localctx.enableIgnore)
            localctx.i = localctx._disjunction.d
            self.state = 382
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==SetlXgrammarParser.T__40:
                self.state = 378
                self.match(SetlXgrammarParser.T__40)
                self.state = 379
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
            self.state = 384
            localctx._conjunction = self.conjunction(localctx.enableIgnore)
            localctx.d = localctx._conjunction.c
            self.state = 392
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==SetlXgrammarParser.T__41:
                self.state = 386
                self.match(SetlXgrammarParser.T__41)
                self.state = 387
                localctx._conjunction = self.conjunction(localctx.enableIgnore)
                localctx.d = Disjunction(localctx.d, localctx._conjunction.c) 
                self.state = 394
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
            self.state = 395
            localctx._comparison = self.comparison(localctx.enableIgnore)
            localctx.c = localctx._comparison.c
            self.state = 403
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==SetlXgrammarParser.T__42:
                self.state = 397
                self.match(SetlXgrammarParser.T__42)
                self.state = 398
                localctx._comparison = self.comparison(localctx.enableIgnore)
                localctx.c = Conjunction(localctx.c, localctx._comparison.c) 
                self.state = 405
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
            self.state = 406
            localctx.s1 = self.setlxSum(localctx.enableIgnore)
            localctx.c = localctx.s1.s 
            self.state = 440
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [SetlXgrammarParser.T__43]:
                self.state = 408
                self.match(SetlXgrammarParser.T__43)
                self.state = 409
                localctx.s2 = self.setlxSum(localctx.enableIgnore)
                localctx.c = Equal(localctx.s1.s,localctx.s2.s) 
                pass
            elif token in [SetlXgrammarParser.T__44]:
                self.state = 412
                self.match(SetlXgrammarParser.T__44)
                self.state = 413
                localctx.s2 = self.setlxSum(localctx.enableIgnore)
                localctx.c = NotEqual(localctx.s1.s,localctx.s2.s) 
                pass
            elif token in [SetlXgrammarParser.T__45]:
                self.state = 416
                self.match(SetlXgrammarParser.T__45)
                self.state = 417
                localctx.s2 = self.setlxSum(localctx.enableIgnore)
                localctx.c = LessThan(localctx.s1.s,localctx.s2.s) 
                pass
            elif token in [SetlXgrammarParser.T__46]:
                self.state = 420
                self.match(SetlXgrammarParser.T__46)
                self.state = 421
                localctx.s2 = self.setlxSum(localctx.enableIgnore)
                localctx.c = LessOrEqual(localctx.s1.s,localctx.s2.s) 
                pass
            elif token in [SetlXgrammarParser.T__47]:
                self.state = 424
                self.match(SetlXgrammarParser.T__47)
                self.state = 425
                localctx.s2 = self.setlxSum(localctx.enableIgnore)
                localctx.c = GreaterThan(localctx.s1.s,localctx.s2.s) 
                pass
            elif token in [SetlXgrammarParser.T__48]:
                self.state = 428
                self.match(SetlXgrammarParser.T__48)
                self.state = 429
                localctx.s2 = self.setlxSum(localctx.enableIgnore)
                localctx.c = GreaterOrEqual(localctx.s1.s,localctx.s2.s) 
                pass
            elif token in [SetlXgrammarParser.T__49]:
                self.state = 432
                self.match(SetlXgrammarParser.T__49)
                self.state = 433
                localctx.s2 = self.setlxSum(localctx.enableIgnore)
                localctx.c = In(localctx.s1.s,localctx.s2.s) 
                pass
            elif token in [SetlXgrammarParser.T__50]:
                self.state = 436
                self.match(SetlXgrammarParser.T__50)
                self.state = 437
                localctx.s2 = self.setlxSum(localctx.enableIgnore)
                localctx.c = NotIn(localctx.s1.s,localctx.s2.s) 
                pass
            elif token in [SetlXgrammarParser.T__2, SetlXgrammarParser.T__5, SetlXgrammarParser.T__10, SetlXgrammarParser.T__13, SetlXgrammarParser.T__16, SetlXgrammarParser.T__25, SetlXgrammarParser.T__35, SetlXgrammarParser.T__37, SetlXgrammarParser.T__38, SetlXgrammarParser.T__40, SetlXgrammarParser.T__41, SetlXgrammarParser.T__42, SetlXgrammarParser.RANGE_SIGN]:
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
            self.state = 442
            localctx.p1 = self.product(localctx.enableIgnore)
            localctx.s = localctx.p1.p
            self.state = 454
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==SetlXgrammarParser.T__51 or _la==SetlXgrammarParser.T__52:
                self.state = 452
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [SetlXgrammarParser.T__51]:
                    self.state = 444
                    self.match(SetlXgrammarParser.T__51)
                    self.state = 445
                    localctx.p2 = self.product(localctx.enableIgnore)
                    localctx.s = Sum(localctx.p1.p,localctx.p2.p) 
                    pass
                elif token in [SetlXgrammarParser.T__52]:
                    self.state = 448
                    self.match(SetlXgrammarParser.T__52)
                    self.state = 449
                    localctx.p2 = self.product(localctx.enableIgnore)
                    localctx.s = Difference(localctx.p1.p,localctx.p2.p) 
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 456
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
            self.state = 457
            localctx.r1 = self.setlxReduce(localctx.enableIgnore)
            localctx.p = localctx.r1.r
            self.state = 481
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << SetlXgrammarParser.T__53) | (1 << SetlXgrammarParser.T__54) | (1 << SetlXgrammarParser.T__55) | (1 << SetlXgrammarParser.T__56) | (1 << SetlXgrammarParser.T__57))) != 0):
                self.state = 479
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [SetlXgrammarParser.T__53]:
                    self.state = 459
                    self.match(SetlXgrammarParser.T__53)
                    self.state = 460
                    localctx.r2 = self.setlxReduce(localctx.enableIgnore)
                    localctx.p = Product(localctx.p,localctx.r2.r) 
                    pass
                elif token in [SetlXgrammarParser.T__54]:
                    self.state = 463
                    self.match(SetlXgrammarParser.T__54)
                    self.state = 464
                    localctx.r2 = self.setlxReduce(localctx.enableIgnore)
                    localctx.p = Quotient(localctx.p,localctx.r2.r) 
                    pass
                elif token in [SetlXgrammarParser.T__55]:
                    self.state = 467
                    self.match(SetlXgrammarParser.T__55)
                    self.state = 468
                    localctx.r2 = self.setlxReduce(localctx.enableIgnore)
                    localctx.p = IntegerDivision(localctx.p,localctx.r2.r) 
                    pass
                elif token in [SetlXgrammarParser.T__56]:
                    self.state = 471
                    self.match(SetlXgrammarParser.T__56)
                    self.state = 472
                    localctx.r2 = self.setlxReduce(localctx.enableIgnore)
                    localctx.p = Modulo(localctx.p,localctx.r2.r) 
                    pass
                elif token in [SetlXgrammarParser.T__57]:
                    self.state = 475
                    self.match(SetlXgrammarParser.T__57)
                    self.state = 476
                    localctx.r2 = self.setlxReduce(localctx.enableIgnore)
                    localctx.p = CartesianProduct(localctx.p,localctx.r2.r) 
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 483
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
            self.state = 484
            localctx.p1 = self.prefixOperation(localctx.enableIgnore)
            localctx.r = localctx.p1.p
            self.state = 496
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==SetlXgrammarParser.T__58 or _la==SetlXgrammarParser.T__59:
                self.state = 494
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [SetlXgrammarParser.T__58]:
                    self.state = 486
                    self.match(SetlXgrammarParser.T__58)
                    self.state = 487
                    localctx.p2 = self.prefixOperation(localctx.enableIgnore)
                    localctx.r = SumOfMembersBinary(localctx.r,localctx.p2.p) 
                    pass
                elif token in [SetlXgrammarParser.T__59]:
                    self.state = 490
                    self.match(SetlXgrammarParser.T__59)
                    self.state = 491
                    localctx.p2 = self.prefixOperation(localctx.enableIgnore)
                    localctx.r = ProductOfMembersBinary(localctx.r,localctx.p2.p) 
                    pass
                else:
                    raise NoViableAltException(self)

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
            self.state = 523
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,33,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 499
                localctx._factor = self.factor(localctx.enableIgnore)
                localctx.p = localctx._factor.f
                self.state = 505
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==SetlXgrammarParser.T__60:
                    self.state = 501
                    self.match(SetlXgrammarParser.T__60)
                    self.state = 502
                    localctx._prefixOperation = self.prefixOperation(localctx.enableIgnore)
                    localctx.p = Power(localctx.p,localctx._prefixOperation.p) 


                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 507
                self.match(SetlXgrammarParser.T__58)
                self.state = 508
                localctx._prefixOperation = self.prefixOperation(localctx.enableIgnore)
                localctx.p = SumOfMembers(localctx._prefixOperation.p) 
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 511
                self.match(SetlXgrammarParser.T__59)
                self.state = 512
                localctx._prefixOperation = self.prefixOperation(localctx.enableIgnore)
                localctx.p = ProductOfMembers(localctx._prefixOperation.p) 
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 515
                self.match(SetlXgrammarParser.T__61)
                self.state = 516
                localctx._prefixOperation = self.prefixOperation(localctx.enableIgnore)
                localctx.p = Cardinality(localctx._prefixOperation.p) 
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 519
                self.match(SetlXgrammarParser.T__52)
                self.state = 520
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
            self.state = 580
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,39,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 525
                self.match(SetlXgrammarParser.T__62)
                self.state = 526
                localctx._factor = self.factor(localctx.enableIgnore)
                localctx.f = Not(localctx._factor.f) 
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 529
                self.match(SetlXgrammarParser.T__63)
                self.state = 530
                self.match(SetlXgrammarParser.T__1)
                self.state = 531
                localctx._iteratorChain = self.iteratorChain(localctx.enableIgnore)
                self.state = 532
                self.match(SetlXgrammarParser.T__13)
                self.state = 533
                localctx._condition = self.condition()
                self.state = 534
                self.match(SetlXgrammarParser.T__2)
                localctx.f = Forall(localctx._iteratorChain.ic,localctx._condition.cnd)
                		
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 537
                self.match(SetlXgrammarParser.T__64)
                self.state = 538
                self.match(SetlXgrammarParser.T__1)
                self.state = 539
                localctx._iteratorChain = self.iteratorChain(localctx.enableIgnore)
                self.state = 540
                self.match(SetlXgrammarParser.T__13)
                self.state = 541
                localctx._condition = self.condition()
                self.state = 542
                self.match(SetlXgrammarParser.T__2)
                localctx.f = Exists(localctx._iteratorChain.ic,localctx._condition.cnd)
                		
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 556
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [SetlXgrammarParser.T__1]:
                    self.state = 545
                    self.match(SetlXgrammarParser.T__1)
                    self.state = 546
                    localctx._exprContent = self.exprContent(localctx.enableIgnore)
                    self.state = 547
                    self.match(SetlXgrammarParser.T__2)
                    localctx.f = localctx._exprContent.ex 
                    pass
                elif token in [SetlXgrammarParser.T__65, SetlXgrammarParser.T__66, SetlXgrammarParser.T__67]:
                    self.state = 550
                    localctx._procedure = self.procedure()
                    localctx.f = localctx._procedure.pd 
                    pass
                elif token in [SetlXgrammarParser.ID]:
                    self.state = 553
                    localctx._variable = self.variable()
                    localctx.f = localctx._variable.v 
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 567
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << SetlXgrammarParser.T__1) | (1 << SetlXgrammarParser.T__33) | (1 << SetlXgrammarParser.T__34))) != 0):
                    self.state = 565
                    self._errHandler.sync(self)
                    token = self._input.LA(1)
                    if token in [SetlXgrammarParser.T__33]:
                        self.state = 558
                        self.match(SetlXgrammarParser.T__33)
                        self.state = 559
                        localctx._variable = self.variable()
                        localctx.f = MemberAccess(localctx.f,localctx._variable.v) 
                        pass
                    elif token in [SetlXgrammarParser.T__1, SetlXgrammarParser.T__34]:
                        self.state = 562
                        localctx._call = self.call(localctx.enableIgnore)

                        localctx._call.c.callable = localctx.f
                        localctx.f = localctx._call.c
                                
                        pass
                    else:
                        raise NoViableAltException(self)

                    self.state = 569
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 572
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==SetlXgrammarParser.T__62:
                    self.state = 570
                    self.match(SetlXgrammarParser.T__62)
                    localctx.f = Factorial(localctx.f) 


                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 574
                localctx._value = self.value(localctx.enableIgnore)
                localctx.f = localctx._value.v 
                self.state = 578
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==SetlXgrammarParser.T__62:
                    self.state = 576
                    self.match(SetlXgrammarParser.T__62)
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
            self.state = 609
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [SetlXgrammarParser.T__65]:
                self.enterOuterAlt(localctx, 1)
                self.state = 582
                self.match(SetlXgrammarParser.T__65)
                self.state = 583
                self.match(SetlXgrammarParser.T__1)
                self.state = 584
                localctx._procedureParameters = self.procedureParameters(True)
                self.state = 585
                self.match(SetlXgrammarParser.T__2)
                self.state = 586
                self.match(SetlXgrammarParser.T__3)
                self.state = 587
                localctx._block = self.block()
                self.state = 588
                self.match(SetlXgrammarParser.T__5)
                localctx.pd = Procedure(localctx._procedureParameters.paramList, localctx._block.blk) 
                		
                pass
            elif token in [SetlXgrammarParser.T__66]:
                self.enterOuterAlt(localctx, 2)
                self.state = 591
                self.match(SetlXgrammarParser.T__66)
                self.state = 592
                self.match(SetlXgrammarParser.T__1)
                self.state = 593
                localctx._procedureParameters = self.procedureParameters(False)
                self.state = 594
                self.match(SetlXgrammarParser.T__2)
                self.state = 595
                self.match(SetlXgrammarParser.T__3)
                self.state = 596
                localctx._block = self.block()
                self.state = 597
                self.match(SetlXgrammarParser.T__5)
                localctx.pd = CachedProcedure(localctx._procedureParameters.paramList, localctx._block.blk) 
                		
                pass
            elif token in [SetlXgrammarParser.T__67]:
                self.enterOuterAlt(localctx, 3)
                self.state = 600
                self.match(SetlXgrammarParser.T__67)
                self.state = 601
                self.match(SetlXgrammarParser.T__1)
                self.state = 602
                localctx._procedureParameters = self.procedureParameters(True)
                self.state = 603
                self.match(SetlXgrammarParser.T__2)
                self.state = 604
                self.match(SetlXgrammarParser.T__3)
                self.state = 605
                localctx._block = self.block()
                self.state = 606
                self.match(SetlXgrammarParser.T__5)
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
            self.lp1 = None # ProcedureListParameterContext
            self.dp2 = None # ProcedureDefaultParameterContext
            self.dp3 = None # ProcedureDefaultParameterContext
            self.lp2 = None # ProcedureListParameterContext
            self.lp3 = None # ProcedureListParameterContext
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


        def procedureListParameter(self):
            return self.getTypedRuleContext(SetlXgrammarParser.ProcedureListParameterContext,0)


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
            self.state = 658
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,46,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 611
                localctx.pp1 = self.procedureParameter(localctx.enableRw)
                localctx.paramList.append(localctx.pp1.param) 
                self.state = 619
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,41,self._ctx)
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1:
                        self.state = 613
                        self.match(SetlXgrammarParser.T__25)
                        self.state = 614
                        localctx.pp2 = self.procedureParameter(localctx.enableRw)
                        localctx.paramList.append(localctx.pp2.param)  
                    self.state = 621
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,41,self._ctx)

                self.state = 628
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,42,self._ctx)
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1:
                        self.state = 622
                        self.match(SetlXgrammarParser.T__25)
                        self.state = 623
                        localctx.dp1 = self.procedureDefaultParameter()
                        localctx.paramList.append(localctx.dp1.param)  
                    self.state = 630
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,42,self._ctx)

                self.state = 635
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==SetlXgrammarParser.T__25:
                    self.state = 631
                    self.match(SetlXgrammarParser.T__25)
                    self.state = 632
                    localctx.lp1 = self.procedureListParameter()
                    localctx.paramList.append(localctx.lp1.param) 


                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 637
                localctx.dp2 = self.procedureDefaultParameter()
                localctx.paramList.append(localctx.dp2.param) 
                self.state = 645
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,44,self._ctx)
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1:
                        self.state = 639
                        self.match(SetlXgrammarParser.T__25)
                        self.state = 640
                        localctx.dp3 = self.procedureDefaultParameter()
                        localctx.paramList.append(localctx.dp3.param)  
                    self.state = 647
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,44,self._ctx)

                self.state = 652
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==SetlXgrammarParser.T__25:
                    self.state = 648
                    self.match(SetlXgrammarParser.T__25)
                    self.state = 649
                    localctx.lp2 = self.procedureListParameter()
                    localctx.paramList.append(localctx.lp2.param) 


                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 654
                localctx.lp3 = self.procedureListParameter()
                localctx.paramList.append(localctx.lp3.param) 
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)

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
            self.state = 668
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,47,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 660
                if not localctx.enableRw:
                    from antlr4.error.Errors import FailedPredicateException
                    raise FailedPredicateException(self, "$enableRw")
                self.state = 661
                self.match(SetlXgrammarParser.T__68)
                self.state = 662
                localctx._assignableVariable = self.assignableVariable()
                localctx.param = ReadWriteParameter(localctx._assignableVariable.v.id) 
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 665
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
            self.state = 670
            localctx._assignableVariable = self.assignableVariable()
            self.state = 671
            self.match(SetlXgrammarParser.T__32)
            self.state = 672
            localctx._expr = self.expr(False)
            localctx.param = Parameter(localctx._assignableVariable.v.id, localctx._expr.ex) 
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ProcedureListParameterContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.param = None
            self._variable = None # VariableContext

        def variable(self):
            return self.getTypedRuleContext(SetlXgrammarParser.VariableContext,0)


        def getRuleIndex(self):
            return SetlXgrammarParser.RULE_procedureListParameter

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProcedureListParameter" ):
                listener.enterProcedureListParameter(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProcedureListParameter" ):
                listener.exitProcedureListParameter(self)




    def procedureListParameter(self):

        localctx = SetlXgrammarParser.ProcedureListParameterContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_procedureListParameter)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 675
            self.match(SetlXgrammarParser.T__53)
            self.state = 676
            localctx._variable = self.variable()
            localctx.param = ListParameter(localctx._variable.v.id) 
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
        self.enterRule(localctx, 50, self.RULE_call)
        try:
            self.state = 689
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [SetlXgrammarParser.T__1]:
                self.enterOuterAlt(localctx, 1)
                self.state = 679
                self.match(SetlXgrammarParser.T__1)
                self.state = 680
                localctx._callParameters = self.callParameters(localctx.enableIgnore)
                self.state = 681
                self.match(SetlXgrammarParser.T__2)
                localctx.c = FunctionCall(localctx._callParameters.params) 
                		
                pass
            elif token in [SetlXgrammarParser.T__34]:
                self.enterOuterAlt(localctx, 2)
                self.state = 684
                self.match(SetlXgrammarParser.T__34)
                self.state = 685
                localctx._collectionAccessParams = self.collectionAccessParams(localctx.enableIgnore)
                self.state = 686
                self.match(SetlXgrammarParser.T__35)
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
        self.enterRule(localctx, 52, self.RULE_collectionAccessParams)

        params = []
            
        self._la = 0 # Token type
        try:
            self.state = 716
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,52,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 691
                localctx.e1 = self.expr(localctx.enableIgnore)
                self.state = 710
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [SetlXgrammarParser.RANGE_SIGN]:
                    self.state = 692
                    self.match(SetlXgrammarParser.RANGE_SIGN)
                    self.state = 697
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,49,self._ctx)
                    if la_ == 1:
                        self.state = 693
                        localctx.e2 = self.expr(localctx.enableIgnore)
                        localctx.p = ListRange(localctx.e1.ex,localctx.e2.ex) 
                        pass

                    elif la_ == 2:
                        localctx.p = ListRange(localctx.e1.ex,None) 
                        pass


                    pass
                elif token in [SetlXgrammarParser.T__25]:
                    self.state = 703 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    while True:
                        self.state = 699
                        self.match(SetlXgrammarParser.T__25)
                        self.state = 700
                        localctx.e3 = self.expr(False)
                        params.append(localctx.e3.ex) 
                        self.state = 705 
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)
                        if not (_la==SetlXgrammarParser.T__25):
                            break

                    localctx.p = params 
                    pass
                elif token in [SetlXgrammarParser.T__35]:
                    localctx.p = localctx.e1.ex 
                    pass
                else:
                    raise NoViableAltException(self)

                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 712
                self.match(SetlXgrammarParser.RANGE_SIGN)
                self.state = 713
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
            self._exprList = None # ExprListContext
            self._exprContent = None # ExprContentContext
            self.enableIgnore = enableIgnore

        def exprList(self):
            return self.getTypedRuleContext(SetlXgrammarParser.ExprListContext,0)


        def exprContent(self):
            return self.getTypedRuleContext(SetlXgrammarParser.ExprContentContext,0)


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
        self.enterRule(localctx, 54, self.RULE_callParameters)

        localctx.params = []
            
        self._la = 0 # Token type
        try:
            self.state = 732
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,54,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 718
                localctx._exprList = self.exprList(localctx.enableIgnore)
                localctx.params = localctx._exprList.exprs
                self.state = 725
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==SetlXgrammarParser.T__25:
                    self.state = 720
                    self.match(SetlXgrammarParser.T__25)
                    self.state = 721
                    self.match(SetlXgrammarParser.T__53)
                    self.state = 722
                    localctx._exprContent = self.exprContent(False)
                    localctx.params.append(OperatorExpression(localctx._exprContent.ex))


                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 727
                self.match(SetlXgrammarParser.T__53)
                self.state = 728
                localctx._exprContent = self.exprContent(False)
                localctx.params = [OperatorExpression(localctx._exprContent.ex)]
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
        self.enterRule(localctx, 56, self.RULE_value)

        cb = None
            
        try:
            self.state = 760
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,57,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 734
                self.match(SetlXgrammarParser.T__34)
                self.state = 738
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,55,self._ctx)
                if la_ == 1:
                    self.state = 735
                    localctx._collectionBuilder = self.collectionBuilder(localctx.enableIgnore)
                    cb = localctx._collectionBuilder.cb; 


                self.state = 740
                self.match(SetlXgrammarParser.T__35)
                localctx.v = SetlXList(cb) 
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 742
                self.match(SetlXgrammarParser.T__3)
                self.state = 746
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,56,self._ctx)
                if la_ == 1:
                    self.state = 743
                    localctx._collectionBuilder = self.collectionBuilder(localctx.enableIgnore)
                    cb = localctx._collectionBuilder.cb; 


                self.state = 748
                self.match(SetlXgrammarParser.T__5)
                localctx.v = SetListConstructor(cb) 
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 750
                localctx._STRING = self.match(SetlXgrammarParser.STRING)
                localctx.v = SetlXString((None if localctx._STRING is None else localctx._STRING.text)) 
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 752
                localctx._LITERAL = self.match(SetlXgrammarParser.LITERAL)
                localctx.v = SetlXLiteral((None if localctx._LITERAL is None else localctx._LITERAL.text)) 
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 754
                localctx._atomicValue = self.atomicValue()
                localctx.v = localctx._atomicValue.av 
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 757
                if not localctx.enableIgnore:
                    from antlr4.error.Errors import FailedPredicateException
                    raise FailedPredicateException(self, "$enableIgnore")
                self.state = 758
                self.match(SetlXgrammarParser.T__36)
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
        self.enterRule(localctx, 58, self.RULE_collectionBuilder)

        exprs = []
            
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 762
            localctx.e1 = self.expr(localctx.enableIgnore)
            self.state = 809
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [SetlXgrammarParser.T__25]:
                self.state = 763
                self.match(SetlXgrammarParser.T__25)
                self.state = 764
                localctx.e2 = self.expr(localctx.enableIgnore)
                self.state = 786
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [SetlXgrammarParser.RANGE_SIGN]:
                    self.state = 765
                    self.match(SetlXgrammarParser.RANGE_SIGN)
                    self.state = 766
                    localctx.e3 = self.expr(localctx.enableIgnore)
                    localctx.cb = Range(localctx.e1.ex, localctx.e2.ex, localctx.e3.ex) 
                    pass
                elif token in [SetlXgrammarParser.T__5, SetlXgrammarParser.T__13, SetlXgrammarParser.T__25, SetlXgrammarParser.T__35]:
                    exprs.append(localctx.e1.ex); exprs.append(localctx.e2.ex) 
                    self.state = 776
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    while _la==SetlXgrammarParser.T__25:
                        self.state = 770
                        self.match(SetlXgrammarParser.T__25)
                        self.state = 771
                        localctx.e3 = self.expr(localctx.enableIgnore)
                        exprs.append(localctx.e3.ex) 
                        self.state = 778
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)

                    self.state = 784
                    self._errHandler.sync(self)
                    token = self._input.LA(1)
                    if token in [SetlXgrammarParser.T__13]:
                        self.state = 779
                        self.match(SetlXgrammarParser.T__13)
                        self.state = 780
                        localctx.e4 = self.expr(False)
                        localctx.cb = ExplicitListWithRest(exprs, localctx.e4.ex) 
                        pass
                    elif token in [SetlXgrammarParser.T__5, SetlXgrammarParser.T__35]:
                        localctx.cb = ExplicitList(exprs)         
                        pass
                    else:
                        raise NoViableAltException(self)

                    pass
                else:
                    raise NoViableAltException(self)

                pass
            elif token in [SetlXgrammarParser.RANGE_SIGN]:
                self.state = 788
                self.match(SetlXgrammarParser.RANGE_SIGN)
                self.state = 789
                localctx.e3 = self.expr(localctx.enableIgnore)
                localctx.cb = Range(localctx.e1.ex, None, localctx.e3.ex) 
                pass
            elif token in [SetlXgrammarParser.T__5, SetlXgrammarParser.T__13, SetlXgrammarParser.T__35]:
                exprs.append(localctx.e1.ex) 
                self.state = 798
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [SetlXgrammarParser.T__13]:
                    self.state = 793
                    self.match(SetlXgrammarParser.T__13)
                    self.state = 794
                    localctx.e2 = self.expr(False)
                    localctx.cb = ExplicitListWithRest(exprs, localctx.e2.ex) 
                    pass
                elif token in [SetlXgrammarParser.T__5, SetlXgrammarParser.T__35]:
                    localctx.cb = ExplicitList(exprs)         
                    pass
                else:
                    raise NoViableAltException(self)

                pass
            elif token in [SetlXgrammarParser.T__10]:
                self.state = 800
                self.match(SetlXgrammarParser.T__10)
                self.state = 801
                localctx._iteratorChain = self.iteratorChain(localctx.enableIgnore)
                self.state = 807
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [SetlXgrammarParser.T__13]:
                    self.state = 802
                    self.match(SetlXgrammarParser.T__13)
                    self.state = 803
                    localctx.c1 = self.condition()
                    localctx.cb = SetlIteration(localctx.e1.ex, localctx._iteratorChain.ic, localctx.c1.cnd) 
                    pass
                elif token in [SetlXgrammarParser.T__5, SetlXgrammarParser.T__35]:
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
        self.enterRule(localctx, 60, self.RULE_iteratorChain)

        localctx.ic = []
            
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 811
            localctx.i1 = self.iterator(localctx.enableIgnore)
            localctx.ic.append(localctx.i1.iter)
            self.state = 819
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==SetlXgrammarParser.T__25:
                self.state = 813
                self.match(SetlXgrammarParser.T__25)
                self.state = 814
                localctx.i2 = self.iterator(localctx.enableIgnore)
                localctx.ic.append(localctx.i2.iter) 
                self.state = 821
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
        self.enterRule(localctx, 62, self.RULE_iterator)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 822
            localctx._assignable = self.assignable(True)
            self.state = 823
            self.match(SetlXgrammarParser.T__49)
            self.state = 824
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
        self.enterRule(localctx, 64, self.RULE_atomicValue)
        try:
            self.state = 837
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [SetlXgrammarParser.NUMBER]:
                self.enterOuterAlt(localctx, 1)
                self.state = 827
                localctx._NUMBER = self.match(SetlXgrammarParser.NUMBER)
                localctx.av = SetlXFraction((None if localctx._NUMBER is None else localctx._NUMBER.text)) 
                pass
            elif token in [SetlXgrammarParser.DOUBLE]:
                self.enterOuterAlt(localctx, 2)
                self.state = 829
                localctx._DOUBLE = self.match(SetlXgrammarParser.DOUBLE)
                localctx.av = float((None if localctx._DOUBLE is None else localctx._DOUBLE.text)) 
                pass
            elif token in [SetlXgrammarParser.T__69]:
                self.enterOuterAlt(localctx, 3)
                self.state = 831
                self.match(SetlXgrammarParser.T__69)
                localctx.av = SetlXOm() 
                pass
            elif token in [SetlXgrammarParser.T__70]:
                self.enterOuterAlt(localctx, 4)
                self.state = 833
                self.match(SetlXgrammarParser.T__70)
                localctx.av = SetlXTrue() 
                pass
            elif token in [SetlXgrammarParser.T__71]:
                self.enterOuterAlt(localctx, 5)
                self.state = 835
                self.match(SetlXgrammarParser.T__71)
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
        self.enterRule(localctx, 66, self.RULE_variable)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 839
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
        self.enterRule(localctx, 68, self.RULE_condition)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 842
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
        self.enterRule(localctx, 70, self.RULE_assignmentList)

        localctx.al = []
            
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 845
            localctx.a1 = self.assignable(True)
            localctx.al.append(localctx.a1.a) 
            self.state = 853
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==SetlXgrammarParser.T__25:
                self.state = 847
                self.match(SetlXgrammarParser.T__25)
                self.state = 848
                localctx.a2 = self.assignable(True)
                localctx.al.append(localctx.a2.a) 
                self.state = 855
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
        self._predicates[28] = self.value_sempred
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
         




