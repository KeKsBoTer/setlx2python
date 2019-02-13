# Generated from SetlXgrammar.g4 by ANTLR 4.7.1
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2R")
        buf.write("\u0226\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.")
        buf.write("\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64")
        buf.write("\t\64\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:")
        buf.write("\4;\t;\4<\t<\4=\t=\4>\t>\4?\t?\4@\t@\4A\tA\4B\tB\4C\t")
        buf.write("C\4D\tD\4E\tE\4F\tF\4G\tG\4H\tH\4I\tI\4J\tJ\4K\tK\4L\t")
        buf.write("L\4M\tM\4N\tN\4O\tO\4P\tP\4Q\tQ\3\2\3\2\3\2\3\3\3\3\3")
        buf.write("\4\3\4\3\5\3\5\3\6\3\6\3\7\3\7\3\7\3\7\3\7\3\b\3\b\3\b")
        buf.write("\3\b\3\b\3\b\3\b\3\t\3\t\3\t\3\t\3\t\3\n\3\n\3\13\3\13")
        buf.write("\3\13\3\13\3\13\3\13\3\13\3\13\3\f\3\f\3\f\3\f\3\r\3\r")
        buf.write("\3\16\3\16\3\16\3\16\3\16\3\16\3\17\3\17\3\17\3\20\3\20")
        buf.write("\3\21\3\21\3\21\3\21\3\22\3\22\3\22\3\22\3\22\3\22\3\23")
        buf.write("\3\23\3\23\3\23\3\23\3\23\3\23\3\23\3\23\3\23\3\24\3\24")
        buf.write("\3\24\3\24\3\24\3\24\3\25\3\25\3\25\3\25\3\25\3\25\3\25")
        buf.write("\3\25\3\25\3\26\3\26\3\26\3\26\3\26\3\27\3\27\3\27\3\27")
        buf.write("\3\27\3\27\3\27\3\30\3\30\3\30\3\30\3\30\3\30\3\30\3\31")
        buf.write("\3\31\3\32\3\32\3\32\3\33\3\33\3\33\3\34\3\34\3\34\3\35")
        buf.write("\3\35\3\35\3\36\3\36\3\36\3\37\3\37\3\37\3 \3 \3 \3!\3")
        buf.write("!\3\"\3\"\3#\3#\3$\3$\3%\3%\3%\3%\3%\3&\3&\3&\3&\3&\3")
        buf.write("\'\3\'\3\'\3\'\3(\3(\3(\3)\3)\3)\3*\3*\3*\3+\3+\3+\3,")
        buf.write("\3,\3,\3-\3-\3.\3.\3.\3/\3/\3\60\3\60\3\60\3\61\3\61\3")
        buf.write("\61\3\62\3\62\3\62\3\62\3\62\3\62\3\63\3\63\3\64\3\64")
        buf.write("\3\65\3\65\3\66\3\66\3\67\3\67\38\38\39\39\39\3:\3:\3")
        buf.write(":\3;\3;\3;\3<\3<\3<\3=\3=\3>\3>\3?\3?\3?\3?\3?\3?\3?\3")
        buf.write("@\3@\3@\3@\3@\3@\3@\3A\3A\3A\3A\3A\3A\3A\3A\3A\3A\3B\3")
        buf.write("B\3B\3B\3B\3B\3B\3B\3B\3B\3B\3B\3B\3B\3B\3B\3C\3C\3C\3")
        buf.write("C\3C\3C\3C\3C\3D\3D\3D\3E\3E\3E\3F\3F\3F\3F\3F\3G\3G\3")
        buf.write("G\3G\3G\3G\3H\3H\7H\u01bf\nH\fH\16H\u01c2\13H\3I\3I\3")
        buf.write("I\7I\u01c7\nI\fI\16I\u01ca\13I\5I\u01cc\nI\3J\5J\u01cf")
        buf.write("\nJ\3J\3J\6J\u01d3\nJ\rJ\16J\u01d4\3J\3J\5J\u01d9\nJ\3")
        buf.write("J\6J\u01dc\nJ\rJ\16J\u01dd\5J\u01e0\nJ\3K\3K\3K\3L\3L")
        buf.write("\3L\3L\7L\u01e9\nL\fL\16L\u01ec\13L\3L\3L\3M\3M\3M\3M")
        buf.write("\7M\u01f4\nM\fM\16M\u01f7\13M\3M\3M\3N\3N\3N\3N\7N\u01ff")
        buf.write("\nN\fN\16N\u0202\13N\3N\3N\3O\3O\3O\3O\3O\6O\u020b\nO")
        buf.write("\rO\16O\u020c\3O\7O\u0210\nO\fO\16O\u0213\13O\3O\6O\u0216")
        buf.write("\nO\rO\16O\u0217\3O\3O\3O\3O\3P\6P\u021f\nP\rP\16P\u0220")
        buf.write("\3P\3P\3Q\3Q\2\2R\3\3\5\4\7\5\t\6\13\7\r\b\17\t\21\n\23")
        buf.write("\13\25\f\27\r\31\16\33\17\35\20\37\21!\22#\23%\24\'\25")
        buf.write(")\26+\27-\30/\31\61\32\63\33\65\34\67\359\36;\37= ?!A")
        buf.write("\"C#E$G%I&K\'M(O)Q*S+U,W-Y.[/]\60_\61a\62c\63e\64g\65")
        buf.write("i\66k\67m8o9q:s;u<w=y>{?}@\177A\u0081B\u0083C\u0085D\u0087")
        buf.write("E\u0089F\u008bG\u008dH\u008fI\u0091J\u0093K\u0095L\u0097")
        buf.write("M\u0099N\u009bO\u009dP\u009fQ\u00a1R\3\2\f\4\2C\\c|\6")
        buf.write("\2\62;C\\aac|\4\2GGgg\4\2--//\4\2$$^^\3\2))\4\2\f\f\17")
        buf.write("\17\3\2,,\4\2,,\61\61\5\2\13\f\17\17\"\"\2\u0237\2\3\3")
        buf.write("\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2")
        buf.write("\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21\3\2\2\2\2\23\3\2\2\2")
        buf.write("\2\25\3\2\2\2\2\27\3\2\2\2\2\31\3\2\2\2\2\33\3\2\2\2\2")
        buf.write("\35\3\2\2\2\2\37\3\2\2\2\2!\3\2\2\2\2#\3\2\2\2\2%\3\2")
        buf.write("\2\2\2\'\3\2\2\2\2)\3\2\2\2\2+\3\2\2\2\2-\3\2\2\2\2/\3")
        buf.write("\2\2\2\2\61\3\2\2\2\2\63\3\2\2\2\2\65\3\2\2\2\2\67\3\2")
        buf.write("\2\2\29\3\2\2\2\2;\3\2\2\2\2=\3\2\2\2\2?\3\2\2\2\2A\3")
        buf.write("\2\2\2\2C\3\2\2\2\2E\3\2\2\2\2G\3\2\2\2\2I\3\2\2\2\2K")
        buf.write("\3\2\2\2\2M\3\2\2\2\2O\3\2\2\2\2Q\3\2\2\2\2S\3\2\2\2\2")
        buf.write("U\3\2\2\2\2W\3\2\2\2\2Y\3\2\2\2\2[\3\2\2\2\2]\3\2\2\2")
        buf.write("\2_\3\2\2\2\2a\3\2\2\2\2c\3\2\2\2\2e\3\2\2\2\2g\3\2\2")
        buf.write("\2\2i\3\2\2\2\2k\3\2\2\2\2m\3\2\2\2\2o\3\2\2\2\2q\3\2")
        buf.write("\2\2\2s\3\2\2\2\2u\3\2\2\2\2w\3\2\2\2\2y\3\2\2\2\2{\3")
        buf.write("\2\2\2\2}\3\2\2\2\2\177\3\2\2\2\2\u0081\3\2\2\2\2\u0083")
        buf.write("\3\2\2\2\2\u0085\3\2\2\2\2\u0087\3\2\2\2\2\u0089\3\2\2")
        buf.write("\2\2\u008b\3\2\2\2\2\u008d\3\2\2\2\2\u008f\3\2\2\2\2\u0091")
        buf.write("\3\2\2\2\2\u0093\3\2\2\2\2\u0095\3\2\2\2\2\u0097\3\2\2")
        buf.write("\2\2\u0099\3\2\2\2\2\u009b\3\2\2\2\2\u009d\3\2\2\2\2\u009f")
        buf.write("\3\2\2\2\2\u00a1\3\2\2\2\3\u00a3\3\2\2\2\5\u00a6\3\2\2")
        buf.write("\2\7\u00a8\3\2\2\2\t\u00aa\3\2\2\2\13\u00ac\3\2\2\2\r")
        buf.write("\u00ae\3\2\2\2\17\u00b3\3\2\2\2\21\u00ba\3\2\2\2\23\u00bf")
        buf.write("\3\2\2\2\25\u00c1\3\2\2\2\27\u00c9\3\2\2\2\31\u00cd\3")
        buf.write("\2\2\2\33\u00cf\3\2\2\2\35\u00d5\3\2\2\2\37\u00d8\3\2")
        buf.write("\2\2!\u00da\3\2\2\2#\u00de\3\2\2\2%\u00e4\3\2\2\2\'\u00ee")
        buf.write("\3\2\2\2)\u00f4\3\2\2\2+\u00fd\3\2\2\2-\u0102\3\2\2\2")
        buf.write("/\u0109\3\2\2\2\61\u0110\3\2\2\2\63\u0112\3\2\2\2\65\u0115")
        buf.write("\3\2\2\2\67\u0118\3\2\2\29\u011b\3\2\2\2;\u011e\3\2\2")
        buf.write("\2=\u0121\3\2\2\2?\u0124\3\2\2\2A\u0127\3\2\2\2C\u0129")
        buf.write("\3\2\2\2E\u012b\3\2\2\2G\u012d\3\2\2\2I\u012f\3\2\2\2")
        buf.write("K\u0134\3\2\2\2M\u0139\3\2\2\2O\u013d\3\2\2\2Q\u0140\3")
        buf.write("\2\2\2S\u0143\3\2\2\2U\u0146\3\2\2\2W\u0149\3\2\2\2Y\u014c")
        buf.write("\3\2\2\2[\u014e\3\2\2\2]\u0151\3\2\2\2_\u0153\3\2\2\2")
        buf.write("a\u0156\3\2\2\2c\u0159\3\2\2\2e\u015f\3\2\2\2g\u0161\3")
        buf.write("\2\2\2i\u0163\3\2\2\2k\u0165\3\2\2\2m\u0167\3\2\2\2o\u0169")
        buf.write("\3\2\2\2q\u016b\3\2\2\2s\u016e\3\2\2\2u\u0171\3\2\2\2")
        buf.write("w\u0174\3\2\2\2y\u0177\3\2\2\2{\u0179\3\2\2\2}\u017b\3")
        buf.write("\2\2\2\177\u0182\3\2\2\2\u0081\u0189\3\2\2\2\u0083\u0193")
        buf.write("\3\2\2\2\u0085\u01a3\3\2\2\2\u0087\u01ab\3\2\2\2\u0089")
        buf.write("\u01ae\3\2\2\2\u008b\u01b1\3\2\2\2\u008d\u01b6\3\2\2\2")
        buf.write("\u008f\u01bc\3\2\2\2\u0091\u01cb\3\2\2\2\u0093\u01ce\3")
        buf.write("\2\2\2\u0095\u01e1\3\2\2\2\u0097\u01e4\3\2\2\2\u0099\u01ef")
        buf.write("\3\2\2\2\u009b\u01fa\3\2\2\2\u009d\u0205\3\2\2\2\u009f")
        buf.write("\u021e\3\2\2\2\u00a1\u0224\3\2\2\2\u00a3\u00a4\7k\2\2")
        buf.write("\u00a4\u00a5\7h\2\2\u00a5\4\3\2\2\2\u00a6\u00a7\7*\2\2")
        buf.write("\u00a7\6\3\2\2\2\u00a8\u00a9\7+\2\2\u00a9\b\3\2\2\2\u00aa")
        buf.write("\u00ab\7}\2\2\u00ab\n\3\2\2\2\u00ac\u00ad\7\177\2\2\u00ad")
        buf.write("\f\3\2\2\2\u00ae\u00af\7g\2\2\u00af\u00b0\7n\2\2\u00b0")
        buf.write("\u00b1\7u\2\2\u00b1\u00b2\7g\2\2\u00b2\16\3\2\2\2\u00b3")
        buf.write("\u00b4\7u\2\2\u00b4\u00b5\7y\2\2\u00b5\u00b6\7k\2\2\u00b6")
        buf.write("\u00b7\7v\2\2\u00b7\u00b8\7e\2\2\u00b8\u00b9\7j\2\2\u00b9")
        buf.write("\20\3\2\2\2\u00ba\u00bb\7e\2\2\u00bb\u00bc\7c\2\2\u00bc")
        buf.write("\u00bd\7u\2\2\u00bd\u00be\7g\2\2\u00be\22\3\2\2\2\u00bf")
        buf.write("\u00c0\7<\2\2\u00c0\24\3\2\2\2\u00c1\u00c2\7f\2\2\u00c2")
        buf.write("\u00c3\7g\2\2\u00c3\u00c4\7h\2\2\u00c4\u00c5\7c\2\2\u00c5")
        buf.write("\u00c6\7w\2\2\u00c6\u00c7\7n\2\2\u00c7\u00c8\7v\2\2\u00c8")
        buf.write("\26\3\2\2\2\u00c9\u00ca\7h\2\2\u00ca\u00cb\7q\2\2\u00cb")
        buf.write("\u00cc\7t\2\2\u00cc\30\3\2\2\2\u00cd\u00ce\7~\2\2\u00ce")
        buf.write("\32\3\2\2\2\u00cf\u00d0\7y\2\2\u00d0\u00d1\7j\2\2\u00d1")
        buf.write("\u00d2\7k\2\2\u00d2\u00d3\7n\2\2\u00d3\u00d4\7g\2\2\u00d4")
        buf.write("\34\3\2\2\2\u00d5\u00d6\7f\2\2\u00d6\u00d7\7q\2\2\u00d7")
        buf.write("\36\3\2\2\2\u00d8\u00d9\7=\2\2\u00d9 \3\2\2\2\u00da\u00db")
        buf.write("\7v\2\2\u00db\u00dc\7t\2\2\u00dc\u00dd\7{\2\2\u00dd\"")
        buf.write("\3\2\2\2\u00de\u00df\7e\2\2\u00df\u00e0\7c\2\2\u00e0\u00e1")
        buf.write("\7v\2\2\u00e1\u00e2\7e\2\2\u00e2\u00e3\7j\2\2\u00e3$\3")
        buf.write("\2\2\2\u00e4\u00e5\7d\2\2\u00e5\u00e6\7c\2\2\u00e6\u00e7")
        buf.write("\7e\2\2\u00e7\u00e8\7m\2\2\u00e8\u00e9\7v\2\2\u00e9\u00ea")
        buf.write("\7t\2\2\u00ea\u00eb\7c\2\2\u00eb\u00ec\7e\2\2\u00ec\u00ed")
        buf.write("\7m\2\2\u00ed&\3\2\2\2\u00ee\u00ef\7d\2\2\u00ef\u00f0")
        buf.write("\7t\2\2\u00f0\u00f1\7g\2\2\u00f1\u00f2\7c\2\2\u00f2\u00f3")
        buf.write("\7m\2\2\u00f3(\3\2\2\2\u00f4\u00f5\7e\2\2\u00f5\u00f6")
        buf.write("\7q\2\2\u00f6\u00f7\7p\2\2\u00f7\u00f8\7v\2\2\u00f8\u00f9")
        buf.write("\7k\2\2\u00f9\u00fa\7p\2\2\u00fa\u00fb\7w\2\2\u00fb\u00fc")
        buf.write("\7g\2\2\u00fc*\3\2\2\2\u00fd\u00fe\7g\2\2\u00fe\u00ff")
        buf.write("\7z\2\2\u00ff\u0100\7k\2\2\u0100\u0101\7v\2\2\u0101,\3")
        buf.write("\2\2\2\u0102\u0103\7t\2\2\u0103\u0104\7g\2\2\u0104\u0105")
        buf.write("\7v\2\2\u0105\u0106\7w\2\2\u0106\u0107\7t\2\2\u0107\u0108")
        buf.write("\7p\2\2\u0108.\3\2\2\2\u0109\u010a\7c\2\2\u010a\u010b")
        buf.write("\7u\2\2\u010b\u010c\7u\2\2\u010c\u010d\7g\2\2\u010d\u010e")
        buf.write("\7t\2\2\u010e\u010f\7v\2\2\u010f\60\3\2\2\2\u0110\u0111")
        buf.write("\7.\2\2\u0111\62\3\2\2\2\u0112\u0113\7-\2\2\u0113\u0114")
        buf.write("\7?\2\2\u0114\64\3\2\2\2\u0115\u0116\7/\2\2\u0116\u0117")
        buf.write("\7?\2\2\u0117\66\3\2\2\2\u0118\u0119\7,\2\2\u0119\u011a")
        buf.write("\7?\2\2\u011a8\3\2\2\2\u011b\u011c\7\61\2\2\u011c\u011d")
        buf.write("\7?\2\2\u011d:\3\2\2\2\u011e\u011f\7^\2\2\u011f\u0120")
        buf.write("\7?\2\2\u0120<\3\2\2\2\u0121\u0122\7\'\2\2\u0122\u0123")
        buf.write("\7?\2\2\u0123>\3\2\2\2\u0124\u0125\7<\2\2\u0125\u0126")
        buf.write("\7?\2\2\u0126@\3\2\2\2\u0127\u0128\7\60\2\2\u0128B\3\2")
        buf.write("\2\2\u0129\u012a\7]\2\2\u012aD\3\2\2\2\u012b\u012c\7_")
        buf.write("\2\2\u012cF\3\2\2\2\u012d\u012e\7a\2\2\u012eH\3\2\2\2")
        buf.write("\u012f\u0130\7>\2\2\u0130\u0131\7?\2\2\u0131\u0132\7?")
        buf.write("\2\2\u0132\u0133\7@\2\2\u0133J\3\2\2\2\u0134\u0135\7>")
        buf.write("\2\2\u0135\u0136\7#\2\2\u0136\u0137\7?\2\2\u0137\u0138")
        buf.write("\7@\2\2\u0138L\3\2\2\2\u0139\u013a\7~\2\2\u013a\u013b")
        buf.write("\7?\2\2\u013b\u013c\7@\2\2\u013cN\3\2\2\2\u013d\u013e")
        buf.write("\7?\2\2\u013e\u013f\7@\2\2\u013fP\3\2\2\2\u0140\u0141")
        buf.write("\7~\2\2\u0141\u0142\7~\2\2\u0142R\3\2\2\2\u0143\u0144")
        buf.write("\7(\2\2\u0144\u0145\7(\2\2\u0145T\3\2\2\2\u0146\u0147")
        buf.write("\7?\2\2\u0147\u0148\7?\2\2\u0148V\3\2\2\2\u0149\u014a")
        buf.write("\7#\2\2\u014a\u014b\7?\2\2\u014bX\3\2\2\2\u014c\u014d")
        buf.write("\7>\2\2\u014dZ\3\2\2\2\u014e\u014f\7>\2\2\u014f\u0150")
        buf.write("\7?\2\2\u0150\\\3\2\2\2\u0151\u0152\7@\2\2\u0152^\3\2")
        buf.write("\2\2\u0153\u0154\7@\2\2\u0154\u0155\7?\2\2\u0155`\3\2")
        buf.write("\2\2\u0156\u0157\7k\2\2\u0157\u0158\7p\2\2\u0158b\3\2")
        buf.write("\2\2\u0159\u015a\7p\2\2\u015a\u015b\7q\2\2\u015b\u015c")
        buf.write("\7v\2\2\u015c\u015d\7k\2\2\u015d\u015e\7p\2\2\u015ed\3")
        buf.write("\2\2\2\u015f\u0160\7-\2\2\u0160f\3\2\2\2\u0161\u0162\7")
        buf.write("/\2\2\u0162h\3\2\2\2\u0163\u0164\7,\2\2\u0164j\3\2\2\2")
        buf.write("\u0165\u0166\7\61\2\2\u0166l\3\2\2\2\u0167\u0168\7^\2")
        buf.write("\2\u0168n\3\2\2\2\u0169\u016a\7\'\2\2\u016ap\3\2\2\2\u016b")
        buf.write("\u016c\7@\2\2\u016c\u016d\7>\2\2\u016dr\3\2\2\2\u016e")
        buf.write("\u016f\7-\2\2\u016f\u0170\7\61\2\2\u0170t\3\2\2\2\u0171")
        buf.write("\u0172\7,\2\2\u0172\u0173\7\61\2\2\u0173v\3\2\2\2\u0174")
        buf.write("\u0175\7,\2\2\u0175\u0176\7,\2\2\u0176x\3\2\2\2\u0177")
        buf.write("\u0178\7%\2\2\u0178z\3\2\2\2\u0179\u017a\7#\2\2\u017a")
        buf.write("|\3\2\2\2\u017b\u017c\7h\2\2\u017c\u017d\7q\2\2\u017d")
        buf.write("\u017e\7t\2\2\u017e\u017f\7c\2\2\u017f\u0180\7n\2\2\u0180")
        buf.write("\u0181\7n\2\2\u0181~\3\2\2\2\u0182\u0183\7g\2\2\u0183")
        buf.write("\u0184\7z\2\2\u0184\u0185\7k\2\2\u0185\u0186\7u\2\2\u0186")
        buf.write("\u0187\7v\2\2\u0187\u0188\7u\2\2\u0188\u0080\3\2\2\2\u0189")
        buf.write("\u018a\7r\2\2\u018a\u018b\7t\2\2\u018b\u018c\7q\2\2\u018c")
        buf.write("\u018d\7e\2\2\u018d\u018e\7g\2\2\u018e\u018f\7f\2\2\u018f")
        buf.write("\u0190\7w\2\2\u0190\u0191\7t\2\2\u0191\u0192\7g\2\2\u0192")
        buf.write("\u0082\3\2\2\2\u0193\u0194\7e\2\2\u0194\u0195\7c\2\2\u0195")
        buf.write("\u0196\7e\2\2\u0196\u0197\7j\2\2\u0197\u0198\7g\2\2\u0198")
        buf.write("\u0199\7f\2\2\u0199\u019a\7R\2\2\u019a\u019b\7t\2\2\u019b")
        buf.write("\u019c\7q\2\2\u019c\u019d\7e\2\2\u019d\u019e\7g\2\2\u019e")
        buf.write("\u019f\7f\2\2\u019f\u01a0\7w\2\2\u01a0\u01a1\7t\2\2\u01a1")
        buf.write("\u01a2\7g\2\2\u01a2\u0084\3\2\2\2\u01a3\u01a4\7e\2\2\u01a4")
        buf.write("\u01a5\7n\2\2\u01a5\u01a6\7q\2\2\u01a6\u01a7\7u\2\2\u01a7")
        buf.write("\u01a8\7w\2\2\u01a8\u01a9\7t\2\2\u01a9\u01aa\7g\2\2\u01aa")
        buf.write("\u0086\3\2\2\2\u01ab\u01ac\7t\2\2\u01ac\u01ad\7y\2\2\u01ad")
        buf.write("\u0088\3\2\2\2\u01ae\u01af\7q\2\2\u01af\u01b0\7o\2\2\u01b0")
        buf.write("\u008a\3\2\2\2\u01b1\u01b2\7v\2\2\u01b2\u01b3\7t\2\2\u01b3")
        buf.write("\u01b4\7w\2\2\u01b4\u01b5\7g\2\2\u01b5\u008c\3\2\2\2\u01b6")
        buf.write("\u01b7\7h\2\2\u01b7\u01b8\7c\2\2\u01b8\u01b9\7n\2\2\u01b9")
        buf.write("\u01ba\7u\2\2\u01ba\u01bb\7g\2\2\u01bb\u008e\3\2\2\2\u01bc")
        buf.write("\u01c0\t\2\2\2\u01bd\u01bf\t\3\2\2\u01be\u01bd\3\2\2\2")
        buf.write("\u01bf\u01c2\3\2\2\2\u01c0\u01be\3\2\2\2\u01c0\u01c1\3")
        buf.write("\2\2\2\u01c1\u0090\3\2\2\2\u01c2\u01c0\3\2\2\2\u01c3\u01cc")
        buf.write("\7\62\2\2\u01c4\u01c8\4\63;\2\u01c5\u01c7\4\62;\2\u01c6")
        buf.write("\u01c5\3\2\2\2\u01c7\u01ca\3\2\2\2\u01c8\u01c6\3\2\2\2")
        buf.write("\u01c8\u01c9\3\2\2\2\u01c9\u01cc\3\2\2\2\u01ca\u01c8\3")
        buf.write("\2\2\2\u01cb\u01c3\3\2\2\2\u01cb\u01c4\3\2\2\2\u01cc\u0092")
        buf.write("\3\2\2\2\u01cd\u01cf\5\u0091I\2\u01ce\u01cd\3\2\2\2\u01ce")
        buf.write("\u01cf\3\2\2\2\u01cf\u01d0\3\2\2\2\u01d0\u01d2\7\60\2")
        buf.write("\2\u01d1\u01d3\4\62;\2\u01d2\u01d1\3\2\2\2\u01d3\u01d4")
        buf.write("\3\2\2\2\u01d4\u01d2\3\2\2\2\u01d4\u01d5\3\2\2\2\u01d5")
        buf.write("\u01df\3\2\2\2\u01d6\u01d8\t\4\2\2\u01d7\u01d9\t\5\2\2")
        buf.write("\u01d8\u01d7\3\2\2\2\u01d8\u01d9\3\2\2\2\u01d9\u01db\3")
        buf.write("\2\2\2\u01da\u01dc\4\62;\2\u01db\u01da\3\2\2\2\u01dc\u01dd")
        buf.write("\3\2\2\2\u01dd\u01db\3\2\2\2\u01dd\u01de\3\2\2\2\u01de")
        buf.write("\u01e0\3\2\2\2\u01df\u01d6\3\2\2\2\u01df\u01e0\3\2\2\2")
        buf.write("\u01e0\u0094\3\2\2\2\u01e1\u01e2\7\60\2\2\u01e2\u01e3")
        buf.write("\7\60\2\2\u01e3\u0096\3\2\2\2\u01e4\u01ea\7$\2\2\u01e5")
        buf.write("\u01e6\7^\2\2\u01e6\u01e9\13\2\2\2\u01e7\u01e9\n\6\2\2")
        buf.write("\u01e8\u01e5\3\2\2\2\u01e8\u01e7\3\2\2\2\u01e9\u01ec\3")
        buf.write("\2\2\2\u01ea\u01e8\3\2\2\2\u01ea\u01eb\3\2\2\2\u01eb\u01ed")
        buf.write("\3\2\2\2\u01ec\u01ea\3\2\2\2\u01ed\u01ee\7$\2\2\u01ee")
        buf.write("\u0098\3\2\2\2\u01ef\u01f5\7)\2\2\u01f0\u01f1\7)\2\2\u01f1")
        buf.write("\u01f4\7)\2\2\u01f2\u01f4\n\7\2\2\u01f3\u01f0\3\2\2\2")
        buf.write("\u01f3\u01f2\3\2\2\2\u01f4\u01f7\3\2\2\2\u01f5\u01f3\3")
        buf.write("\2\2\2\u01f5\u01f6\3\2\2\2\u01f6\u01f8\3\2\2\2\u01f7\u01f5")
        buf.write("\3\2\2\2\u01f8\u01f9\7)\2\2\u01f9\u009a\3\2\2\2\u01fa")
        buf.write("\u01fb\7\61\2\2\u01fb\u01fc\7\61\2\2\u01fc\u0200\3\2\2")
        buf.write("\2\u01fd\u01ff\n\b\2\2\u01fe\u01fd\3\2\2\2\u01ff\u0202")
        buf.write("\3\2\2\2\u0200\u01fe\3\2\2\2\u0200\u0201\3\2\2\2\u0201")
        buf.write("\u0203\3\2\2\2\u0202\u0200\3\2\2\2\u0203\u0204\bN\2\2")
        buf.write("\u0204\u009c\3\2\2\2\u0205\u0206\7\61\2\2\u0206\u0207")
        buf.write("\7,\2\2\u0207\u0211\3\2\2\2\u0208\u0210\n\t\2\2\u0209")
        buf.write("\u020b\7,\2\2\u020a\u0209\3\2\2\2\u020b\u020c\3\2\2\2")
        buf.write("\u020c\u020a\3\2\2\2\u020c\u020d\3\2\2\2\u020d\u020e\3")
        buf.write("\2\2\2\u020e\u0210\n\n\2\2\u020f\u0208\3\2\2\2\u020f\u020a")
        buf.write("\3\2\2\2\u0210\u0213\3\2\2\2\u0211\u020f\3\2\2\2\u0211")
        buf.write("\u0212\3\2\2\2\u0212\u0215\3\2\2\2\u0213\u0211\3\2\2\2")
        buf.write("\u0214\u0216\7,\2\2\u0215\u0214\3\2\2\2\u0216\u0217\3")
        buf.write("\2\2\2\u0217\u0215\3\2\2\2\u0217\u0218\3\2\2\2\u0218\u0219")
        buf.write("\3\2\2\2\u0219\u021a\7\61\2\2\u021a\u021b\3\2\2\2\u021b")
        buf.write("\u021c\bO\2\2\u021c\u009e\3\2\2\2\u021d\u021f\t\13\2\2")
        buf.write("\u021e\u021d\3\2\2\2\u021f\u0220\3\2\2\2\u0220\u021e\3")
        buf.write("\2\2\2\u0220\u0221\3\2\2\2\u0221\u0222\3\2\2\2\u0222\u0223")
        buf.write("\bP\2\2\u0223\u00a0\3\2\2\2\u0224\u0225\13\2\2\2\u0225")
        buf.write("\u00a2\3\2\2\2\25\2\u01c0\u01c8\u01cb\u01ce\u01d4\u01d8")
        buf.write("\u01dd\u01df\u01e8\u01ea\u01f3\u01f5\u0200\u020c\u020f")
        buf.write("\u0211\u0217\u0220\3\b\2\2")
        return buf.getvalue()


class SetlXgrammarLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    T__0 = 1
    T__1 = 2
    T__2 = 3
    T__3 = 4
    T__4 = 5
    T__5 = 6
    T__6 = 7
    T__7 = 8
    T__8 = 9
    T__9 = 10
    T__10 = 11
    T__11 = 12
    T__12 = 13
    T__13 = 14
    T__14 = 15
    T__15 = 16
    T__16 = 17
    T__17 = 18
    T__18 = 19
    T__19 = 20
    T__20 = 21
    T__21 = 22
    T__22 = 23
    T__23 = 24
    T__24 = 25
    T__25 = 26
    T__26 = 27
    T__27 = 28
    T__28 = 29
    T__29 = 30
    T__30 = 31
    T__31 = 32
    T__32 = 33
    T__33 = 34
    T__34 = 35
    T__35 = 36
    T__36 = 37
    T__37 = 38
    T__38 = 39
    T__39 = 40
    T__40 = 41
    T__41 = 42
    T__42 = 43
    T__43 = 44
    T__44 = 45
    T__45 = 46
    T__46 = 47
    T__47 = 48
    T__48 = 49
    T__49 = 50
    T__50 = 51
    T__51 = 52
    T__52 = 53
    T__53 = 54
    T__54 = 55
    T__55 = 56
    T__56 = 57
    T__57 = 58
    T__58 = 59
    T__59 = 60
    T__60 = 61
    T__61 = 62
    T__62 = 63
    T__63 = 64
    T__64 = 65
    T__65 = 66
    T__66 = 67
    T__67 = 68
    T__68 = 69
    T__69 = 70
    ID = 71
    NUMBER = 72
    DOUBLE = 73
    RANGE_SIGN = 74
    STRING = 75
    LITERAL = 76
    LINE_COMMENT = 77
    MULTI_COMMENT = 78
    WS = 79
    REMAINDER = 80

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'if'", "'('", "')'", "'{'", "'}'", "'else'", "'switch'", "'case'", 
            "':'", "'default'", "'for'", "'|'", "'while'", "'do'", "';'", 
            "'try'", "'catch'", "'backtrack'", "'break'", "'continue'", 
            "'exit'", "'return'", "'assert'", "','", "'+='", "'-='", "'*='", 
            "'/='", "'\\='", "'%='", "':='", "'.'", "'['", "']'", "'_'", 
            "'<==>'", "'<!=>'", "'|=>'", "'=>'", "'||'", "'&&'", "'=='", 
            "'!='", "'<'", "'<='", "'>'", "'>='", "'in'", "'notin'", "'+'", 
            "'-'", "'*'", "'/'", "'\\'", "'%'", "'><'", "'+/'", "'*/'", 
            "'**'", "'#'", "'!'", "'forall'", "'exists'", "'procedure'", 
            "'cachedProcedure'", "'closure'", "'rw'", "'om'", "'true'", 
            "'false'", "'..'" ]

    symbolicNames = [ "<INVALID>",
            "ID", "NUMBER", "DOUBLE", "RANGE_SIGN", "STRING", "LITERAL", 
            "LINE_COMMENT", "MULTI_COMMENT", "WS", "REMAINDER" ]

    ruleNames = [ "T__0", "T__1", "T__2", "T__3", "T__4", "T__5", "T__6", 
                  "T__7", "T__8", "T__9", "T__10", "T__11", "T__12", "T__13", 
                  "T__14", "T__15", "T__16", "T__17", "T__18", "T__19", 
                  "T__20", "T__21", "T__22", "T__23", "T__24", "T__25", 
                  "T__26", "T__27", "T__28", "T__29", "T__30", "T__31", 
                  "T__32", "T__33", "T__34", "T__35", "T__36", "T__37", 
                  "T__38", "T__39", "T__40", "T__41", "T__42", "T__43", 
                  "T__44", "T__45", "T__46", "T__47", "T__48", "T__49", 
                  "T__50", "T__51", "T__52", "T__53", "T__54", "T__55", 
                  "T__56", "T__57", "T__58", "T__59", "T__60", "T__61", 
                  "T__62", "T__63", "T__64", "T__65", "T__66", "T__67", 
                  "T__68", "T__69", "ID", "NUMBER", "DOUBLE", "RANGE_SIGN", 
                  "STRING", "LITERAL", "LINE_COMMENT", "MULTI_COMMENT", 
                  "WS", "REMAINDER" ]

    grammarFileName = "SetlXgrammar.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.7.1")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


