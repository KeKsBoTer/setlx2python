# Generated from grammar/SetlXgrammar.g4 by ANTLR 4.7.1
# encoding: utf-8
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys


from .types import *

def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3T")
        buf.write("\u0365\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31")
        buf.write("\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36")
        buf.write("\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%\4&\t")
        buf.write("&\3\2\3\2\3\2\7\2P\n\2\f\2\16\2S\13\2\3\2\3\2\3\3\3\3")
        buf.write("\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\5\3d\n\3")
        buf.write("\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3")
        buf.write("\3\3\3\3\3\3\3\3\3\3\3\3\3\7\3z\n\3\f\3\16\3}\13\3\3\3")
        buf.write("\3\3\3\3\3\3\3\3\3\3\5\3\u0085\n\3\3\3\3\3\3\3\3\3\3\3")
        buf.write("\3\3\3\3\3\3\3\3\3\3\7\3\u0091\n\3\f\3\16\3\u0094\13\3")
        buf.write("\3\3\3\3\3\3\5\3\u0099\n\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3")
        buf.write("\3\3\3\3\5\3\u00a4\n\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3")
        buf.write("\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3")
        buf.write("\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3")
        buf.write("\3\3\3\3\3\3\3\3\5\3\u00cd\n\3\3\3\3\3\3\3\3\3\3\3\3\3")
        buf.write("\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\5\3\u00e1")
        buf.write("\n\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3")
        buf.write("\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\5\3\u00fa\n")
        buf.write("\3\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4")
        buf.write("\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\5\4\u0115")
        buf.write("\n\4\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\5\5\u011f\n\5\3\6")
        buf.write("\3\6\3\6\3\6\3\6\3\6\3\6\3\6\5\6\u0129\n\6\3\7\3\7\3\7")
        buf.write("\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\7\7\u0136\n\7\f\7\16")
        buf.write("\7\u0139\13\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\5\7\u0143")
        buf.write("\n\7\3\b\3\b\3\b\3\t\3\t\3\t\3\n\3\n\3\n\3\n\3\n\3\n\7")
        buf.write("\n\u0151\n\n\f\n\16\n\u0154\13\n\3\13\3\13\3\13\3\13\3")
        buf.write("\13\3\13\3\13\3\13\3\13\3\13\3\13\3\13\3\13\5\13\u0163")
        buf.write("\n\13\5\13\u0165\n\13\3\f\3\f\3\f\3\f\3\f\3\r\3\r\3\r")
        buf.write("\3\r\3\r\3\r\3\r\3\r\3\r\3\r\7\r\u0176\n\r\f\r\16\r\u0179")
        buf.write("\13\r\5\r\u017b\n\r\3\r\5\r\u017e\n\r\3\16\3\16\3\16\3")
        buf.write("\16\3\16\3\16\5\16\u0186\n\16\3\17\3\17\3\17\3\17\3\17")
        buf.write("\3\17\7\17\u018e\n\17\f\17\16\17\u0191\13\17\3\20\3\20")
        buf.write("\3\20\3\20\3\20\3\20\7\20\u0199\n\20\f\20\16\20\u019c")
        buf.write("\13\20\3\21\3\21\3\21\3\21\3\21\3\21\3\21\3\21\3\21\3")
        buf.write("\21\3\21\3\21\3\21\3\21\3\21\3\21\3\21\3\21\3\21\3\21")
        buf.write("\3\21\3\21\3\21\3\21\3\21\3\21\3\21\3\21\3\21\3\21\3\21")
        buf.write("\3\21\3\21\3\21\5\21\u01c0\n\21\3\22\3\22\3\22\3\22\3")
        buf.write("\22\3\22\3\22\3\22\3\22\3\22\7\22\u01cc\n\22\f\22\16\22")
        buf.write("\u01cf\13\22\3\23\3\23\3\23\3\23\3\23\3\23\3\23\3\23\3")
        buf.write("\23\3\23\3\23\3\23\3\23\3\23\3\23\3\23\3\23\3\23\3\23")
        buf.write("\3\23\3\23\3\23\7\23\u01e7\n\23\f\23\16\23\u01ea\13\23")
        buf.write("\3\24\3\24\3\24\3\24\3\24\3\24\3\24\3\24\3\24\3\24\7\24")
        buf.write("\u01f6\n\24\f\24\16\24\u01f9\13\24\3\25\3\25\3\25\3\25")
        buf.write("\3\25\3\25\5\25\u0201\n\25\3\25\3\25\3\25\3\25\3\25\3")
        buf.write("\25\3\25\3\25\3\25\3\25\3\25\3\25\3\25\3\25\3\25\3\25")
        buf.write("\5\25\u0213\n\25\3\26\3\26\3\26\3\26\3\26\3\26\3\26\3")
        buf.write("\26\3\26\3\26\3\26\3\26\3\26\3\26\3\26\3\26\3\26\3\26")
        buf.write("\3\26\3\26\3\26\3\26\3\26\3\26\3\26\3\26\3\26\3\26\3\26")
        buf.write("\3\26\3\26\5\26\u0234\n\26\3\26\3\26\3\26\3\26\3\26\3")
        buf.write("\26\3\26\7\26\u023d\n\26\f\26\16\26\u0240\13\26\3\26\3")
        buf.write("\26\5\26\u0244\n\26\3\26\3\26\3\26\3\26\5\26\u024a\n\26")
        buf.write("\5\26\u024c\n\26\3\27\3\27\3\27\3\27\3\27\3\27\3\27\3")
        buf.write("\27\3\27\3\27\3\27\3\27\3\27\3\27\3\27\3\27\3\27\3\27")
        buf.write("\3\27\3\27\3\27\3\27\3\27\3\27\3\27\3\27\3\27\5\27\u0269")
        buf.write("\n\27\3\30\3\30\3\30\3\30\3\30\3\30\7\30\u0271\n\30\f")
        buf.write("\30\16\30\u0274\13\30\3\30\3\30\3\30\3\30\7\30\u027a\n")
        buf.write("\30\f\30\16\30\u027d\13\30\3\30\3\30\3\30\3\30\5\30\u0283")
        buf.write("\n\30\3\30\3\30\3\30\3\30\3\30\3\30\7\30\u028b\n\30\f")
        buf.write("\30\16\30\u028e\13\30\3\30\3\30\3\30\3\30\5\30\u0294\n")
        buf.write("\30\3\30\3\30\3\30\3\30\5\30\u029a\n\30\3\31\3\31\3\31")
        buf.write("\3\31\3\31\3\31\3\31\3\31\5\31\u02a4\n\31\3\32\3\32\3")
        buf.write("\32\3\32\3\32\3\33\3\33\3\33\3\33\3\34\3\34\3\34\3\34")
        buf.write("\3\34\3\34\3\34\3\34\3\34\3\34\3\34\3\34\3\34\3\34\3\34")
        buf.write("\5\34\u02be\n\34\3\35\3\35\3\35\3\35\3\35\3\35\5\35\u02c6")
        buf.write("\n\35\3\35\3\35\3\35\3\35\6\35\u02cc\n\35\r\35\16\35\u02cd")
        buf.write("\3\35\3\35\3\35\5\35\u02d3\n\35\3\35\3\35\3\35\3\35\5")
        buf.write("\35\u02d9\n\35\3\36\3\36\3\36\3\36\3\36\3\36\3\36\5\36")
        buf.write("\u02e2\n\36\3\36\3\36\3\36\3\36\3\36\5\36\u02e9\n\36\3")
        buf.write("\37\3\37\3\37\3\37\5\37\u02ef\n\37\3\37\3\37\3\37\3\37")
        buf.write("\3\37\3\37\5\37\u02f7\n\37\3\37\3\37\3\37\3\37\3\37\3")
        buf.write("\37\3\37\3\37\3\37\3\37\3\37\3\37\5\37\u0305\n\37\3 \3")
        buf.write(" \3 \3 \3 \3 \3 \3 \3 \3 \3 \3 \7 \u0313\n \f \16 \u0316")
        buf.write("\13 \3 \3 \3 \3 \3 \5 \u031d\n \5 \u031f\n \3 \3 \3 \3")
        buf.write(" \3 \3 \3 \3 \3 \3 \5 \u032b\n \3 \3 \3 \3 \3 \3 \3 \5")
        buf.write(" \u0334\n \5 \u0336\n \3!\3!\3!\3!\3!\3!\7!\u033e\n!\f")
        buf.write("!\16!\u0341\13!\3\"\3\"\3\"\3\"\3\"\3#\3#\3#\3#\3#\3#")
        buf.write("\3#\3#\3#\3#\5#\u0352\n#\3$\3$\3$\3%\3%\3%\3&\3&\3&\3")
        buf.write("&\3&\3&\7&\u0360\n&\f&\16&\u0363\13&\3&\2\2\'\2\4\6\b")
        buf.write("\n\f\16\20\22\24\26\30\32\34\36 \"$&(*,.\60\62\64\668")
        buf.write(":<>@BDFHJ\2\2\2\u03b6\2Q\3\2\2\2\4\u00f9\3\2\2\2\6\u00fb")
        buf.write("\3\2\2\2\b\u011e\3\2\2\2\n\u0120\3\2\2\2\f\u0142\3\2\2")
        buf.write("\2\16\u0144\3\2\2\2\20\u0147\3\2\2\2\22\u014a\3\2\2\2")
        buf.write("\24\u0164\3\2\2\2\26\u0166\3\2\2\2\30\u017d\3\2\2\2\32")
        buf.write("\u017f\3\2\2\2\34\u0187\3\2\2\2\36\u0192\3\2\2\2 \u019d")
        buf.write("\3\2\2\2\"\u01c1\3\2\2\2$\u01d0\3\2\2\2&\u01eb\3\2\2\2")
        buf.write("(\u0212\3\2\2\2*\u024b\3\2\2\2,\u0268\3\2\2\2.\u0299\3")
        buf.write("\2\2\2\60\u02a3\3\2\2\2\62\u02a5\3\2\2\2\64\u02aa\3\2")
        buf.write("\2\2\66\u02bd\3\2\2\28\u02d8\3\2\2\2:\u02e8\3\2\2\2<\u0304")
        buf.write("\3\2\2\2>\u0306\3\2\2\2@\u0337\3\2\2\2B\u0342\3\2\2\2")
        buf.write("D\u0351\3\2\2\2F\u0353\3\2\2\2H\u0356\3\2\2\2J\u0359\3")
        buf.write("\2\2\2LM\5\4\3\2MN\b\2\1\2NP\3\2\2\2OL\3\2\2\2PS\3\2\2")
        buf.write("\2QO\3\2\2\2QR\3\2\2\2RT\3\2\2\2SQ\3\2\2\2TU\b\2\1\2U")
        buf.write("\3\3\2\2\2VW\7\3\2\2WX\7K\2\2XY\7\4\2\2YZ\5.\30\2Z[\7")
        buf.write("\5\2\2[\\\7\6\2\2\\c\5\2\2\2]^\7\7\2\2^_\7\6\2\2_`\5\2")
        buf.write("\2\2`a\7\b\2\2ab\b\3\1\2bd\3\2\2\2c]\3\2\2\2cd\3\2\2\2")
        buf.write("de\3\2\2\2ef\7\b\2\2fg\b\3\1\2g\u00fa\3\2\2\2hi\7\t\2")
        buf.write("\2ij\7\4\2\2jk\5H%\2kl\7\5\2\2lm\7\6\2\2mn\5\2\2\2n{\7")
        buf.write("\b\2\2op\7\n\2\2pq\7\t\2\2qr\7\4\2\2rs\5H%\2st\7\5\2\2")
        buf.write("tu\7\6\2\2uv\5\2\2\2vw\7\b\2\2wx\b\3\1\2xz\3\2\2\2yo\3")
        buf.write("\2\2\2z}\3\2\2\2{y\3\2\2\2{|\3\2\2\2|\u0084\3\2\2\2}{")
        buf.write("\3\2\2\2~\177\7\n\2\2\177\u0080\7\6\2\2\u0080\u0081\5")
        buf.write("\2\2\2\u0081\u0082\7\b\2\2\u0082\u0083\b\3\1\2\u0083\u0085")
        buf.write("\3\2\2\2\u0084~\3\2\2\2\u0084\u0085\3\2\2\2\u0085\u0086")
        buf.write("\3\2\2\2\u0086\u0087\b\3\1\2\u0087\u00fa\3\2\2\2\u0088")
        buf.write("\u0089\7\13\2\2\u0089\u0092\7\6\2\2\u008a\u008b\7\f\2")
        buf.write("\2\u008b\u008c\5H%\2\u008c\u008d\7\r\2\2\u008d\u008e\5")
        buf.write("\2\2\2\u008e\u008f\b\3\1\2\u008f\u0091\3\2\2\2\u0090\u008a")
        buf.write("\3\2\2\2\u0091\u0094\3\2\2\2\u0092\u0090\3\2\2\2\u0092")
        buf.write("\u0093\3\2\2\2\u0093\u0098\3\2\2\2\u0094\u0092\3\2\2\2")
        buf.write("\u0095\u0096\7\16\2\2\u0096\u0097\7\r\2\2\u0097\u0099")
        buf.write("\5\2\2\2\u0098\u0095\3\2\2\2\u0098\u0099\3\2\2\2\u0099")
        buf.write("\u009a\3\2\2\2\u009a\u009b\7\b\2\2\u009b\u00fa\b\3\1\2")
        buf.write("\u009c\u009d\7\17\2\2\u009d\u009e\7\4\2\2\u009e\u00a3")
        buf.write("\5@!\2\u009f\u00a0\7\20\2\2\u00a0\u00a1\5H%\2\u00a1\u00a2")
        buf.write("\b\3\1\2\u00a2\u00a4\3\2\2\2\u00a3\u009f\3\2\2\2\u00a3")
        buf.write("\u00a4\3\2\2\2\u00a4\u00a5\3\2\2\2\u00a5\u00a6\7\5\2\2")
        buf.write("\u00a6\u00a7\7\6\2\2\u00a7\u00a8\5\2\2\2\u00a8\u00a9\7")
        buf.write("\b\2\2\u00a9\u00aa\b\3\1\2\u00aa\u00fa\3\2\2\2\u00ab\u00ac")
        buf.write("\7\21\2\2\u00ac\u00ad\7\4\2\2\u00ad\u00ae\5H%\2\u00ae")
        buf.write("\u00af\7\5\2\2\u00af\u00b0\7\6\2\2\u00b0\u00b1\5\2\2\2")
        buf.write("\u00b1\u00b2\7\b\2\2\u00b2\u00b3\b\3\1\2\u00b3\u00fa\3")
        buf.write("\2\2\2\u00b4\u00b5\7\22\2\2\u00b5\u00b6\7\6\2\2\u00b6")
        buf.write("\u00b7\5\2\2\2\u00b7\u00b8\7\b\2\2\u00b8\u00b9\7\21\2")
        buf.write("\2\u00b9\u00ba\7\4\2\2\u00ba\u00bb\5H%\2\u00bb\u00bc\7")
        buf.write("\5\2\2\u00bc\u00bd\7\23\2\2\u00bd\u00be\b\3\1\2\u00be")
        buf.write("\u00fa\3\2\2\2\u00bf\u00c0\7\24\2\2\u00c0\u00c1\7\6\2")
        buf.write("\2\u00c1\u00c2\5\2\2\2\u00c2\u00cc\7\b\2\2\u00c3\u00c4")
        buf.write("\7\25\2\2\u00c4\u00c5\7\4\2\2\u00c5\u00c6\5\16\b\2\u00c6")
        buf.write("\u00c7\7\5\2\2\u00c7\u00c8\7\6\2\2\u00c8\u00c9\5\2\2\2")
        buf.write("\u00c9\u00ca\7\b\2\2\u00ca\u00cb\b\3\1\2\u00cb\u00cd\3")
        buf.write("\2\2\2\u00cc\u00c3\3\2\2\2\u00cc\u00cd\3\2\2\2\u00cd\u00ce")
        buf.write("\3\2\2\2\u00ce\u00cf\b\3\1\2\u00cf\u00fa\3\2\2\2\u00d0")
        buf.write("\u00d1\7\26\2\2\u00d1\u00d2\7\23\2\2\u00d2\u00fa\b\3\1")
        buf.write("\2\u00d3\u00d4\7\27\2\2\u00d4\u00d5\7\23\2\2\u00d5\u00fa")
        buf.write("\b\3\1\2\u00d6\u00d7\7\30\2\2\u00d7\u00d8\7\23\2\2\u00d8")
        buf.write("\u00fa\b\3\1\2\u00d9\u00da\7\31\2\2\u00da\u00db\7\23\2")
        buf.write("\2\u00db\u00fa\b\3\1\2\u00dc\u00e0\7\32\2\2\u00dd\u00de")
        buf.write("\5\20\t\2\u00de\u00df\b\3\1\2\u00df\u00e1\3\2\2\2\u00e0")
        buf.write("\u00dd\3\2\2\2\u00e0\u00e1\3\2\2\2\u00e1\u00e2\3\2\2\2")
        buf.write("\u00e2\u00e3\7\23\2\2\u00e3\u00fa\b\3\1\2\u00e4\u00e5")
        buf.write("\7\33\2\2\u00e5\u00e6\7\4\2\2\u00e6\u00e7\5H%\2\u00e7")
        buf.write("\u00e8\7\34\2\2\u00e8\u00e9\5\20\t\2\u00e9\u00ea\7\5\2")
        buf.write("\2\u00ea\u00eb\7\23\2\2\u00eb\u00ec\b\3\1\2\u00ec\u00fa")
        buf.write("\3\2\2\2\u00ed\u00ee\5\6\4\2\u00ee\u00ef\7\23\2\2\u00ef")
        buf.write("\u00f0\b\3\1\2\u00f0\u00fa\3\2\2\2\u00f1\u00f2\5\b\5\2")
        buf.write("\u00f2\u00f3\7\23\2\2\u00f3\u00f4\b\3\1\2\u00f4\u00fa")
        buf.write("\3\2\2\2\u00f5\u00f6\5\20\t\2\u00f6\u00f7\7\23\2\2\u00f7")
        buf.write("\u00f8\b\3\1\2\u00f8\u00fa\3\2\2\2\u00f9V\3\2\2\2\u00f9")
        buf.write("h\3\2\2\2\u00f9\u0088\3\2\2\2\u00f9\u009c\3\2\2\2\u00f9")
        buf.write("\u00ab\3\2\2\2\u00f9\u00b4\3\2\2\2\u00f9\u00bf\3\2\2\2")
        buf.write("\u00f9\u00d0\3\2\2\2\u00f9\u00d3\3\2\2\2\u00f9\u00d6\3")
        buf.write("\2\2\2\u00f9\u00d9\3\2\2\2\u00f9\u00dc\3\2\2\2\u00f9\u00e4")
        buf.write("\3\2\2\2\u00f9\u00ed\3\2\2\2\u00f9\u00f1\3\2\2\2\u00f9")
        buf.write("\u00f5\3\2\2\2\u00fa\5\3\2\2\2\u00fb\u0114\5\f\7\2\u00fc")
        buf.write("\u00fd\7\35\2\2\u00fd\u00fe\5\20\t\2\u00fe\u00ff\b\4\1")
        buf.write("\2\u00ff\u0115\3\2\2\2\u0100\u0101\7\36\2\2\u0101\u0102")
        buf.write("\5\20\t\2\u0102\u0103\b\4\1\2\u0103\u0115\3\2\2\2\u0104")
        buf.write("\u0105\7\37\2\2\u0105\u0106\5\20\t\2\u0106\u0107\b\4\1")
        buf.write("\2\u0107\u0115\3\2\2\2\u0108\u0109\7 \2\2\u0109\u010a")
        buf.write("\5\20\t\2\u010a\u010b\b\4\1\2\u010b\u0115\3\2\2\2\u010c")
        buf.write("\u010d\7!\2\2\u010d\u010e\5\20\t\2\u010e\u010f\b\4\1\2")
        buf.write("\u010f\u0115\3\2\2\2\u0110\u0111\7\"\2\2\u0111\u0112\5")
        buf.write("\20\t\2\u0112\u0113\b\4\1\2\u0113\u0115\3\2\2\2\u0114")
        buf.write("\u00fc\3\2\2\2\u0114\u0100\3\2\2\2\u0114\u0104\3\2\2\2")
        buf.write("\u0114\u0108\3\2\2\2\u0114\u010c\3\2\2\2\u0114\u0110\3")
        buf.write("\2\2\2\u0115\7\3\2\2\2\u0116\u0117\5F$\2\u0117\u0118\7")
        buf.write("#\2\2\u0118\u0119\5,\27\2\u0119\u011a\b\5\1\2\u011a\u011f")
        buf.write("\3\2\2\2\u011b\u011c\5\n\6\2\u011c\u011d\b\5\1\2\u011d")
        buf.write("\u011f\3\2\2\2\u011e\u0116\3\2\2\2\u011e\u011b\3\2\2\2")
        buf.write("\u011f\t\3\2\2\2\u0120\u0121\5\f\7\2\u0121\u0128\7#\2")
        buf.write("\2\u0122\u0123\5\n\6\2\u0123\u0124\b\6\1\2\u0124\u0129")
        buf.write("\3\2\2\2\u0125\u0126\5\24\13\2\u0126\u0127\b\6\1\2\u0127")
        buf.write("\u0129\3\2\2\2\u0128\u0122\3\2\2\2\u0128\u0125\3\2\2\2")
        buf.write("\u0129\13\3\2\2\2\u012a\u012b\5\16\b\2\u012b\u0137\b\7")
        buf.write("\1\2\u012c\u012d\7$\2\2\u012d\u012e\5F$\2\u012e\u012f")
        buf.write("\b\7\1\2\u012f\u0136\3\2\2\2\u0130\u0131\7%\2\2\u0131")
        buf.write("\u0132\5\22\n\2\u0132\u0133\7&\2\2\u0133\u0134\b\7\1\2")
        buf.write("\u0134\u0136\3\2\2\2\u0135\u012c\3\2\2\2\u0135\u0130\3")
        buf.write("\2\2\2\u0136\u0139\3\2\2\2\u0137\u0135\3\2\2\2\u0137\u0138")
        buf.write("\3\2\2\2\u0138\u0143\3\2\2\2\u0139\u0137\3\2\2\2\u013a")
        buf.write("\u013b\7%\2\2\u013b\u013c\5J&\2\u013c\u013d\7&\2\2\u013d")
        buf.write("\u013e\b\7\1\2\u013e\u0143\3\2\2\2\u013f\u0140\6\7\2\3")
        buf.write("\u0140\u0141\7\'\2\2\u0141\u0143\b\7\1\2\u0142\u012a\3")
        buf.write("\2\2\2\u0142\u013a\3\2\2\2\u0142\u013f\3\2\2\2\u0143\r")
        buf.write("\3\2\2\2\u0144\u0145\7K\2\2\u0145\u0146\b\b\1\2\u0146")
        buf.write("\17\3\2\2\2\u0147\u0148\5\24\13\2\u0148\u0149\b\t\1\2")
        buf.write("\u0149\21\3\2\2\2\u014a\u014b\5\24\13\2\u014b\u0152\b")
        buf.write("\n\1\2\u014c\u014d\7\34\2\2\u014d\u014e\5\24\13\2\u014e")
        buf.write("\u014f\b\n\1\2\u014f\u0151\3\2\2\2\u0150\u014c\3\2\2\2")
        buf.write("\u0151\u0154\3\2\2\2\u0152\u0150\3\2\2\2\u0152\u0153\3")
        buf.write("\2\2\2\u0153\23\3\2\2\2\u0154\u0152\3\2\2\2\u0155\u0156")
        buf.write("\5\26\f\2\u0156\u0157\b\13\1\2\u0157\u0165\3\2\2\2\u0158")
        buf.write("\u0159\5\32\16\2\u0159\u0162\b\13\1\2\u015a\u015b\7(\2")
        buf.write("\2\u015b\u015c\5\32\16\2\u015c\u015d\b\13\1\2\u015d\u0163")
        buf.write("\3\2\2\2\u015e\u015f\7)\2\2\u015f\u0160\5\32\16\2\u0160")
        buf.write("\u0161\b\13\1\2\u0161\u0163\3\2\2\2\u0162\u015a\3\2\2")
        buf.write("\2\u0162\u015e\3\2\2\2\u0162\u0163\3\2\2\2\u0163\u0165")
        buf.write("\3\2\2\2\u0164\u0155\3\2\2\2\u0164\u0158\3\2\2\2\u0165")
        buf.write("\25\3\2\2\2\u0166\u0167\5\30\r\2\u0167\u0168\7*\2\2\u0168")
        buf.write("\u0169\5\20\t\2\u0169\u016a\b\f\1\2\u016a\27\3\2\2\2\u016b")
        buf.write("\u016c\5F$\2\u016c\u016d\b\r\1\2\u016d\u017e\3\2\2\2\u016e")
        buf.write("\u017a\7%\2\2\u016f\u0170\5F$\2\u0170\u0177\b\r\1\2\u0171")
        buf.write("\u0172\7\34\2\2\u0172\u0173\5F$\2\u0173\u0174\b\r\1\2")
        buf.write("\u0174\u0176\3\2\2\2\u0175\u0171\3\2\2\2\u0176\u0179\3")
        buf.write("\2\2\2\u0177\u0175\3\2\2\2\u0177\u0178\3\2\2\2\u0178\u017b")
        buf.write("\3\2\2\2\u0179\u0177\3\2\2\2\u017a\u016f\3\2\2\2\u017a")
        buf.write("\u017b\3\2\2\2\u017b\u017c\3\2\2\2\u017c\u017e\7&\2\2")
        buf.write("\u017d\u016b\3\2\2\2\u017d\u016e\3\2\2\2\u017e\31\3\2")
        buf.write("\2\2\u017f\u0180\5\34\17\2\u0180\u0185\b\16\1\2\u0181")
        buf.write("\u0182\7+\2\2\u0182\u0183\5\32\16\2\u0183\u0184\b\16\1")
        buf.write("\2\u0184\u0186\3\2\2\2\u0185\u0181\3\2\2\2\u0185\u0186")
        buf.write("\3\2\2\2\u0186\33\3\2\2\2\u0187\u0188\5\36\20\2\u0188")
        buf.write("\u018f\b\17\1\2\u0189\u018a\7,\2\2\u018a\u018b\5\36\20")
        buf.write("\2\u018b\u018c\b\17\1\2\u018c\u018e\3\2\2\2\u018d\u0189")
        buf.write("\3\2\2\2\u018e\u0191\3\2\2\2\u018f\u018d\3\2\2\2\u018f")
        buf.write("\u0190\3\2\2\2\u0190\35\3\2\2\2\u0191\u018f\3\2\2\2\u0192")
        buf.write("\u0193\5 \21\2\u0193\u019a\b\20\1\2\u0194\u0195\7-\2\2")
        buf.write("\u0195\u0196\5 \21\2\u0196\u0197\b\20\1\2\u0197\u0199")
        buf.write("\3\2\2\2\u0198\u0194\3\2\2\2\u0199\u019c\3\2\2\2\u019a")
        buf.write("\u0198\3\2\2\2\u019a\u019b\3\2\2\2\u019b\37\3\2\2\2\u019c")
        buf.write("\u019a\3\2\2\2\u019d\u019e\5\"\22\2\u019e\u01bf\b\21\1")
        buf.write("\2\u019f\u01a0\7.\2\2\u01a0\u01a1\5\"\22\2\u01a1\u01a2")
        buf.write("\b\21\1\2\u01a2\u01c0\3\2\2\2\u01a3\u01a4\7/\2\2\u01a4")
        buf.write("\u01a5\5\"\22\2\u01a5\u01a6\b\21\1\2\u01a6\u01c0\3\2\2")
        buf.write("\2\u01a7\u01a8\7\60\2\2\u01a8\u01a9\5\"\22\2\u01a9\u01aa")
        buf.write("\b\21\1\2\u01aa\u01c0\3\2\2\2\u01ab\u01ac\7\61\2\2\u01ac")
        buf.write("\u01ad\5\"\22\2\u01ad\u01ae\b\21\1\2\u01ae\u01c0\3\2\2")
        buf.write("\2\u01af\u01b0\7\62\2\2\u01b0\u01b1\5\"\22\2\u01b1\u01b2")
        buf.write("\b\21\1\2\u01b2\u01c0\3\2\2\2\u01b3\u01b4\7\63\2\2\u01b4")
        buf.write("\u01b5\5\"\22\2\u01b5\u01b6\b\21\1\2\u01b6\u01c0\3\2\2")
        buf.write("\2\u01b7\u01b8\7\64\2\2\u01b8\u01b9\5\"\22\2\u01b9\u01ba")
        buf.write("\b\21\1\2\u01ba\u01c0\3\2\2\2\u01bb\u01bc\7\65\2\2\u01bc")
        buf.write("\u01bd\5\"\22\2\u01bd\u01be\b\21\1\2\u01be\u01c0\3\2\2")
        buf.write("\2\u01bf\u019f\3\2\2\2\u01bf\u01a3\3\2\2\2\u01bf\u01a7")
        buf.write("\3\2\2\2\u01bf\u01ab\3\2\2\2\u01bf\u01af\3\2\2\2\u01bf")
        buf.write("\u01b3\3\2\2\2\u01bf\u01b7\3\2\2\2\u01bf\u01bb\3\2\2\2")
        buf.write("\u01bf\u01c0\3\2\2\2\u01c0!\3\2\2\2\u01c1\u01c2\5$\23")
        buf.write("\2\u01c2\u01cd\b\22\1\2\u01c3\u01c4\7\66\2\2\u01c4\u01c5")
        buf.write("\5$\23\2\u01c5\u01c6\b\22\1\2\u01c6\u01cc\3\2\2\2\u01c7")
        buf.write("\u01c8\7\67\2\2\u01c8\u01c9\5$\23\2\u01c9\u01ca\b\22\1")
        buf.write("\2\u01ca\u01cc\3\2\2\2\u01cb\u01c3\3\2\2\2\u01cb\u01c7")
        buf.write("\3\2\2\2\u01cc\u01cf\3\2\2\2\u01cd\u01cb\3\2\2\2\u01cd")
        buf.write("\u01ce\3\2\2\2\u01ce#\3\2\2\2\u01cf\u01cd\3\2\2\2\u01d0")
        buf.write("\u01d1\5&\24\2\u01d1\u01e8\b\23\1\2\u01d2\u01d3\78\2\2")
        buf.write("\u01d3\u01d4\5&\24\2\u01d4\u01d5\b\23\1\2\u01d5\u01e7")
        buf.write("\3\2\2\2\u01d6\u01d7\79\2\2\u01d7\u01d8\5&\24\2\u01d8")
        buf.write("\u01d9\b\23\1\2\u01d9\u01e7\3\2\2\2\u01da\u01db\7:\2\2")
        buf.write("\u01db\u01dc\5&\24\2\u01dc\u01dd\b\23\1\2\u01dd\u01e7")
        buf.write("\3\2\2\2\u01de\u01df\7;\2\2\u01df\u01e0\5&\24\2\u01e0")
        buf.write("\u01e1\b\23\1\2\u01e1\u01e7\3\2\2\2\u01e2\u01e3\7<\2\2")
        buf.write("\u01e3\u01e4\5&\24\2\u01e4\u01e5\b\23\1\2\u01e5\u01e7")
        buf.write("\3\2\2\2\u01e6\u01d2\3\2\2\2\u01e6\u01d6\3\2\2\2\u01e6")
        buf.write("\u01da\3\2\2\2\u01e6\u01de\3\2\2\2\u01e6\u01e2\3\2\2\2")
        buf.write("\u01e7\u01ea\3\2\2\2\u01e8\u01e6\3\2\2\2\u01e8\u01e9\3")
        buf.write("\2\2\2\u01e9%\3\2\2\2\u01ea\u01e8\3\2\2\2\u01eb\u01ec")
        buf.write("\5(\25\2\u01ec\u01f7\b\24\1\2\u01ed\u01ee\7=\2\2\u01ee")
        buf.write("\u01ef\5(\25\2\u01ef\u01f0\b\24\1\2\u01f0\u01f6\3\2\2")
        buf.write("\2\u01f1\u01f2\7>\2\2\u01f2\u01f3\5(\25\2\u01f3\u01f4")
        buf.write("\b\24\1\2\u01f4\u01f6\3\2\2\2\u01f5\u01ed\3\2\2\2\u01f5")
        buf.write("\u01f1\3\2\2\2\u01f6\u01f9\3\2\2\2\u01f7\u01f5\3\2\2\2")
        buf.write("\u01f7\u01f8\3\2\2\2\u01f8\'\3\2\2\2\u01f9\u01f7\3\2\2")
        buf.write("\2\u01fa\u01fb\5*\26\2\u01fb\u0200\b\25\1\2\u01fc\u01fd")
        buf.write("\7?\2\2\u01fd\u01fe\5(\25\2\u01fe\u01ff\b\25\1\2\u01ff")
        buf.write("\u0201\3\2\2\2\u0200\u01fc\3\2\2\2\u0200\u0201\3\2\2\2")
        buf.write("\u0201\u0213\3\2\2\2\u0202\u0203\7=\2\2\u0203\u0204\5")
        buf.write("(\25\2\u0204\u0205\b\25\1\2\u0205\u0213\3\2\2\2\u0206")
        buf.write("\u0207\7>\2\2\u0207\u0208\5(\25\2\u0208\u0209\b\25\1\2")
        buf.write("\u0209\u0213\3\2\2\2\u020a\u020b\7@\2\2\u020b\u020c\5")
        buf.write("(\25\2\u020c\u020d\b\25\1\2\u020d\u0213\3\2\2\2\u020e")
        buf.write("\u020f\7\67\2\2\u020f\u0210\5(\25\2\u0210\u0211\b\25\1")
        buf.write("\2\u0211\u0213\3\2\2\2\u0212\u01fa\3\2\2\2\u0212\u0202")
        buf.write("\3\2\2\2\u0212\u0206\3\2\2\2\u0212\u020a\3\2\2\2\u0212")
        buf.write("\u020e\3\2\2\2\u0213)\3\2\2\2\u0214\u0215\7A\2\2\u0215")
        buf.write("\u0216\5*\26\2\u0216\u0217\b\26\1\2\u0217\u024c\3\2\2")
        buf.write("\2\u0218\u0219\7B\2\2\u0219\u021a\7\4\2\2\u021a\u021b")
        buf.write("\5@!\2\u021b\u021c\7\20\2\2\u021c\u021d\5H%\2\u021d\u021e")
        buf.write("\7\5\2\2\u021e\u021f\b\26\1\2\u021f\u024c\3\2\2\2\u0220")
        buf.write("\u0221\7C\2\2\u0221\u0222\7\4\2\2\u0222\u0223\5@!\2\u0223")
        buf.write("\u0224\7\20\2\2\u0224\u0225\5H%\2\u0225\u0226\7\5\2\2")
        buf.write("\u0226\u0227\b\26\1\2\u0227\u024c\3\2\2\2\u0228\u0229")
        buf.write("\7\4\2\2\u0229\u022a\5\24\13\2\u022a\u022b\7\5\2\2\u022b")
        buf.write("\u022c\b\26\1\2\u022c\u0234\3\2\2\2\u022d\u022e\5,\27")
        buf.write("\2\u022e\u022f\b\26\1\2\u022f\u0234\3\2\2\2\u0230\u0231")
        buf.write("\5F$\2\u0231\u0232\b\26\1\2\u0232\u0234\3\2\2\2\u0233")
        buf.write("\u0228\3\2\2\2\u0233\u022d\3\2\2\2\u0233\u0230\3\2\2\2")
        buf.write("\u0234\u023e\3\2\2\2\u0235\u0236\7$\2\2\u0236\u0237\5")
        buf.write("F$\2\u0237\u0238\b\26\1\2\u0238\u023d\3\2\2\2\u0239\u023a")
        buf.write("\5\66\34\2\u023a\u023b\b\26\1\2\u023b\u023d\3\2\2\2\u023c")
        buf.write("\u0235\3\2\2\2\u023c\u0239\3\2\2\2\u023d\u0240\3\2\2\2")
        buf.write("\u023e\u023c\3\2\2\2\u023e\u023f\3\2\2\2\u023f\u0243\3")
        buf.write("\2\2\2\u0240\u023e\3\2\2\2\u0241\u0242\7A\2\2\u0242\u0244")
        buf.write("\b\26\1\2\u0243\u0241\3\2\2\2\u0243\u0244\3\2\2\2\u0244")
        buf.write("\u024c\3\2\2\2\u0245\u0246\5<\37\2\u0246\u0249\b\26\1")
        buf.write("\2\u0247\u0248\7A\2\2\u0248\u024a\b\26\1\2\u0249\u0247")
        buf.write("\3\2\2\2\u0249\u024a\3\2\2\2\u024a\u024c\3\2\2\2\u024b")
        buf.write("\u0214\3\2\2\2\u024b\u0218\3\2\2\2\u024b\u0220\3\2\2\2")
        buf.write("\u024b\u0233\3\2\2\2\u024b\u0245\3\2\2\2\u024c+\3\2\2")
        buf.write("\2\u024d\u024e\7D\2\2\u024e\u024f\7\4\2\2\u024f\u0250")
        buf.write("\5.\30\2\u0250\u0251\7\5\2\2\u0251\u0252\7\6\2\2\u0252")
        buf.write("\u0253\5\2\2\2\u0253\u0254\7\b\2\2\u0254\u0255\b\27\1")
        buf.write("\2\u0255\u0269\3\2\2\2\u0256\u0257\7E\2\2\u0257\u0258")
        buf.write("\7\4\2\2\u0258\u0259\5.\30\2\u0259\u025a\7\5\2\2\u025a")
        buf.write("\u025b\7\6\2\2\u025b\u025c\5\2\2\2\u025c\u025d\7\b\2\2")
        buf.write("\u025d\u025e\b\27\1\2\u025e\u0269\3\2\2\2\u025f\u0260")
        buf.write("\7F\2\2\u0260\u0261\7\4\2\2\u0261\u0262\5.\30\2\u0262")
        buf.write("\u0263\7\5\2\2\u0263\u0264\7\6\2\2\u0264\u0265\5\2\2\2")
        buf.write("\u0265\u0266\7\b\2\2\u0266\u0267\b\27\1\2\u0267\u0269")
        buf.write("\3\2\2\2\u0268\u024d\3\2\2\2\u0268\u0256\3\2\2\2\u0268")
        buf.write("\u025f\3\2\2\2\u0269-\3\2\2\2\u026a\u026b\5\60\31\2\u026b")
        buf.write("\u0272\b\30\1\2\u026c\u026d\7\34\2\2\u026d\u026e\5\60")
        buf.write("\31\2\u026e\u026f\b\30\1\2\u026f\u0271\3\2\2\2\u0270\u026c")
        buf.write("\3\2\2\2\u0271\u0274\3\2\2\2\u0272\u0270\3\2\2\2\u0272")
        buf.write("\u0273\3\2\2\2\u0273\u027b\3\2\2\2\u0274\u0272\3\2\2\2")
        buf.write("\u0275\u0276\7\34\2\2\u0276\u0277\5\62\32\2\u0277\u0278")
        buf.write("\b\30\1\2\u0278\u027a\3\2\2\2\u0279\u0275\3\2\2\2\u027a")
        buf.write("\u027d\3\2\2\2\u027b\u0279\3\2\2\2\u027b\u027c\3\2\2\2")
        buf.write("\u027c\u0282\3\2\2\2\u027d\u027b\3\2\2\2\u027e\u027f\7")
        buf.write("\34\2\2\u027f\u0280\5\64\33\2\u0280\u0281\b\30\1\2\u0281")
        buf.write("\u0283\3\2\2\2\u0282\u027e\3\2\2\2\u0282\u0283\3\2\2\2")
        buf.write("\u0283\u029a\3\2\2\2\u0284\u0285\5\62\32\2\u0285\u028c")
        buf.write("\b\30\1\2\u0286\u0287\7\34\2\2\u0287\u0288\5\62\32\2\u0288")
        buf.write("\u0289\b\30\1\2\u0289\u028b\3\2\2\2\u028a\u0286\3\2\2")
        buf.write("\2\u028b\u028e\3\2\2\2\u028c\u028a\3\2\2\2\u028c\u028d")
        buf.write("\3\2\2\2\u028d\u0293\3\2\2\2\u028e\u028c\3\2\2\2\u028f")
        buf.write("\u0290\7\34\2\2\u0290\u0291\5\64\33\2\u0291\u0292\b\30")
        buf.write("\1\2\u0292\u0294\3\2\2\2\u0293\u028f\3\2\2\2\u0293\u0294")
        buf.write("\3\2\2\2\u0294\u029a\3\2\2\2\u0295\u0296\5\64\33\2\u0296")
        buf.write("\u0297\b\30\1\2\u0297\u029a\3\2\2\2\u0298\u029a\3\2\2")
        buf.write("\2\u0299\u026a\3\2\2\2\u0299\u0284\3\2\2\2\u0299\u0295")
        buf.write("\3\2\2\2\u0299\u0298\3\2\2\2\u029a/\3\2\2\2\u029b\u029c")
        buf.write("\6\31\3\3\u029c\u029d\7G\2\2\u029d\u029e\5\16\b\2\u029e")
        buf.write("\u029f\b\31\1\2\u029f\u02a4\3\2\2\2\u02a0\u02a1\5F$\2")
        buf.write("\u02a1\u02a2\b\31\1\2\u02a2\u02a4\3\2\2\2\u02a3\u029b")
        buf.write("\3\2\2\2\u02a3\u02a0\3\2\2\2\u02a4\61\3\2\2\2\u02a5\u02a6")
        buf.write("\5\16\b\2\u02a6\u02a7\7#\2\2\u02a7\u02a8\5\20\t\2\u02a8")
        buf.write("\u02a9\b\32\1\2\u02a9\63\3\2\2\2\u02aa\u02ab\78\2\2\u02ab")
        buf.write("\u02ac\5F$\2\u02ac\u02ad\b\33\1\2\u02ad\65\3\2\2\2\u02ae")
        buf.write("\u02af\7\4\2\2\u02af\u02b0\5:\36\2\u02b0\u02b1\7\5\2\2")
        buf.write("\u02b1\u02b2\b\34\1\2\u02b2\u02be\3\2\2\2\u02b3\u02b4")
        buf.write("\7%\2\2\u02b4\u02b5\58\35\2\u02b5\u02b6\7&\2\2\u02b6\u02b7")
        buf.write("\b\34\1\2\u02b7\u02be\3\2\2\2\u02b8\u02b9\7\6\2\2\u02b9")
        buf.write("\u02ba\5\20\t\2\u02ba\u02bb\7\b\2\2\u02bb\u02bc\b\34\1")
        buf.write("\2\u02bc\u02be\3\2\2\2\u02bd\u02ae\3\2\2\2\u02bd\u02b3")
        buf.write("\3\2\2\2\u02bd\u02b8\3\2\2\2\u02be\67\3\2\2\2\u02bf\u02d2")
        buf.write("\5\20\t\2\u02c0\u02c5\7N\2\2\u02c1\u02c2\5\20\t\2\u02c2")
        buf.write("\u02c3\b\35\1\2\u02c3\u02c6\3\2\2\2\u02c4\u02c6\b\35\1")
        buf.write("\2\u02c5\u02c1\3\2\2\2\u02c5\u02c4\3\2\2\2\u02c6\u02d3")
        buf.write("\3\2\2\2\u02c7\u02c8\7\34\2\2\u02c8\u02c9\5\20\t\2\u02c9")
        buf.write("\u02ca\b\35\1\2\u02ca\u02cc\3\2\2\2\u02cb\u02c7\3\2\2")
        buf.write("\2\u02cc\u02cd\3\2\2\2\u02cd\u02cb\3\2\2\2\u02cd\u02ce")
        buf.write("\3\2\2\2\u02ce\u02cf\3\2\2\2\u02cf\u02d0\b\35\1\2\u02d0")
        buf.write("\u02d3\3\2\2\2\u02d1\u02d3\b\35\1\2\u02d2\u02c0\3\2\2")
        buf.write("\2\u02d2\u02cb\3\2\2\2\u02d2\u02d1\3\2\2\2\u02d3\u02d9")
        buf.write("\3\2\2\2\u02d4\u02d5\7N\2\2\u02d5\u02d6\5\20\t\2\u02d6")
        buf.write("\u02d7\b\35\1\2\u02d7\u02d9\3\2\2\2\u02d8\u02bf\3\2\2")
        buf.write("\2\u02d8\u02d4\3\2\2\2\u02d99\3\2\2\2\u02da\u02db\5\22")
        buf.write("\n\2\u02db\u02e1\b\36\1\2\u02dc\u02dd\7\34\2\2\u02dd\u02de")
        buf.write("\78\2\2\u02de\u02df\5\24\13\2\u02df\u02e0\b\36\1\2\u02e0")
        buf.write("\u02e2\3\2\2\2\u02e1\u02dc\3\2\2\2\u02e1\u02e2\3\2\2\2")
        buf.write("\u02e2\u02e9\3\2\2\2\u02e3\u02e4\78\2\2\u02e4\u02e5\5")
        buf.write("\24\13\2\u02e5\u02e6\b\36\1\2\u02e6\u02e9\3\2\2\2\u02e7")
        buf.write("\u02e9\3\2\2\2\u02e8\u02da\3\2\2\2\u02e8\u02e3\3\2\2\2")
        buf.write("\u02e8\u02e7\3\2\2\2\u02e9;\3\2\2\2\u02ea\u02ee\7%\2\2")
        buf.write("\u02eb\u02ec\5> \2\u02ec\u02ed\b\37\1\2\u02ed\u02ef\3")
        buf.write("\2\2\2\u02ee\u02eb\3\2\2\2\u02ee\u02ef\3\2\2\2\u02ef\u02f0")
        buf.write("\3\2\2\2\u02f0\u02f1\7&\2\2\u02f1\u0305\b\37\1\2\u02f2")
        buf.write("\u02f6\7\6\2\2\u02f3\u02f4\5> \2\u02f4\u02f5\b\37\1\2")
        buf.write("\u02f5\u02f7\3\2\2\2\u02f6\u02f3\3\2\2\2\u02f6\u02f7\3")
        buf.write("\2\2\2\u02f7\u02f8\3\2\2\2\u02f8\u02f9\7\b\2\2\u02f9\u0305")
        buf.write("\b\37\1\2\u02fa\u02fb\7O\2\2\u02fb\u0305\b\37\1\2\u02fc")
        buf.write("\u02fd\7P\2\2\u02fd\u0305\b\37\1\2\u02fe\u02ff\5D#\2\u02ff")
        buf.write("\u0300\b\37\1\2\u0300\u0305\3\2\2\2\u0301\u0302\6\37\4")
        buf.write("\3\u0302\u0303\7\'\2\2\u0303\u0305\b\37\1\2\u0304\u02ea")
        buf.write("\3\2\2\2\u0304\u02f2\3\2\2\2\u0304\u02fa\3\2\2\2\u0304")
        buf.write("\u02fc\3\2\2\2\u0304\u02fe\3\2\2\2\u0304\u0301\3\2\2\2")
        buf.write("\u0305=\3\2\2\2\u0306\u0335\5\20\t\2\u0307\u0308\7\34")
        buf.write("\2\2\u0308\u031e\5\20\t\2\u0309\u030a\7N\2\2\u030a\u030b")
        buf.write("\5\20\t\2\u030b\u030c\b \1\2\u030c\u031f\3\2\2\2\u030d")
        buf.write("\u0314\b \1\2\u030e\u030f\7\34\2\2\u030f\u0310\5\20\t")
        buf.write("\2\u0310\u0311\b \1\2\u0311\u0313\3\2\2\2\u0312\u030e")
        buf.write("\3\2\2\2\u0313\u0316\3\2\2\2\u0314\u0312\3\2\2\2\u0314")
        buf.write("\u0315\3\2\2\2\u0315\u031c\3\2\2\2\u0316\u0314\3\2\2\2")
        buf.write("\u0317\u0318\7\20\2\2\u0318\u0319\5\20\t\2\u0319\u031a")
        buf.write("\b \1\2\u031a\u031d\3\2\2\2\u031b\u031d\b \1\2\u031c\u0317")
        buf.write("\3\2\2\2\u031c\u031b\3\2\2\2\u031d\u031f\3\2\2\2\u031e")
        buf.write("\u0309\3\2\2\2\u031e\u030d\3\2\2\2\u031f\u0336\3\2\2\2")
        buf.write("\u0320\u0321\7N\2\2\u0321\u0322\5\20\t\2\u0322\u0323\b")
        buf.write(" \1\2\u0323\u0336\3\2\2\2\u0324\u032a\b \1\2\u0325\u0326")
        buf.write("\7\20\2\2\u0326\u0327\5\20\t\2\u0327\u0328\b \1\2\u0328")
        buf.write("\u032b\3\2\2\2\u0329\u032b\b \1\2\u032a\u0325\3\2\2\2")
        buf.write("\u032a\u0329\3\2\2\2\u032b\u0336\3\2\2\2\u032c\u032d\7")
        buf.write("\r\2\2\u032d\u0333\5@!\2\u032e\u032f\7\20\2\2\u032f\u0330")
        buf.write("\5H%\2\u0330\u0331\b \1\2\u0331\u0334\3\2\2\2\u0332\u0334")
        buf.write("\b \1\2\u0333\u032e\3\2\2\2\u0333\u0332\3\2\2\2\u0334")
        buf.write("\u0336\3\2\2\2\u0335\u0307\3\2\2\2\u0335\u0320\3\2\2\2")
        buf.write("\u0335\u0324\3\2\2\2\u0335\u032c\3\2\2\2\u0336?\3\2\2")
        buf.write("\2\u0337\u0338\5B\"\2\u0338\u033f\b!\1\2\u0339\u033a\7")
        buf.write("\34\2\2\u033a\u033b\5B\"\2\u033b\u033c\b!\1\2\u033c\u033e")
        buf.write("\3\2\2\2\u033d\u0339\3\2\2\2\u033e\u0341\3\2\2\2\u033f")
        buf.write("\u033d\3\2\2\2\u033f\u0340\3\2\2\2\u0340A\3\2\2\2\u0341")
        buf.write("\u033f\3\2\2\2\u0342\u0343\5\f\7\2\u0343\u0344\7\64\2")
        buf.write("\2\u0344\u0345\5\20\t\2\u0345\u0346\b\"\1\2\u0346C\3\2")
        buf.write("\2\2\u0347\u0348\7L\2\2\u0348\u0352\b#\1\2\u0349\u034a")
        buf.write("\7M\2\2\u034a\u0352\b#\1\2\u034b\u034c\7H\2\2\u034c\u0352")
        buf.write("\b#\1\2\u034d\u034e\7I\2\2\u034e\u0352\b#\1\2\u034f\u0350")
        buf.write("\7J\2\2\u0350\u0352\b#\1\2\u0351\u0347\3\2\2\2\u0351\u0349")
        buf.write("\3\2\2\2\u0351\u034b\3\2\2\2\u0351\u034d\3\2\2\2\u0351")
        buf.write("\u034f\3\2\2\2\u0352E\3\2\2\2\u0353\u0354\7K\2\2\u0354")
        buf.write("\u0355\b$\1\2\u0355G\3\2\2\2\u0356\u0357\5\20\t\2\u0357")
        buf.write("\u0358\b%\1\2\u0358I\3\2\2\2\u0359\u035a\5\f\7\2\u035a")
        buf.write("\u0361\b&\1\2\u035b\u035c\7\34\2\2\u035c\u035d\5\f\7\2")
        buf.write("\u035d\u035e\b&\1\2\u035e\u0360\3\2\2\2\u035f\u035b\3")
        buf.write("\2\2\2\u0360\u0363\3\2\2\2\u0361\u035f\3\2\2\2\u0361\u0362")
        buf.write("\3\2\2\2\u0362K\3\2\2\2\u0363\u0361\3\2\2\2EQc{\u0084")
        buf.write("\u0092\u0098\u00a3\u00cc\u00e0\u00f9\u0114\u011e\u0128")
        buf.write("\u0135\u0137\u0142\u0152\u0162\u0164\u0177\u017a\u017d")
        buf.write("\u0185\u018f\u019a\u01bf\u01cb\u01cd\u01e6\u01e8\u01f5")
        buf.write("\u01f7\u0200\u0212\u0233\u023c\u023e\u0243\u0249\u024b")
        buf.write("\u0268\u0272\u027b\u0282\u028c\u0293\u0299\u02a3\u02bd")
        buf.write("\u02c5\u02cd\u02d2\u02d8\u02e1\u02e8\u02ee\u02f6\u0304")
        buf.write("\u0314\u031c\u031e\u032a\u0333\u0335\u033f\u0351\u0361")
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
    RULE_assignment = 3
    RULE_assignmentDirect = 4
    RULE_assignable = 5
    RULE_assignableVariable = 6
    RULE_expr = 7
    RULE_exprList = 8
    RULE_exprContent = 9
    RULE_lambdaProcedure = 10
    RULE_lambdaParameters = 11
    RULE_implication = 12
    RULE_disjunction = 13
    RULE_conjunction = 14
    RULE_comparison = 15
    RULE_setlxSum = 16
    RULE_product = 17
    RULE_setlxReduce = 18
    RULE_prefixOperation = 19
    RULE_factor = 20
    RULE_procedure = 21
    RULE_procedureParameters = 22
    RULE_procedureParameter = 23
    RULE_procedureDefaultParameter = 24
    RULE_procedureListParameter = 25
    RULE_call = 26
    RULE_collectionAccessParams = 27
    RULE_callParameters = 28
    RULE_value = 29
    RULE_collectionBuilder = 30
    RULE_iteratorChain = 31
    RULE_iterator = 32
    RULE_atomicValue = 33
    RULE_variable = 34
    RULE_condition = 35
    RULE_assignmentList = 36

    ruleNames =  [ "block", "statement", "assignmentOther", "assignment", 
                   "assignmentDirect", "assignable", "assignableVariable", 
                   "expr", "exprList", "exprContent", "lambdaProcedure", 
                   "lambdaParameters", "implication", "disjunction", "conjunction", 
                   "comparison", "setlxSum", "product", "setlxReduce", "prefixOperation", 
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
            self.state = 79
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,0,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 74
                    localctx._statement = self.statement()
                    stmnts.append(localctx._statement.stmnt) 
                self.state = 81
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
            self._assignment = None # AssignmentContext

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


        def assignment(self):
            return self.getTypedRuleContext(SetlXgrammarParser.AssignmentContext,0)


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
            self.state = 247
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,9,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 84
                self.match(SetlXgrammarParser.T__0)
                self.state = 85
                localctx._ID = self.match(SetlXgrammarParser.ID)
                self.state = 86
                self.match(SetlXgrammarParser.T__1)
                self.state = 87
                localctx._procedureParameters = self.procedureParameters(True)
                self.state = 88
                self.match(SetlXgrammarParser.T__2)
                self.state = 89
                self.match(SetlXgrammarParser.T__3)
                self.state = 90
                localctx.b1 = self.block()
                self.state = 97
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==SetlXgrammarParser.T__4:
                    self.state = 91
                    self.match(SetlXgrammarParser.T__4)
                    self.state = 92
                    self.match(SetlXgrammarParser.T__3)
                    self.state = 93
                    localctx.b2 = self.block()
                    self.state = 94
                    self.match(SetlXgrammarParser.T__5)
                    static = localctx.b2.blk


                self.state = 99
                self.match(SetlXgrammarParser.T__5)
                localctx.stmnt = ClassConstructor((None if localctx._ID is None else localctx._ID.text), localctx._procedureParameters.paramList, localctx.b1.blk, static)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 102
                self.match(SetlXgrammarParser.T__6)
                self.state = 103
                self.match(SetlXgrammarParser.T__1)
                self.state = 104
                localctx.c1 = self.condition()
                self.state = 105
                self.match(SetlXgrammarParser.T__2)
                self.state = 106
                self.match(SetlXgrammarParser.T__3)
                self.state = 107
                localctx.b1 = self.block()
                self.state = 108
                self.match(SetlXgrammarParser.T__5)
                self.state = 121
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,2,self._ctx)
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1:
                        self.state = 109
                        self.match(SetlXgrammarParser.T__7)
                        self.state = 110
                        self.match(SetlXgrammarParser.T__6)
                        self.state = 111
                        self.match(SetlXgrammarParser.T__1)
                        self.state = 112
                        localctx.c2 = self.condition()
                        self.state = 113
                        self.match(SetlXgrammarParser.T__2)
                        self.state = 114
                        self.match(SetlXgrammarParser.T__3)
                        self.state = 115
                        localctx.b2 = self.block()
                        self.state = 116
                        self.match(SetlXgrammarParser.T__5)
                        else_list.append(IfThenBranch(localctx.c2.cnd,localctx.b2.blk,[])) 
                        			 
                    self.state = 123
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,2,self._ctx)

                self.state = 130
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
                if la_ == 1:
                    self.state = 124
                    self.match(SetlXgrammarParser.T__7)
                    self.state = 125
                    self.match(SetlXgrammarParser.T__3)
                    self.state = 126
                    localctx.b3 = self.block()
                    self.state = 127
                    self.match(SetlXgrammarParser.T__5)
                    else_list.append(localctx.b3.blk) 


                localctx.stmnt = IfThen(localctx.c1.cnd,localctx.b1.blk,else_list) 
                		
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 134
                self.match(SetlXgrammarParser.T__8)
                self.state = 135
                self.match(SetlXgrammarParser.T__3)
                self.state = 144
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==SetlXgrammarParser.T__9:
                    self.state = 136
                    self.match(SetlXgrammarParser.T__9)
                    self.state = 137
                    localctx.c1 = self.condition()
                    self.state = 138
                    self.match(SetlXgrammarParser.T__10)
                    self.state = 139
                    localctx.b1 = self.block()
                    caseList.append((localctx.c1.cnd, localctx.b1.blk)) 
                    self.state = 146
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 150
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==SetlXgrammarParser.T__11:
                    self.state = 147
                    self.match(SetlXgrammarParser.T__11)
                    self.state = 148
                    self.match(SetlXgrammarParser.T__10)
                    self.state = 149
                    localctx.b2 = self.block()


                self.state = 152
                self.match(SetlXgrammarParser.T__5)
                localctx.stmnt = Switch(caseList,localctx.b2.blk) 
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 154
                self.match(SetlXgrammarParser.T__12)
                self.state = 155
                self.match(SetlXgrammarParser.T__1)
                self.state = 156
                localctx._iteratorChain = self.iteratorChain(False)
                self.state = 161
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==SetlXgrammarParser.T__13:
                    self.state = 157
                    self.match(SetlXgrammarParser.T__13)
                    self.state = 158
                    localctx._condition = self.condition()
                    condition = localctx._condition.cnd


                self.state = 163
                self.match(SetlXgrammarParser.T__2)
                self.state = 164
                self.match(SetlXgrammarParser.T__3)
                self.state = 165
                localctx._block = self.block()
                self.state = 166
                self.match(SetlXgrammarParser.T__5)
                localctx.stmnt = SetlXFor(localctx._iteratorChain.ic, condition, localctx._block.blk) 
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 169
                self.match(SetlXgrammarParser.T__14)
                self.state = 170
                self.match(SetlXgrammarParser.T__1)
                self.state = 171
                localctx._condition = self.condition()
                self.state = 172
                self.match(SetlXgrammarParser.T__2)
                self.state = 173
                self.match(SetlXgrammarParser.T__3)
                self.state = 174
                localctx._block = self.block()
                self.state = 175
                self.match(SetlXgrammarParser.T__5)
                localctx.stmnt = SetlXWhile(localctx._condition.cnd, localctx._block.blk) 
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 178
                self.match(SetlXgrammarParser.T__15)
                self.state = 179
                self.match(SetlXgrammarParser.T__3)
                self.state = 180
                localctx._block = self.block()
                self.state = 181
                self.match(SetlXgrammarParser.T__5)
                self.state = 182
                self.match(SetlXgrammarParser.T__14)
                self.state = 183
                self.match(SetlXgrammarParser.T__1)
                self.state = 184
                localctx._condition = self.condition()
                self.state = 185
                self.match(SetlXgrammarParser.T__2)
                self.state = 186
                self.match(SetlXgrammarParser.T__16)
                localctx.stmnt = DoWhile(localctx._condition.cnd, localctx._block.blk) 
                		
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 189
                self.match(SetlXgrammarParser.T__17)
                self.state = 190
                self.match(SetlXgrammarParser.T__3)
                self.state = 191
                localctx.b1 = self.block()
                self.state = 192
                self.match(SetlXgrammarParser.T__5)
                self.state = 202
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,7,self._ctx)
                if la_ == 1:
                    self.state = 193
                    self.match(SetlXgrammarParser.T__18)
                    self.state = 194
                    self.match(SetlXgrammarParser.T__1)
                    self.state = 195
                    localctx.v2 = self.assignableVariable()
                    self.state = 196
                    self.match(SetlXgrammarParser.T__2)
                    self.state = 197
                    self.match(SetlXgrammarParser.T__3)
                    self.state = 198
                    localctx.b3 = self.block()
                    self.state = 199
                    self.match(SetlXgrammarParser.T__5)
                    tryList.append(TryCatchBranch(localctx.v2.v, localctx.b3.blk))         
                    			


                localctx.stmnt = TryCatch(localctx.b1.blk, tryList) 
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 206
                self.match(SetlXgrammarParser.T__19)
                self.state = 207
                self.match(SetlXgrammarParser.T__16)
                localctx.stmnt = Backtrack() 
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 209
                self.match(SetlXgrammarParser.T__20)
                self.state = 210
                self.match(SetlXgrammarParser.T__16)
                localctx.stmnt = SetlXBreak() 
                pass

            elif la_ == 10:
                self.enterOuterAlt(localctx, 10)
                self.state = 212
                self.match(SetlXgrammarParser.T__21)
                self.state = 213
                self.match(SetlXgrammarParser.T__16)
                localctx.stmnt = SetlXContinue() 
                pass

            elif la_ == 11:
                self.enterOuterAlt(localctx, 11)
                self.state = 215
                self.match(SetlXgrammarParser.T__22)
                self.state = 216
                self.match(SetlXgrammarParser.T__16)
                localctx.stmnt = Exit() 
                pass

            elif la_ == 12:
                self.enterOuterAlt(localctx, 12)
                self.state = 218
                self.match(SetlXgrammarParser.T__23)
                self.state = 222
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,8,self._ctx)
                if la_ == 1:
                    self.state = 219
                    localctx._expr = self.expr(False)
                    expression = localctx._expr.ex 


                self.state = 224
                self.match(SetlXgrammarParser.T__16)
                localctx.stmnt = SetlXReturn(expression) 
                pass

            elif la_ == 13:
                self.enterOuterAlt(localctx, 13)
                self.state = 226
                self.match(SetlXgrammarParser.T__24)
                self.state = 227
                self.match(SetlXgrammarParser.T__1)
                self.state = 228
                localctx._condition = self.condition()
                self.state = 229
                self.match(SetlXgrammarParser.T__25)
                self.state = 230
                localctx._expr = self.expr(False)
                self.state = 231
                self.match(SetlXgrammarParser.T__2)
                self.state = 232
                self.match(SetlXgrammarParser.T__16)
                localctx.stmnt = SetlXAssert(localctx._condition.cnd, localctx._expr.ex)
                pass

            elif la_ == 14:
                self.enterOuterAlt(localctx, 14)
                self.state = 235
                localctx._assignmentOther = self.assignmentOther()
                self.state = 236
                self.match(SetlXgrammarParser.T__16)
                localctx.stmnt = localctx._assignmentOther.assign 
                pass

            elif la_ == 15:
                self.enterOuterAlt(localctx, 15)
                self.state = 239
                localctx._assignment = self.assignment()
                self.state = 240
                self.match(SetlXgrammarParser.T__16)
                localctx.stmnt = localctx._assignment.assign 
                pass

            elif la_ == 16:
                self.enterOuterAlt(localctx, 16)
                self.state = 243
                localctx._expr = self.expr(False)
                self.state = 244
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
            self.state = 249
            localctx._assignable = self.assignable(False)
            self.state = 274
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [SetlXgrammarParser.T__26]:
                self.state = 250
                self.match(SetlXgrammarParser.T__26)
                self.state = 251
                localctx.e = self.expr(False)
                localctx.assign = SumAssignment(localctx._assignable.a, localctx.e.ex) 
                pass
            elif token in [SetlXgrammarParser.T__27]:
                self.state = 254
                self.match(SetlXgrammarParser.T__27)
                self.state = 255
                localctx.e = self.expr(False)
                localctx.assign = DifferenceAssignment(localctx._assignable.a, localctx.e.ex) 
                pass
            elif token in [SetlXgrammarParser.T__28]:
                self.state = 258
                self.match(SetlXgrammarParser.T__28)
                self.state = 259
                localctx.e = self.expr(False)
                localctx.assign = ProductAssignment(localctx._assignable.a, localctx.e.ex) 
                pass
            elif token in [SetlXgrammarParser.T__29]:
                self.state = 262
                self.match(SetlXgrammarParser.T__29)
                self.state = 263
                localctx.e = self.expr(False)
                localctx.assign = QuotientAssignment(localctx._assignable.a, localctx.e.ex) 
                pass
            elif token in [SetlXgrammarParser.T__30]:
                self.state = 266
                self.match(SetlXgrammarParser.T__30)
                self.state = 267
                localctx.e = self.expr(False)
                localctx.assign = IntegerDivisionAssignment(localctx._assignable.a, localctx.e.ex) 
                pass
            elif token in [SetlXgrammarParser.T__31]:
                self.state = 270
                self.match(SetlXgrammarParser.T__31)
                self.state = 271
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

    class AssignmentContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.assign = None
            self._variable = None # VariableContext
            self._procedure = None # ProcedureContext
            self._assignmentDirect = None # AssignmentDirectContext

        def variable(self):
            return self.getTypedRuleContext(SetlXgrammarParser.VariableContext,0)


        def procedure(self):
            return self.getTypedRuleContext(SetlXgrammarParser.ProcedureContext,0)


        def assignmentDirect(self):
            return self.getTypedRuleContext(SetlXgrammarParser.AssignmentDirectContext,0)


        def getRuleIndex(self):
            return SetlXgrammarParser.RULE_assignment

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAssignment" ):
                listener.enterAssignment(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAssignment" ):
                listener.exitAssignment(self)




    def assignment(self):

        localctx = SetlXgrammarParser.AssignmentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_assignment)
        try:
            self.state = 284
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,11,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 276
                localctx._variable = self.variable()
                self.state = 277
                self.match(SetlXgrammarParser.T__32)
                self.state = 278
                localctx._procedure = self.procedure(localctx._variable.v.id)
                localctx.assign = localctx._procedure.pd 
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 281
                localctx._assignmentDirect = self.assignmentDirect()
                localctx.assign = localctx._assignmentDirect.assign 
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
        self.enterRule(localctx, 8, self.RULE_assignmentDirect)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 286
            localctx._assignable = self.assignable(False)
            self.state = 287
            self.match(SetlXgrammarParser.T__32)
            self.state = 294
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,12,self._ctx)
            if la_ == 1:
                self.state = 288
                localctx._assignmentDirect = self.assignmentDirect()
                localctx.assign = Assignment([localctx._assignable.a]+localctx._assignmentDirect.assign.assignables, localctx._assignmentDirect.assign.right_hand_side) 
                pass

            elif la_ == 2:
                self.state = 291
                localctx._exprContent = self.exprContent(False)
                localctx.assign = Assignment([localctx._assignable.a], localctx._exprContent.ex) 
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
        self.enterRule(localctx, 10, self.RULE_assignable)
        self._la = 0 # Token type
        try:
            self.state = 320
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,15,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 296
                localctx._assignableVariable = self.assignableVariable()
                localctx.a = localctx._assignableVariable.v
                self.state = 309
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==SetlXgrammarParser.T__33 or _la==SetlXgrammarParser.T__34:
                    self.state = 307
                    self._errHandler.sync(self)
                    token = self._input.LA(1)
                    if token in [SetlXgrammarParser.T__33]:
                        self.state = 298
                        self.match(SetlXgrammarParser.T__33)
                        self.state = 299
                        localctx._variable = self.variable()
                        localctx.a = AssignableMember(localctx.a, localctx._variable.v)
                        pass
                    elif token in [SetlXgrammarParser.T__34]:
                        self.state = 302
                        self.match(SetlXgrammarParser.T__34)
                        self.state = 303
                        localctx._exprList = self.exprList(False)
                        self.state = 304
                        self.match(SetlXgrammarParser.T__35)
                        localctx.a = AssignableCollectionAccess(localctx.a, localctx._exprList.exprs)
                        pass
                    else:
                        raise NoViableAltException(self)

                    self.state = 311
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 312
                self.match(SetlXgrammarParser.T__34)
                self.state = 313
                localctx._assignmentList = self.assignmentList()
                self.state = 314
                self.match(SetlXgrammarParser.T__35)
                localctx.a = AssignableList(localctx._assignmentList.al)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 317
                if not localctx.enableIgnore:
                    from antlr4.error.Errors import FailedPredicateException
                    raise FailedPredicateException(self, "$enableIgnore")
                self.state = 318
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
        self.enterRule(localctx, 12, self.RULE_assignableVariable)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 322
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
        self.enterRule(localctx, 14, self.RULE_expr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 325
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
        self.enterRule(localctx, 16, self.RULE_exprList)

        localctx.exprs = []
            
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 328
            localctx._exprContent = self.exprContent(localctx.enableIgnore)
            localctx.exprs.append(localctx._exprContent.ex)
            self.state = 336
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,16,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 330
                    self.match(SetlXgrammarParser.T__25)
                    self.state = 331
                    localctx._exprContent = self.exprContent(localctx.enableIgnore)
                    localctx.exprs.append(localctx._exprContent.ex) 
                self.state = 338
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
        self.enterRule(localctx, 18, self.RULE_exprContent)
        try:
            self.state = 354
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,18,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 339
                localctx._lambdaProcedure = self.lambdaProcedure()
                localctx.ex = localctx._lambdaProcedure.lp 
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 342
                localctx._implication = self.implication(localctx.enableIgnore)
                localctx.ex = localctx._implication.i
                self.state = 352
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [SetlXgrammarParser.T__37]:
                    self.state = 344
                    self.match(SetlXgrammarParser.T__37)
                    self.state = 345
                    localctx._implication = self.implication(localctx.enableIgnore)
                    localctx.ex = BooleanEqual(localctx.ex,localctx._implication.i) 
                    pass
                elif token in [SetlXgrammarParser.T__38]:
                    self.state = 348
                    self.match(SetlXgrammarParser.T__38)
                    self.state = 349
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
        self.enterRule(localctx, 20, self.RULE_lambdaProcedure)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 356
            localctx._lambdaParameters = self.lambdaParameters()

            self.state = 357
            self.match(SetlXgrammarParser.T__39)
            self.state = 358
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
        self.enterRule(localctx, 22, self.RULE_lambdaParameters)

        localctx.paramList = []
            
        self._la = 0 # Token type
        try:
            self.state = 379
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [SetlXgrammarParser.ID]:
                self.enterOuterAlt(localctx, 1)
                self.state = 361
                localctx._variable = self.variable()
                localctx.paramList.append(Parameter(localctx._variable.v.id, None, False)) 
                pass
            elif token in [SetlXgrammarParser.T__34]:
                self.enterOuterAlt(localctx, 2)
                self.state = 364
                self.match(SetlXgrammarParser.T__34)
                self.state = 376
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==SetlXgrammarParser.ID:
                    self.state = 365
                    localctx.v1 = self.variable()
                    localctx.paramList.append(Parameter(localctx.v1.v.id, None, False))
                    self.state = 373
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    while _la==SetlXgrammarParser.T__25:
                        self.state = 367
                        self.match(SetlXgrammarParser.T__25)
                        self.state = 368
                        localctx.v2 = self.variable()
                        localctx.paramList.append(Parameter(localctx.v2.v.id, None, False))
                        self.state = 375
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)



                self.state = 378
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
        self.enterRule(localctx, 24, self.RULE_implication)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 381
            localctx._disjunction = self.disjunction(localctx.enableIgnore)
            localctx.i = localctx._disjunction.d
            self.state = 387
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==SetlXgrammarParser.T__40:
                self.state = 383
                self.match(SetlXgrammarParser.T__40)
                self.state = 384
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
        self.enterRule(localctx, 26, self.RULE_disjunction)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 389
            localctx._conjunction = self.conjunction(localctx.enableIgnore)
            localctx.d = localctx._conjunction.c
            self.state = 397
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==SetlXgrammarParser.T__41:
                self.state = 391
                self.match(SetlXgrammarParser.T__41)
                self.state = 392
                localctx._conjunction = self.conjunction(localctx.enableIgnore)
                localctx.d = Disjunction(localctx.d, localctx._conjunction.c) 
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
        self.enterRule(localctx, 28, self.RULE_conjunction)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 400
            localctx._comparison = self.comparison(localctx.enableIgnore)
            localctx.c = localctx._comparison.c
            self.state = 408
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==SetlXgrammarParser.T__42:
                self.state = 402
                self.match(SetlXgrammarParser.T__42)
                self.state = 403
                localctx._comparison = self.comparison(localctx.enableIgnore)
                localctx.c = Conjunction(localctx.c, localctx._comparison.c) 
                self.state = 410
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
        self.enterRule(localctx, 30, self.RULE_comparison)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 411
            localctx.s1 = self.setlxSum(localctx.enableIgnore)
            localctx.c = localctx.s1.s 
            self.state = 445
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [SetlXgrammarParser.T__43]:
                self.state = 413
                self.match(SetlXgrammarParser.T__43)
                self.state = 414
                localctx.s2 = self.setlxSum(localctx.enableIgnore)
                localctx.c = Equal(localctx.s1.s,localctx.s2.s) 
                pass
            elif token in [SetlXgrammarParser.T__44]:
                self.state = 417
                self.match(SetlXgrammarParser.T__44)
                self.state = 418
                localctx.s2 = self.setlxSum(localctx.enableIgnore)
                localctx.c = NotEqual(localctx.s1.s,localctx.s2.s) 
                pass
            elif token in [SetlXgrammarParser.T__45]:
                self.state = 421
                self.match(SetlXgrammarParser.T__45)
                self.state = 422
                localctx.s2 = self.setlxSum(localctx.enableIgnore)
                localctx.c = LessThan(localctx.s1.s,localctx.s2.s) 
                pass
            elif token in [SetlXgrammarParser.T__46]:
                self.state = 425
                self.match(SetlXgrammarParser.T__46)
                self.state = 426
                localctx.s2 = self.setlxSum(localctx.enableIgnore)
                localctx.c = LessOrEqual(localctx.s1.s,localctx.s2.s) 
                pass
            elif token in [SetlXgrammarParser.T__47]:
                self.state = 429
                self.match(SetlXgrammarParser.T__47)
                self.state = 430
                localctx.s2 = self.setlxSum(localctx.enableIgnore)
                localctx.c = GreaterThan(localctx.s1.s,localctx.s2.s) 
                pass
            elif token in [SetlXgrammarParser.T__48]:
                self.state = 433
                self.match(SetlXgrammarParser.T__48)
                self.state = 434
                localctx.s2 = self.setlxSum(localctx.enableIgnore)
                localctx.c = GreaterOrEqual(localctx.s1.s,localctx.s2.s) 
                pass
            elif token in [SetlXgrammarParser.T__49]:
                self.state = 437
                self.match(SetlXgrammarParser.T__49)
                self.state = 438
                localctx.s2 = self.setlxSum(localctx.enableIgnore)
                localctx.c = SetlXIn(localctx.s1.s,localctx.s2.s) 
                pass
            elif token in [SetlXgrammarParser.T__50]:
                self.state = 441
                self.match(SetlXgrammarParser.T__50)
                self.state = 442
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
        self.enterRule(localctx, 32, self.RULE_setlxSum)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 447
            localctx.p1 = self.product(localctx.enableIgnore)
            localctx.s = localctx.p1.p
            self.state = 459
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==SetlXgrammarParser.T__51 or _la==SetlXgrammarParser.T__52:
                self.state = 457
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [SetlXgrammarParser.T__51]:
                    self.state = 449
                    self.match(SetlXgrammarParser.T__51)
                    self.state = 450
                    localctx.p2 = self.product(localctx.enableIgnore)
                    localctx.s = Sum(localctx.p1.p,localctx.p2.p) 
                    pass
                elif token in [SetlXgrammarParser.T__52]:
                    self.state = 453
                    self.match(SetlXgrammarParser.T__52)
                    self.state = 454
                    localctx.p2 = self.product(localctx.enableIgnore)
                    localctx.s = Difference(localctx.p1.p,localctx.p2.p) 
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 461
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
        self.enterRule(localctx, 34, self.RULE_product)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 462
            localctx.r1 = self.setlxReduce(localctx.enableIgnore)
            localctx.p = localctx.r1.r
            self.state = 486
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << SetlXgrammarParser.T__53) | (1 << SetlXgrammarParser.T__54) | (1 << SetlXgrammarParser.T__55) | (1 << SetlXgrammarParser.T__56) | (1 << SetlXgrammarParser.T__57))) != 0):
                self.state = 484
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [SetlXgrammarParser.T__53]:
                    self.state = 464
                    self.match(SetlXgrammarParser.T__53)
                    self.state = 465
                    localctx.r2 = self.setlxReduce(localctx.enableIgnore)
                    localctx.p = Product(localctx.p,localctx.r2.r) 
                    pass
                elif token in [SetlXgrammarParser.T__54]:
                    self.state = 468
                    self.match(SetlXgrammarParser.T__54)
                    self.state = 469
                    localctx.r2 = self.setlxReduce(localctx.enableIgnore)
                    localctx.p = Quotient(localctx.p,localctx.r2.r) 
                    pass
                elif token in [SetlXgrammarParser.T__55]:
                    self.state = 472
                    self.match(SetlXgrammarParser.T__55)
                    self.state = 473
                    localctx.r2 = self.setlxReduce(localctx.enableIgnore)
                    localctx.p = IntegerDivision(localctx.p,localctx.r2.r) 
                    pass
                elif token in [SetlXgrammarParser.T__56]:
                    self.state = 476
                    self.match(SetlXgrammarParser.T__56)
                    self.state = 477
                    localctx.r2 = self.setlxReduce(localctx.enableIgnore)
                    localctx.p = Modulo(localctx.p,localctx.r2.r) 
                    pass
                elif token in [SetlXgrammarParser.T__57]:
                    self.state = 480
                    self.match(SetlXgrammarParser.T__57)
                    self.state = 481
                    localctx.r2 = self.setlxReduce(localctx.enableIgnore)
                    localctx.p = CartesianProduct(localctx.p,localctx.r2.r) 
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 488
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
        self.enterRule(localctx, 36, self.RULE_setlxReduce)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 489
            localctx.p1 = self.prefixOperation(localctx.enableIgnore)
            localctx.r = localctx.p1.p
            self.state = 501
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==SetlXgrammarParser.T__58 or _la==SetlXgrammarParser.T__59:
                self.state = 499
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [SetlXgrammarParser.T__58]:
                    self.state = 491
                    self.match(SetlXgrammarParser.T__58)
                    self.state = 492
                    localctx.p2 = self.prefixOperation(localctx.enableIgnore)
                    localctx.r = SumOfMembersBinary(localctx.r,localctx.p2.p) 
                    pass
                elif token in [SetlXgrammarParser.T__59]:
                    self.state = 495
                    self.match(SetlXgrammarParser.T__59)
                    self.state = 496
                    localctx.p2 = self.prefixOperation(localctx.enableIgnore)
                    localctx.r = ProductOfMembersBinary(localctx.r,localctx.p2.p) 
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 503
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
        self.enterRule(localctx, 38, self.RULE_prefixOperation)
        self._la = 0 # Token type
        try:
            self.state = 528
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,33,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 504
                localctx._factor = self.factor(localctx.enableIgnore)
                localctx.p = localctx._factor.f
                self.state = 510
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==SetlXgrammarParser.T__60:
                    self.state = 506
                    self.match(SetlXgrammarParser.T__60)
                    self.state = 507
                    localctx._prefixOperation = self.prefixOperation(localctx.enableIgnore)
                    localctx.p = Power(localctx.p,localctx._prefixOperation.p) 


                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 512
                self.match(SetlXgrammarParser.T__58)
                self.state = 513
                localctx._prefixOperation = self.prefixOperation(localctx.enableIgnore)
                localctx.p = SumOfMembers(localctx._prefixOperation.p) 
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 516
                self.match(SetlXgrammarParser.T__59)
                self.state = 517
                localctx._prefixOperation = self.prefixOperation(localctx.enableIgnore)
                localctx.p = ProductOfMembers(localctx._prefixOperation.p) 
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 520
                self.match(SetlXgrammarParser.T__61)
                self.state = 521
                localctx._prefixOperation = self.prefixOperation(localctx.enableIgnore)
                localctx.p = Cardinality(localctx._prefixOperation.p) 
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 524
                self.match(SetlXgrammarParser.T__52)
                self.state = 525
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
        self.enterRule(localctx, 40, self.RULE_factor)
        self._la = 0 # Token type
        try:
            self.state = 585
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,39,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 530
                self.match(SetlXgrammarParser.T__62)
                self.state = 531
                localctx._factor = self.factor(localctx.enableIgnore)
                localctx.f = SetlXNot(localctx._factor.f) 
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 534
                self.match(SetlXgrammarParser.T__63)
                self.state = 535
                self.match(SetlXgrammarParser.T__1)
                self.state = 536
                localctx._iteratorChain = self.iteratorChain(localctx.enableIgnore)
                self.state = 537
                self.match(SetlXgrammarParser.T__13)
                self.state = 538
                localctx._condition = self.condition()
                self.state = 539
                self.match(SetlXgrammarParser.T__2)
                localctx.f = Forall(localctx._iteratorChain.ic,localctx._condition.cnd)
                		
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 542
                self.match(SetlXgrammarParser.T__64)
                self.state = 543
                self.match(SetlXgrammarParser.T__1)
                self.state = 544
                localctx._iteratorChain = self.iteratorChain(localctx.enableIgnore)
                self.state = 545
                self.match(SetlXgrammarParser.T__13)
                self.state = 546
                localctx._condition = self.condition()
                self.state = 547
                self.match(SetlXgrammarParser.T__2)
                localctx.f = Exists(localctx._iteratorChain.ic,localctx._condition.cnd)
                		
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 561
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [SetlXgrammarParser.T__1]:
                    self.state = 550
                    self.match(SetlXgrammarParser.T__1)
                    self.state = 551
                    localctx._exprContent = self.exprContent(localctx.enableIgnore)
                    self.state = 552
                    self.match(SetlXgrammarParser.T__2)
                    localctx.f = localctx._exprContent.ex 
                    pass
                elif token in [SetlXgrammarParser.T__65, SetlXgrammarParser.T__66, SetlXgrammarParser.T__67]:
                    self.state = 555
                    localctx._procedure = self.procedure(None)
                    localctx.f = localctx._procedure.pd 
                    pass
                elif token in [SetlXgrammarParser.ID]:
                    self.state = 558
                    localctx._variable = self.variable()
                    localctx.f = localctx._variable.v 
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 572
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << SetlXgrammarParser.T__1) | (1 << SetlXgrammarParser.T__3) | (1 << SetlXgrammarParser.T__33) | (1 << SetlXgrammarParser.T__34))) != 0):
                    self.state = 570
                    self._errHandler.sync(self)
                    token = self._input.LA(1)
                    if token in [SetlXgrammarParser.T__33]:
                        self.state = 563
                        self.match(SetlXgrammarParser.T__33)
                        self.state = 564
                        localctx._variable = self.variable()
                        localctx.f = MemberAccess(localctx.f,localctx._variable.v) 
                        pass
                    elif token in [SetlXgrammarParser.T__1, SetlXgrammarParser.T__3, SetlXgrammarParser.T__34]:
                        self.state = 567
                        localctx._call = self.call(localctx.enableIgnore,localctx.f)
                        localctx.f = localctx._call.c 
                        pass
                    else:
                        raise NoViableAltException(self)

                    self.state = 574
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 577
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==SetlXgrammarParser.T__62:
                    self.state = 575
                    self.match(SetlXgrammarParser.T__62)
                    localctx.f = Factorial(localctx.f) 


                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 579
                localctx._value = self.value(localctx.enableIgnore)
                localctx.f = localctx._value.v 
                self.state = 583
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==SetlXgrammarParser.T__62:
                    self.state = 581
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

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1, name=None):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.name = None
            self.pd = None
            self._procedureParameters = None # ProcedureParametersContext
            self._block = None # BlockContext
            self.name = name

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




    def procedure(self, name):

        localctx = SetlXgrammarParser.ProcedureContext(self, self._ctx, self.state, name)
        self.enterRule(localctx, 42, self.RULE_procedure)
        try:
            self.state = 614
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [SetlXgrammarParser.T__65]:
                self.enterOuterAlt(localctx, 1)
                self.state = 587
                self.match(SetlXgrammarParser.T__65)
                self.state = 588
                self.match(SetlXgrammarParser.T__1)
                self.state = 589
                localctx._procedureParameters = self.procedureParameters(True)
                self.state = 590
                self.match(SetlXgrammarParser.T__2)
                self.state = 591
                self.match(SetlXgrammarParser.T__3)
                self.state = 592
                localctx._block = self.block()
                self.state = 593
                self.match(SetlXgrammarParser.T__5)
                localctx.pd = Procedure(localctx._procedureParameters.paramList, localctx._block.blk,localctx.name,None) 
                		
                pass
            elif token in [SetlXgrammarParser.T__66]:
                self.enterOuterAlt(localctx, 2)
                self.state = 596
                self.match(SetlXgrammarParser.T__66)
                self.state = 597
                self.match(SetlXgrammarParser.T__1)
                self.state = 598
                localctx._procedureParameters = self.procedureParameters(False)
                self.state = 599
                self.match(SetlXgrammarParser.T__2)
                self.state = 600
                self.match(SetlXgrammarParser.T__3)
                self.state = 601
                localctx._block = self.block()
                self.state = 602
                self.match(SetlXgrammarParser.T__5)
                localctx.pd = CachedProcedure(localctx._procedureParameters.paramList, localctx._block.blk,localctx.name) 
                		
                pass
            elif token in [SetlXgrammarParser.T__67]:
                self.enterOuterAlt(localctx, 3)
                self.state = 605
                self.match(SetlXgrammarParser.T__67)
                self.state = 606
                self.match(SetlXgrammarParser.T__1)
                self.state = 607
                localctx._procedureParameters = self.procedureParameters(True)
                self.state = 608
                self.match(SetlXgrammarParser.T__2)
                self.state = 609
                self.match(SetlXgrammarParser.T__3)
                self.state = 610
                localctx._block = self.block()
                self.state = 611
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
        self.enterRule(localctx, 44, self.RULE_procedureParameters)

        localctx.paramList = []
            
        self._la = 0 # Token type
        try:
            self.state = 663
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,46,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 616
                localctx.pp1 = self.procedureParameter(localctx.enableRw)
                localctx.paramList.append(localctx.pp1.param) 
                self.state = 624
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,41,self._ctx)
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1:
                        self.state = 618
                        self.match(SetlXgrammarParser.T__25)
                        self.state = 619
                        localctx.pp2 = self.procedureParameter(localctx.enableRw)
                        localctx.paramList.append(localctx.pp2.param)  
                    self.state = 626
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,41,self._ctx)

                self.state = 633
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,42,self._ctx)
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1:
                        self.state = 627
                        self.match(SetlXgrammarParser.T__25)
                        self.state = 628
                        localctx.dp1 = self.procedureDefaultParameter()
                        localctx.paramList.append(localctx.dp1.param)  
                    self.state = 635
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,42,self._ctx)

                self.state = 640
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==SetlXgrammarParser.T__25:
                    self.state = 636
                    self.match(SetlXgrammarParser.T__25)
                    self.state = 637
                    localctx.lp1 = self.procedureListParameter()
                    localctx.paramList.append(localctx.lp1.param) 


                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 642
                localctx.dp2 = self.procedureDefaultParameter()
                localctx.paramList.append(localctx.dp2.param) 
                self.state = 650
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,44,self._ctx)
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1:
                        self.state = 644
                        self.match(SetlXgrammarParser.T__25)
                        self.state = 645
                        localctx.dp3 = self.procedureDefaultParameter()
                        localctx.paramList.append(localctx.dp3.param)  
                    self.state = 652
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,44,self._ctx)

                self.state = 657
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==SetlXgrammarParser.T__25:
                    self.state = 653
                    self.match(SetlXgrammarParser.T__25)
                    self.state = 654
                    localctx.lp2 = self.procedureListParameter()
                    localctx.paramList.append(localctx.lp2.param) 


                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 659
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
        self.enterRule(localctx, 46, self.RULE_procedureParameter)
        try:
            self.state = 673
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,47,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 665
                if not localctx.enableRw:
                    from antlr4.error.Errors import FailedPredicateException
                    raise FailedPredicateException(self, "$enableRw")
                self.state = 666
                self.match(SetlXgrammarParser.T__68)
                self.state = 667
                localctx._assignableVariable = self.assignableVariable()
                localctx.param = ReadWriteParameter(localctx._assignableVariable.v.id) 
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 670
                localctx._variable = self.variable()
                localctx.param = Parameter(localctx._variable.v.id, None, False) 
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
        self.enterRule(localctx, 48, self.RULE_procedureDefaultParameter)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 675
            localctx._assignableVariable = self.assignableVariable()
            self.state = 676
            self.match(SetlXgrammarParser.T__32)
            self.state = 677
            localctx._expr = self.expr(False)
            localctx.param = Parameter(localctx._assignableVariable.v.id, localctx._expr.ex, False) 
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
        self.enterRule(localctx, 50, self.RULE_procedureListParameter)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 680
            self.match(SetlXgrammarParser.T__53)
            self.state = 681
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

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1, enableIgnore=None, callable=None):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.enableIgnore = None
            self.callable = None
            self.c = None
            self._callParameters = None # CallParametersContext
            self._collectionAccessParams = None # CollectionAccessParamsContext
            self._expr = None # ExprContext
            self.enableIgnore = enableIgnore
            self.callable = callable

        def callParameters(self):
            return self.getTypedRuleContext(SetlXgrammarParser.CallParametersContext,0)


        def collectionAccessParams(self):
            return self.getTypedRuleContext(SetlXgrammarParser.CollectionAccessParamsContext,0)


        def expr(self):
            return self.getTypedRuleContext(SetlXgrammarParser.ExprContext,0)


        def getRuleIndex(self):
            return SetlXgrammarParser.RULE_call

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCall" ):
                listener.enterCall(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCall" ):
                listener.exitCall(self)




    def call(self, enableIgnore, callable):

        localctx = SetlXgrammarParser.CallContext(self, self._ctx, self.state, enableIgnore, callable)
        self.enterRule(localctx, 52, self.RULE_call)
        try:
            self.state = 699
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [SetlXgrammarParser.T__1]:
                self.enterOuterAlt(localctx, 1)
                self.state = 684
                self.match(SetlXgrammarParser.T__1)
                self.state = 685
                localctx._callParameters = self.callParameters(localctx.enableIgnore)
                self.state = 686
                self.match(SetlXgrammarParser.T__2)
                localctx.c = FunctionCall(localctx._callParameters.params,localctx.callable) 
                		
                pass
            elif token in [SetlXgrammarParser.T__34]:
                self.enterOuterAlt(localctx, 2)
                self.state = 689
                self.match(SetlXgrammarParser.T__34)
                self.state = 690
                localctx._collectionAccessParams = self.collectionAccessParams(localctx.enableIgnore)
                self.state = 691
                self.match(SetlXgrammarParser.T__35)
                localctx.c = CollectionAccess(localctx._collectionAccessParams.p,localctx.callable) 
                pass
            elif token in [SetlXgrammarParser.T__3]:
                self.enterOuterAlt(localctx, 3)
                self.state = 694
                self.match(SetlXgrammarParser.T__3)
                self.state = 695
                localctx._expr = self.expr(localctx.enableIgnore)
                self.state = 696
                self.match(SetlXgrammarParser.T__5)
                localctx.c = CollectMap(localctx._expr.ex,localctx.callable) 
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
        self.enterRule(localctx, 54, self.RULE_collectionAccessParams)

        params = []
            
        self._la = 0 # Token type
        try:
            self.state = 726
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,52,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 701
                localctx.e1 = self.expr(localctx.enableIgnore)
                self.state = 720
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [SetlXgrammarParser.RANGE_SIGN]:
                    self.state = 702
                    self.match(SetlXgrammarParser.RANGE_SIGN)
                    self.state = 707
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,49,self._ctx)
                    if la_ == 1:
                        self.state = 703
                        localctx.e2 = self.expr(localctx.enableIgnore)
                        localctx.p = ListRange(localctx.e1.ex,localctx.e2.ex) 
                        pass

                    elif la_ == 2:
                        localctx.p = ListRange(localctx.e1.ex,None) 
                        pass


                    pass
                elif token in [SetlXgrammarParser.T__25]:
                    self.state = 713 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    while True:
                        self.state = 709
                        self.match(SetlXgrammarParser.T__25)
                        self.state = 710
                        localctx.e3 = self.expr(False)
                        params.append(localctx.e3.ex) 
                        self.state = 715 
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
                self.state = 722
                self.match(SetlXgrammarParser.RANGE_SIGN)
                self.state = 723
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
        self.enterRule(localctx, 56, self.RULE_callParameters)

        localctx.params = []
            
        self._la = 0 # Token type
        try:
            self.state = 742
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,54,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 728
                localctx._exprList = self.exprList(localctx.enableIgnore)
                localctx.params = localctx._exprList.exprs
                self.state = 735
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==SetlXgrammarParser.T__25:
                    self.state = 730
                    self.match(SetlXgrammarParser.T__25)
                    self.state = 731
                    self.match(SetlXgrammarParser.T__53)
                    self.state = 732
                    localctx._exprContent = self.exprContent(False)
                    localctx.params.append(OperatorExpression(localctx._exprContent.ex))


                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 737
                self.match(SetlXgrammarParser.T__53)
                self.state = 738
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
        self.enterRule(localctx, 58, self.RULE_value)

        cb = None
            
        try:
            self.state = 770
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,57,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 744
                self.match(SetlXgrammarParser.T__34)
                self.state = 748
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,55,self._ctx)
                if la_ == 1:
                    self.state = 745
                    localctx._collectionBuilder = self.collectionBuilder(localctx.enableIgnore)
                    cb = localctx._collectionBuilder.cb; 


                self.state = 750
                self.match(SetlXgrammarParser.T__35)
                localctx.v = SetlXList(cb) 
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 752
                self.match(SetlXgrammarParser.T__3)
                self.state = 756
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,56,self._ctx)
                if la_ == 1:
                    self.state = 753
                    localctx._collectionBuilder = self.collectionBuilder(localctx.enableIgnore)
                    cb = localctx._collectionBuilder.cb; 


                self.state = 758
                self.match(SetlXgrammarParser.T__5)
                localctx.v = SetListConstructor(cb) 
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 760
                localctx._STRING = self.match(SetlXgrammarParser.STRING)
                localctx.v = SetlXString((None if localctx._STRING is None else localctx._STRING.text)) 
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 762
                localctx._LITERAL = self.match(SetlXgrammarParser.LITERAL)
                localctx.v = SetlXLiteral((None if localctx._LITERAL is None else localctx._LITERAL.text)) 
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 764
                localctx._atomicValue = self.atomicValue()
                localctx.v = localctx._atomicValue.av 
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 767
                if not localctx.enableIgnore:
                    from antlr4.error.Errors import FailedPredicateException
                    raise FailedPredicateException(self, "$enableIgnore")
                self.state = 768
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
        self.enterRule(localctx, 60, self.RULE_collectionBuilder)

        exprs = []
            
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 772
            localctx.e1 = self.expr(localctx.enableIgnore)
            self.state = 819
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [SetlXgrammarParser.T__25]:
                self.state = 773
                self.match(SetlXgrammarParser.T__25)
                self.state = 774
                localctx.e2 = self.expr(localctx.enableIgnore)
                self.state = 796
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [SetlXgrammarParser.RANGE_SIGN]:
                    self.state = 775
                    self.match(SetlXgrammarParser.RANGE_SIGN)
                    self.state = 776
                    localctx.e3 = self.expr(localctx.enableIgnore)
                    localctx.cb = Range(localctx.e1.ex, localctx.e2.ex, localctx.e3.ex) 
                    pass
                elif token in [SetlXgrammarParser.T__5, SetlXgrammarParser.T__13, SetlXgrammarParser.T__25, SetlXgrammarParser.T__35]:
                    exprs.append(localctx.e1.ex); exprs.append(localctx.e2.ex) 
                    self.state = 786
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    while _la==SetlXgrammarParser.T__25:
                        self.state = 780
                        self.match(SetlXgrammarParser.T__25)
                        self.state = 781
                        localctx.e3 = self.expr(localctx.enableIgnore)
                        exprs.append(localctx.e3.ex) 
                        self.state = 788
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)

                    self.state = 794
                    self._errHandler.sync(self)
                    token = self._input.LA(1)
                    if token in [SetlXgrammarParser.T__13]:
                        self.state = 789
                        self.match(SetlXgrammarParser.T__13)
                        self.state = 790
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
                self.state = 798
                self.match(SetlXgrammarParser.RANGE_SIGN)
                self.state = 799
                localctx.e3 = self.expr(localctx.enableIgnore)
                localctx.cb = Range(localctx.e1.ex, None, localctx.e3.ex) 
                pass
            elif token in [SetlXgrammarParser.T__5, SetlXgrammarParser.T__13, SetlXgrammarParser.T__35]:
                exprs.append(localctx.e1.ex) 
                self.state = 808
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [SetlXgrammarParser.T__13]:
                    self.state = 803
                    self.match(SetlXgrammarParser.T__13)
                    self.state = 804
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
                self.state = 810
                self.match(SetlXgrammarParser.T__10)
                self.state = 811
                localctx._iteratorChain = self.iteratorChain(localctx.enableIgnore)
                self.state = 817
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [SetlXgrammarParser.T__13]:
                    self.state = 812
                    self.match(SetlXgrammarParser.T__13)
                    self.state = 813
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
        self.enterRule(localctx, 62, self.RULE_iteratorChain)

        localctx.ic = []
            
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 821
            localctx.i1 = self.iterator(localctx.enableIgnore)
            localctx.ic.append(localctx.i1.iter)
            self.state = 829
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==SetlXgrammarParser.T__25:
                self.state = 823
                self.match(SetlXgrammarParser.T__25)
                self.state = 824
                localctx.i2 = self.iterator(localctx.enableIgnore)
                localctx.ic.append(localctx.i2.iter) 
                self.state = 831
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
        self.enterRule(localctx, 64, self.RULE_iterator)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 832
            localctx._assignable = self.assignable(True)
            self.state = 833
            self.match(SetlXgrammarParser.T__49)
            self.state = 834
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
        self.enterRule(localctx, 66, self.RULE_atomicValue)
        try:
            self.state = 847
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [SetlXgrammarParser.NUMBER]:
                self.enterOuterAlt(localctx, 1)
                self.state = 837
                localctx._NUMBER = self.match(SetlXgrammarParser.NUMBER)
                localctx.av = SetlXFraction((None if localctx._NUMBER is None else localctx._NUMBER.text)) 
                pass
            elif token in [SetlXgrammarParser.DOUBLE]:
                self.enterOuterAlt(localctx, 2)
                self.state = 839
                localctx._DOUBLE = self.match(SetlXgrammarParser.DOUBLE)
                localctx.av = SetlXDouble((None if localctx._DOUBLE is None else localctx._DOUBLE.text)) 
                pass
            elif token in [SetlXgrammarParser.T__69]:
                self.enterOuterAlt(localctx, 3)
                self.state = 841
                self.match(SetlXgrammarParser.T__69)
                localctx.av = SetlXOm() 
                pass
            elif token in [SetlXgrammarParser.T__70]:
                self.enterOuterAlt(localctx, 4)
                self.state = 843
                self.match(SetlXgrammarParser.T__70)
                localctx.av = SetlXTrue() 
                pass
            elif token in [SetlXgrammarParser.T__71]:
                self.enterOuterAlt(localctx, 5)
                self.state = 845
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
        self.enterRule(localctx, 68, self.RULE_variable)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 849
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
        self.enterRule(localctx, 70, self.RULE_condition)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 852
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
        self.enterRule(localctx, 72, self.RULE_assignmentList)

        localctx.al = []
            
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 855
            localctx.a1 = self.assignable(True)
            localctx.al.append(localctx.a1.a) 
            self.state = 863
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==SetlXgrammarParser.T__25:
                self.state = 857
                self.match(SetlXgrammarParser.T__25)
                self.state = 858
                localctx.a2 = self.assignable(True)
                localctx.al.append(localctx.a2.a) 
                self.state = 865
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
        self._predicates[5] = self.assignable_sempred
        self._predicates[23] = self.procedureParameter_sempred
        self._predicates[29] = self.value_sempred
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
         




