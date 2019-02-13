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
        buf.write("\u0349\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31")
        buf.write("\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36")
        buf.write("\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%\3\2\3")
        buf.write("\2\3\2\7\2N\n\2\f\2\16\2Q\13\2\3\2\3\2\3\3\3\3\3\3\3\3")
        buf.write("\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\7")
        buf.write("\3f\n\3\f\3\16\3i\13\3\3\3\3\3\3\3\3\3\3\3\3\3\5\3q\n")
        buf.write("\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\7\3}\n\3\f")
        buf.write("\3\16\3\u0080\13\3\3\3\3\3\3\3\5\3\u0085\n\3\3\3\3\3\3")
        buf.write("\3\3\3\3\3\3\3\3\3\3\3\3\3\5\3\u0090\n\3\3\3\3\3\3\3\3")
        buf.write("\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3")
        buf.write("\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3")
        buf.write("\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\5\3\u00b9\n\3\3\3\3")
        buf.write("\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3")
        buf.write("\3\3\3\3\3\3\5\3\u00cd\n\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3")
        buf.write("\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3")
        buf.write("\3\3\3\3\3\5\3\u00e6\n\3\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3")
        buf.write("\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4")
        buf.write("\3\4\3\4\3\4\3\4\5\4\u0101\n\4\3\5\3\5\3\5\3\5\3\5\3\5")
        buf.write("\3\5\3\5\3\5\3\5\3\5\3\5\3\5\5\5\u0110\n\5\5\5\u0112\n")
        buf.write("\5\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\7\6\u011f")
        buf.write("\n\6\f\6\16\6\u0122\13\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3")
        buf.write("\6\5\6\u012c\n\6\3\7\3\7\3\7\3\b\3\b\3\b\3\t\3\t\3\t\3")
        buf.write("\t\3\t\3\t\7\t\u013a\n\t\f\t\16\t\u013d\13\t\3\n\3\n\3")
        buf.write("\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n\5\n\u014c\n")
        buf.write("\n\5\n\u014e\n\n\3\13\3\13\3\13\3\13\3\13\3\f\3\f\3\f")
        buf.write("\3\f\3\f\3\f\3\f\3\f\3\f\3\f\7\f\u015f\n\f\f\f\16\f\u0162")
        buf.write("\13\f\5\f\u0164\n\f\3\f\5\f\u0167\n\f\3\r\3\r\3\r\3\r")
        buf.write("\3\r\3\r\5\r\u016f\n\r\3\16\3\16\3\16\3\16\3\16\3\16\7")
        buf.write("\16\u0177\n\16\f\16\16\16\u017a\13\16\3\17\3\17\3\17\3")
        buf.write("\17\3\17\3\17\7\17\u0182\n\17\f\17\16\17\u0185\13\17\3")
        buf.write("\20\3\20\3\20\3\20\3\20\3\20\3\20\3\20\3\20\3\20\3\20")
        buf.write("\3\20\3\20\3\20\3\20\3\20\3\20\3\20\3\20\3\20\3\20\3\20")
        buf.write("\3\20\3\20\3\20\3\20\3\20\3\20\3\20\3\20\3\20\3\20\3\20")
        buf.write("\3\20\5\20\u01a9\n\20\3\21\3\21\3\21\3\21\3\21\3\21\3")
        buf.write("\21\3\21\3\21\3\21\7\21\u01b5\n\21\f\21\16\21\u01b8\13")
        buf.write("\21\3\22\3\22\3\22\3\22\3\22\3\22\3\22\3\22\3\22\3\22")
        buf.write("\3\22\3\22\3\22\3\22\3\22\3\22\3\22\3\22\3\22\3\22\3\22")
        buf.write("\3\22\7\22\u01d0\n\22\f\22\16\22\u01d3\13\22\3\23\3\23")
        buf.write("\3\23\3\23\3\23\3\23\3\23\3\23\3\23\3\23\7\23\u01df\n")
        buf.write("\23\f\23\16\23\u01e2\13\23\3\24\3\24\3\24\3\24\3\24\3")
        buf.write("\24\5\24\u01ea\n\24\3\24\3\24\3\24\3\24\3\24\3\24\3\24")
        buf.write("\3\24\3\24\3\24\3\24\3\24\3\24\3\24\3\24\3\24\5\24\u01fc")
        buf.write("\n\24\3\25\3\25\3\25\3\25\3\25\3\25\3\25\3\25\3\25\3\25")
        buf.write("\3\25\3\25\3\25\3\25\3\25\3\25\3\25\3\25\3\25\3\25\3\25")
        buf.write("\3\25\3\25\3\25\3\25\3\25\3\25\3\25\3\25\3\25\3\25\5\25")
        buf.write("\u021d\n\25\3\25\3\25\3\25\3\25\3\25\3\25\3\25\7\25\u0226")
        buf.write("\n\25\f\25\16\25\u0229\13\25\3\25\3\25\5\25\u022d\n\25")
        buf.write("\3\25\3\25\3\25\3\25\5\25\u0233\n\25\5\25\u0235\n\25\3")
        buf.write("\26\3\26\3\26\3\26\3\26\3\26\3\26\3\26\3\26\3\26\3\26")
        buf.write("\3\26\3\26\3\26\3\26\3\26\3\26\3\26\3\26\3\26\3\26\3\26")
        buf.write("\3\26\3\26\3\26\3\26\3\26\5\26\u0252\n\26\3\27\3\27\3")
        buf.write("\27\3\27\3\27\3\27\7\27\u025a\n\27\f\27\16\27\u025d\13")
        buf.write("\27\3\27\3\27\3\27\3\27\7\27\u0263\n\27\f\27\16\27\u0266")
        buf.write("\13\27\3\27\3\27\3\27\3\27\5\27\u026c\n\27\3\27\3\27\3")
        buf.write("\27\3\27\3\27\3\27\7\27\u0274\n\27\f\27\16\27\u0277\13")
        buf.write("\27\3\27\3\27\3\27\3\27\5\27\u027d\n\27\3\27\3\27\3\27")
        buf.write("\3\27\5\27\u0283\n\27\3\30\3\30\3\30\3\30\3\30\3\30\3")
        buf.write("\30\3\30\5\30\u028d\n\30\3\31\3\31\3\31\3\31\3\31\3\32")
        buf.write("\3\32\3\32\3\32\3\33\3\33\3\33\3\33\3\33\3\33\3\33\3\33")
        buf.write("\3\33\3\33\5\33\u02a2\n\33\3\34\3\34\3\34\3\34\3\34\3")
        buf.write("\34\5\34\u02aa\n\34\3\34\3\34\3\34\3\34\6\34\u02b0\n\34")
        buf.write("\r\34\16\34\u02b1\3\34\3\34\3\34\5\34\u02b7\n\34\3\34")
        buf.write("\3\34\3\34\3\34\5\34\u02bd\n\34\3\35\3\35\3\35\3\35\3")
        buf.write("\35\3\35\3\35\5\35\u02c6\n\35\3\35\3\35\3\35\3\35\3\35")
        buf.write("\5\35\u02cd\n\35\3\36\3\36\3\36\3\36\5\36\u02d3\n\36\3")
        buf.write("\36\3\36\3\36\3\36\3\36\3\36\5\36\u02db\n\36\3\36\3\36")
        buf.write("\3\36\3\36\3\36\3\36\3\36\3\36\3\36\3\36\3\36\3\36\5\36")
        buf.write("\u02e9\n\36\3\37\3\37\3\37\3\37\3\37\3\37\3\37\3\37\3")
        buf.write("\37\3\37\3\37\3\37\7\37\u02f7\n\37\f\37\16\37\u02fa\13")
        buf.write("\37\3\37\3\37\3\37\3\37\3\37\5\37\u0301\n\37\5\37\u0303")
        buf.write("\n\37\3\37\3\37\3\37\3\37\3\37\3\37\3\37\3\37\3\37\3\37")
        buf.write("\5\37\u030f\n\37\3\37\3\37\3\37\3\37\3\37\3\37\3\37\5")
        buf.write("\37\u0318\n\37\5\37\u031a\n\37\3 \3 \3 \3 \3 \3 \7 \u0322")
        buf.write("\n \f \16 \u0325\13 \3!\3!\3!\3!\3!\3\"\3\"\3\"\3\"\3")
        buf.write("\"\3\"\3\"\3\"\3\"\3\"\5\"\u0336\n\"\3#\3#\3#\3$\3$\3")
        buf.write("$\3%\3%\3%\3%\3%\3%\7%\u0344\n%\f%\16%\u0347\13%\3%\2")
        buf.write("\2&\2\4\6\b\n\f\16\20\22\24\26\30\32\34\36 \"$&(*,.\60")
        buf.write("\62\64\668:<>@BDFH\2\2\2\u0398\2O\3\2\2\2\4\u00e5\3\2")
        buf.write("\2\2\6\u00e7\3\2\2\2\b\u0111\3\2\2\2\n\u012b\3\2\2\2\f")
        buf.write("\u012d\3\2\2\2\16\u0130\3\2\2\2\20\u0133\3\2\2\2\22\u014d")
        buf.write("\3\2\2\2\24\u014f\3\2\2\2\26\u0166\3\2\2\2\30\u0168\3")
        buf.write("\2\2\2\32\u0170\3\2\2\2\34\u017b\3\2\2\2\36\u0186\3\2")
        buf.write("\2\2 \u01aa\3\2\2\2\"\u01b9\3\2\2\2$\u01d4\3\2\2\2&\u01fb")
        buf.write("\3\2\2\2(\u0234\3\2\2\2*\u0251\3\2\2\2,\u0282\3\2\2\2")
        buf.write(".\u028c\3\2\2\2\60\u028e\3\2\2\2\62\u0293\3\2\2\2\64\u02a1")
        buf.write("\3\2\2\2\66\u02bc\3\2\2\28\u02cc\3\2\2\2:\u02e8\3\2\2")
        buf.write("\2<\u02ea\3\2\2\2>\u031b\3\2\2\2@\u0326\3\2\2\2B\u0335")
        buf.write("\3\2\2\2D\u0337\3\2\2\2F\u033a\3\2\2\2H\u033d\3\2\2\2")
        buf.write("JK\5\4\3\2KL\b\2\1\2LN\3\2\2\2MJ\3\2\2\2NQ\3\2\2\2OM\3")
        buf.write("\2\2\2OP\3\2\2\2PR\3\2\2\2QO\3\2\2\2RS\b\2\1\2S\3\3\2")
        buf.write("\2\2TU\7\3\2\2UV\7\4\2\2VW\5F$\2WX\7\5\2\2XY\7\6\2\2Y")
        buf.write("Z\5\2\2\2Zg\7\7\2\2[\\\7\b\2\2\\]\7\3\2\2]^\7\4\2\2^_")
        buf.write("\5F$\2_`\7\5\2\2`a\7\6\2\2ab\5\2\2\2bc\7\7\2\2cd\b\3\1")
        buf.write("\2df\3\2\2\2e[\3\2\2\2fi\3\2\2\2ge\3\2\2\2gh\3\2\2\2h")
        buf.write("p\3\2\2\2ig\3\2\2\2jk\7\b\2\2kl\7\6\2\2lm\5\2\2\2mn\7")
        buf.write("\7\2\2no\b\3\1\2oq\3\2\2\2pj\3\2\2\2pq\3\2\2\2qr\3\2\2")
        buf.write("\2rs\b\3\1\2s\u00e6\3\2\2\2tu\7\t\2\2u~\7\6\2\2vw\7\n")
        buf.write("\2\2wx\5F$\2xy\7\13\2\2yz\5\2\2\2z{\b\3\1\2{}\3\2\2\2")
        buf.write("|v\3\2\2\2}\u0080\3\2\2\2~|\3\2\2\2~\177\3\2\2\2\177\u0084")
        buf.write("\3\2\2\2\u0080~\3\2\2\2\u0081\u0082\7\f\2\2\u0082\u0083")
        buf.write("\7\13\2\2\u0083\u0085\5\2\2\2\u0084\u0081\3\2\2\2\u0084")
        buf.write("\u0085\3\2\2\2\u0085\u0086\3\2\2\2\u0086\u0087\7\7\2\2")
        buf.write("\u0087\u00e6\b\3\1\2\u0088\u0089\7\r\2\2\u0089\u008a\7")
        buf.write("\4\2\2\u008a\u008f\5> \2\u008b\u008c\7\16\2\2\u008c\u008d")
        buf.write("\5F$\2\u008d\u008e\b\3\1\2\u008e\u0090\3\2\2\2\u008f\u008b")
        buf.write("\3\2\2\2\u008f\u0090\3\2\2\2\u0090\u0091\3\2\2\2\u0091")
        buf.write("\u0092\7\5\2\2\u0092\u0093\7\6\2\2\u0093\u0094\5\2\2\2")
        buf.write("\u0094\u0095\7\7\2\2\u0095\u0096\b\3\1\2\u0096\u00e6\3")
        buf.write("\2\2\2\u0097\u0098\7\17\2\2\u0098\u0099\7\4\2\2\u0099")
        buf.write("\u009a\5F$\2\u009a\u009b\7\5\2\2\u009b\u009c\7\6\2\2\u009c")
        buf.write("\u009d\5\2\2\2\u009d\u009e\7\7\2\2\u009e\u009f\b\3\1\2")
        buf.write("\u009f\u00e6\3\2\2\2\u00a0\u00a1\7\20\2\2\u00a1\u00a2")
        buf.write("\7\6\2\2\u00a2\u00a3\5\2\2\2\u00a3\u00a4\7\7\2\2\u00a4")
        buf.write("\u00a5\7\17\2\2\u00a5\u00a6\7\4\2\2\u00a6\u00a7\5F$\2")
        buf.write("\u00a7\u00a8\7\5\2\2\u00a8\u00a9\7\21\2\2\u00a9\u00aa")
        buf.write("\b\3\1\2\u00aa\u00e6\3\2\2\2\u00ab\u00ac\7\22\2\2\u00ac")
        buf.write("\u00ad\7\6\2\2\u00ad\u00ae\5\2\2\2\u00ae\u00b8\7\7\2\2")
        buf.write("\u00af\u00b0\7\23\2\2\u00b0\u00b1\7\4\2\2\u00b1\u00b2")
        buf.write("\5\f\7\2\u00b2\u00b3\7\5\2\2\u00b3\u00b4\7\6\2\2\u00b4")
        buf.write("\u00b5\5\2\2\2\u00b5\u00b6\7\7\2\2\u00b6\u00b7\b\3\1\2")
        buf.write("\u00b7\u00b9\3\2\2\2\u00b8\u00af\3\2\2\2\u00b8\u00b9\3")
        buf.write("\2\2\2\u00b9\u00ba\3\2\2\2\u00ba\u00bb\b\3\1\2\u00bb\u00e6")
        buf.write("\3\2\2\2\u00bc\u00bd\7\24\2\2\u00bd\u00be\7\21\2\2\u00be")
        buf.write("\u00e6\b\3\1\2\u00bf\u00c0\7\25\2\2\u00c0\u00c1\7\21\2")
        buf.write("\2\u00c1\u00e6\b\3\1\2\u00c2\u00c3\7\26\2\2\u00c3\u00c4")
        buf.write("\7\21\2\2\u00c4\u00e6\b\3\1\2\u00c5\u00c6\7\27\2\2\u00c6")
        buf.write("\u00c7\7\21\2\2\u00c7\u00e6\b\3\1\2\u00c8\u00cc\7\30\2")
        buf.write("\2\u00c9\u00ca\5\16\b\2\u00ca\u00cb\b\3\1\2\u00cb\u00cd")
        buf.write("\3\2\2\2\u00cc\u00c9\3\2\2\2\u00cc\u00cd\3\2\2\2\u00cd")
        buf.write("\u00ce\3\2\2\2\u00ce\u00cf\7\21\2\2\u00cf\u00e6\b\3\1")
        buf.write("\2\u00d0\u00d1\7\31\2\2\u00d1\u00d2\7\4\2\2\u00d2\u00d3")
        buf.write("\5F$\2\u00d3\u00d4\7\32\2\2\u00d4\u00d5\5\16\b\2\u00d5")
        buf.write("\u00d6\7\5\2\2\u00d6\u00d7\7\21\2\2\u00d7\u00d8\b\3\1")
        buf.write("\2\u00d8\u00e6\3\2\2\2\u00d9\u00da\5\6\4\2\u00da\u00db")
        buf.write("\7\21\2\2\u00db\u00dc\b\3\1\2\u00dc\u00e6\3\2\2\2\u00dd")
        buf.write("\u00de\5\b\5\2\u00de\u00df\7\21\2\2\u00df\u00e0\b\3\1")
        buf.write("\2\u00e0\u00e6\3\2\2\2\u00e1\u00e2\5\16\b\2\u00e2\u00e3")
        buf.write("\7\21\2\2\u00e3\u00e4\b\3\1\2\u00e4\u00e6\3\2\2\2\u00e5")
        buf.write("T\3\2\2\2\u00e5t\3\2\2\2\u00e5\u0088\3\2\2\2\u00e5\u0097")
        buf.write("\3\2\2\2\u00e5\u00a0\3\2\2\2\u00e5\u00ab\3\2\2\2\u00e5")
        buf.write("\u00bc\3\2\2\2\u00e5\u00bf\3\2\2\2\u00e5\u00c2\3\2\2\2")
        buf.write("\u00e5\u00c5\3\2\2\2\u00e5\u00c8\3\2\2\2\u00e5\u00d0\3")
        buf.write("\2\2\2\u00e5\u00d9\3\2\2\2\u00e5\u00dd\3\2\2\2\u00e5\u00e1")
        buf.write("\3\2\2\2\u00e6\5\3\2\2\2\u00e7\u0100\5\n\6\2\u00e8\u00e9")
        buf.write("\7\33\2\2\u00e9\u00ea\5\16\b\2\u00ea\u00eb\b\4\1\2\u00eb")
        buf.write("\u0101\3\2\2\2\u00ec\u00ed\7\34\2\2\u00ed\u00ee\5\16\b")
        buf.write("\2\u00ee\u00ef\b\4\1\2\u00ef\u0101\3\2\2\2\u00f0\u00f1")
        buf.write("\7\35\2\2\u00f1\u00f2\5\16\b\2\u00f2\u00f3\b\4\1\2\u00f3")
        buf.write("\u0101\3\2\2\2\u00f4\u00f5\7\36\2\2\u00f5\u00f6\5\16\b")
        buf.write("\2\u00f6\u00f7\b\4\1\2\u00f7\u0101\3\2\2\2\u00f8\u00f9")
        buf.write("\7\37\2\2\u00f9\u00fa\5\16\b\2\u00fa\u00fb\b\4\1\2\u00fb")
        buf.write("\u0101\3\2\2\2\u00fc\u00fd\7 \2\2\u00fd\u00fe\5\16\b\2")
        buf.write("\u00fe\u00ff\b\4\1\2\u00ff\u0101\3\2\2\2\u0100\u00e8\3")
        buf.write("\2\2\2\u0100\u00ec\3\2\2\2\u0100\u00f0\3\2\2\2\u0100\u00f4")
        buf.write("\3\2\2\2\u0100\u00f8\3\2\2\2\u0100\u00fc\3\2\2\2\u0101")
        buf.write("\7\3\2\2\2\u0102\u0103\5D#\2\u0103\u0104\7!\2\2\u0104")
        buf.write("\u0105\5*\26\2\u0105\u0106\b\5\1\2\u0106\u0112\3\2\2\2")
        buf.write("\u0107\u0108\5\n\6\2\u0108\u010f\7!\2\2\u0109\u010a\5")
        buf.write("\b\5\2\u010a\u010b\b\5\1\2\u010b\u0110\3\2\2\2\u010c\u010d")
        buf.write("\5\22\n\2\u010d\u010e\b\5\1\2\u010e\u0110\3\2\2\2\u010f")
        buf.write("\u0109\3\2\2\2\u010f\u010c\3\2\2\2\u0110\u0112\3\2\2\2")
        buf.write("\u0111\u0102\3\2\2\2\u0111\u0107\3\2\2\2\u0112\t\3\2\2")
        buf.write("\2\u0113\u0114\5\f\7\2\u0114\u0120\b\6\1\2\u0115\u0116")
        buf.write("\7\"\2\2\u0116\u0117\5D#\2\u0117\u0118\b\6\1\2\u0118\u011f")
        buf.write("\3\2\2\2\u0119\u011a\7#\2\2\u011a\u011b\5\20\t\2\u011b")
        buf.write("\u011c\7$\2\2\u011c\u011d\b\6\1\2\u011d\u011f\3\2\2\2")
        buf.write("\u011e\u0115\3\2\2\2\u011e\u0119\3\2\2\2\u011f\u0122\3")
        buf.write("\2\2\2\u0120\u011e\3\2\2\2\u0120\u0121\3\2\2\2\u0121\u012c")
        buf.write("\3\2\2\2\u0122\u0120\3\2\2\2\u0123\u0124\7#\2\2\u0124")
        buf.write("\u0125\5H%\2\u0125\u0126\7$\2\2\u0126\u0127\b\6\1\2\u0127")
        buf.write("\u012c\3\2\2\2\u0128\u0129\6\6\2\3\u0129\u012a\7%\2\2")
        buf.write("\u012a\u012c\b\6\1\2\u012b\u0113\3\2\2\2\u012b\u0123\3")
        buf.write("\2\2\2\u012b\u0128\3\2\2\2\u012c\13\3\2\2\2\u012d\u012e")
        buf.write("\7I\2\2\u012e\u012f\b\7\1\2\u012f\r\3\2\2\2\u0130\u0131")
        buf.write("\5\22\n\2\u0131\u0132\b\b\1\2\u0132\17\3\2\2\2\u0133\u0134")
        buf.write("\5\22\n\2\u0134\u013b\b\t\1\2\u0135\u0136\7\32\2\2\u0136")
        buf.write("\u0137\5\22\n\2\u0137\u0138\b\t\1\2\u0138\u013a\3\2\2")
        buf.write("\2\u0139\u0135\3\2\2\2\u013a\u013d\3\2\2\2\u013b\u0139")
        buf.write("\3\2\2\2\u013b\u013c\3\2\2\2\u013c\21\3\2\2\2\u013d\u013b")
        buf.write("\3\2\2\2\u013e\u013f\5\24\13\2\u013f\u0140\b\n\1\2\u0140")
        buf.write("\u014e\3\2\2\2\u0141\u0142\5\30\r\2\u0142\u014b\b\n\1")
        buf.write("\2\u0143\u0144\7&\2\2\u0144\u0145\5\30\r\2\u0145\u0146")
        buf.write("\b\n\1\2\u0146\u014c\3\2\2\2\u0147\u0148\7\'\2\2\u0148")
        buf.write("\u0149\5\30\r\2\u0149\u014a\b\n\1\2\u014a\u014c\3\2\2")
        buf.write("\2\u014b\u0143\3\2\2\2\u014b\u0147\3\2\2\2\u014b\u014c")
        buf.write("\3\2\2\2\u014c\u014e\3\2\2\2\u014d\u013e\3\2\2\2\u014d")
        buf.write("\u0141\3\2\2\2\u014e\23\3\2\2\2\u014f\u0150\5\26\f\2\u0150")
        buf.write("\u0151\7(\2\2\u0151\u0152\5\16\b\2\u0152\u0153\b\13\1")
        buf.write("\2\u0153\25\3\2\2\2\u0154\u0155\5D#\2\u0155\u0156\b\f")
        buf.write("\1\2\u0156\u0167\3\2\2\2\u0157\u0163\7#\2\2\u0158\u0159")
        buf.write("\5D#\2\u0159\u0160\b\f\1\2\u015a\u015b\7\32\2\2\u015b")
        buf.write("\u015c\5D#\2\u015c\u015d\b\f\1\2\u015d\u015f\3\2\2\2\u015e")
        buf.write("\u015a\3\2\2\2\u015f\u0162\3\2\2\2\u0160\u015e\3\2\2\2")
        buf.write("\u0160\u0161\3\2\2\2\u0161\u0164\3\2\2\2\u0162\u0160\3")
        buf.write("\2\2\2\u0163\u0158\3\2\2\2\u0163\u0164\3\2\2\2\u0164\u0165")
        buf.write("\3\2\2\2\u0165\u0167\7$\2\2\u0166\u0154\3\2\2\2\u0166")
        buf.write("\u0157\3\2\2\2\u0167\27\3\2\2\2\u0168\u0169\5\32\16\2")
        buf.write("\u0169\u016e\b\r\1\2\u016a\u016b\7)\2\2\u016b\u016c\5")
        buf.write("\30\r\2\u016c\u016d\b\r\1\2\u016d\u016f\3\2\2\2\u016e")
        buf.write("\u016a\3\2\2\2\u016e\u016f\3\2\2\2\u016f\31\3\2\2\2\u0170")
        buf.write("\u0171\5\34\17\2\u0171\u0178\b\16\1\2\u0172\u0173\7*\2")
        buf.write("\2\u0173\u0174\5\34\17\2\u0174\u0175\b\16\1\2\u0175\u0177")
        buf.write("\3\2\2\2\u0176\u0172\3\2\2\2\u0177\u017a\3\2\2\2\u0178")
        buf.write("\u0176\3\2\2\2\u0178\u0179\3\2\2\2\u0179\33\3\2\2\2\u017a")
        buf.write("\u0178\3\2\2\2\u017b\u017c\5\36\20\2\u017c\u0183\b\17")
        buf.write("\1\2\u017d\u017e\7+\2\2\u017e\u017f\5\36\20\2\u017f\u0180")
        buf.write("\b\17\1\2\u0180\u0182\3\2\2\2\u0181\u017d\3\2\2\2\u0182")
        buf.write("\u0185\3\2\2\2\u0183\u0181\3\2\2\2\u0183\u0184\3\2\2\2")
        buf.write("\u0184\35\3\2\2\2\u0185\u0183\3\2\2\2\u0186\u0187\5 \21")
        buf.write("\2\u0187\u01a8\b\20\1\2\u0188\u0189\7,\2\2\u0189\u018a")
        buf.write("\5 \21\2\u018a\u018b\b\20\1\2\u018b\u01a9\3\2\2\2\u018c")
        buf.write("\u018d\7-\2\2\u018d\u018e\5 \21\2\u018e\u018f\b\20\1\2")
        buf.write("\u018f\u01a9\3\2\2\2\u0190\u0191\7.\2\2\u0191\u0192\5")
        buf.write(" \21\2\u0192\u0193\b\20\1\2\u0193\u01a9\3\2\2\2\u0194")
        buf.write("\u0195\7/\2\2\u0195\u0196\5 \21\2\u0196\u0197\b\20\1\2")
        buf.write("\u0197\u01a9\3\2\2\2\u0198\u0199\7\60\2\2\u0199\u019a")
        buf.write("\5 \21\2\u019a\u019b\b\20\1\2\u019b\u01a9\3\2\2\2\u019c")
        buf.write("\u019d\7\61\2\2\u019d\u019e\5 \21\2\u019e\u019f\b\20\1")
        buf.write("\2\u019f\u01a9\3\2\2\2\u01a0\u01a1\7\62\2\2\u01a1\u01a2")
        buf.write("\5 \21\2\u01a2\u01a3\b\20\1\2\u01a3\u01a9\3\2\2\2\u01a4")
        buf.write("\u01a5\7\63\2\2\u01a5\u01a6\5 \21\2\u01a6\u01a7\b\20\1")
        buf.write("\2\u01a7\u01a9\3\2\2\2\u01a8\u0188\3\2\2\2\u01a8\u018c")
        buf.write("\3\2\2\2\u01a8\u0190\3\2\2\2\u01a8\u0194\3\2\2\2\u01a8")
        buf.write("\u0198\3\2\2\2\u01a8\u019c\3\2\2\2\u01a8\u01a0\3\2\2\2")
        buf.write("\u01a8\u01a4\3\2\2\2\u01a8\u01a9\3\2\2\2\u01a9\37\3\2")
        buf.write("\2\2\u01aa\u01ab\5\"\22\2\u01ab\u01b6\b\21\1\2\u01ac\u01ad")
        buf.write("\7\64\2\2\u01ad\u01ae\5\"\22\2\u01ae\u01af\b\21\1\2\u01af")
        buf.write("\u01b5\3\2\2\2\u01b0\u01b1\7\65\2\2\u01b1\u01b2\5\"\22")
        buf.write("\2\u01b2\u01b3\b\21\1\2\u01b3\u01b5\3\2\2\2\u01b4\u01ac")
        buf.write("\3\2\2\2\u01b4\u01b0\3\2\2\2\u01b5\u01b8\3\2\2\2\u01b6")
        buf.write("\u01b4\3\2\2\2\u01b6\u01b7\3\2\2\2\u01b7!\3\2\2\2\u01b8")
        buf.write("\u01b6\3\2\2\2\u01b9\u01ba\5$\23\2\u01ba\u01d1\b\22\1")
        buf.write("\2\u01bb\u01bc\7\66\2\2\u01bc\u01bd\5$\23\2\u01bd\u01be")
        buf.write("\b\22\1\2\u01be\u01d0\3\2\2\2\u01bf\u01c0\7\67\2\2\u01c0")
        buf.write("\u01c1\5$\23\2\u01c1\u01c2\b\22\1\2\u01c2\u01d0\3\2\2")
        buf.write("\2\u01c3\u01c4\78\2\2\u01c4\u01c5\5$\23\2\u01c5\u01c6")
        buf.write("\b\22\1\2\u01c6\u01d0\3\2\2\2\u01c7\u01c8\79\2\2\u01c8")
        buf.write("\u01c9\5$\23\2\u01c9\u01ca\b\22\1\2\u01ca\u01d0\3\2\2")
        buf.write("\2\u01cb\u01cc\7:\2\2\u01cc\u01cd\5$\23\2\u01cd\u01ce")
        buf.write("\b\22\1\2\u01ce\u01d0\3\2\2\2\u01cf\u01bb\3\2\2\2\u01cf")
        buf.write("\u01bf\3\2\2\2\u01cf\u01c3\3\2\2\2\u01cf\u01c7\3\2\2\2")
        buf.write("\u01cf\u01cb\3\2\2\2\u01d0\u01d3\3\2\2\2\u01d1\u01cf\3")
        buf.write("\2\2\2\u01d1\u01d2\3\2\2\2\u01d2#\3\2\2\2\u01d3\u01d1")
        buf.write("\3\2\2\2\u01d4\u01d5\5&\24\2\u01d5\u01e0\b\23\1\2\u01d6")
        buf.write("\u01d7\7;\2\2\u01d7\u01d8\5&\24\2\u01d8\u01d9\b\23\1\2")
        buf.write("\u01d9\u01df\3\2\2\2\u01da\u01db\7<\2\2\u01db\u01dc\5")
        buf.write("&\24\2\u01dc\u01dd\b\23\1\2\u01dd\u01df\3\2\2\2\u01de")
        buf.write("\u01d6\3\2\2\2\u01de\u01da\3\2\2\2\u01df\u01e2\3\2\2\2")
        buf.write("\u01e0\u01de\3\2\2\2\u01e0\u01e1\3\2\2\2\u01e1%\3\2\2")
        buf.write("\2\u01e2\u01e0\3\2\2\2\u01e3\u01e4\5(\25\2\u01e4\u01e9")
        buf.write("\b\24\1\2\u01e5\u01e6\7=\2\2\u01e6\u01e7\5&\24\2\u01e7")
        buf.write("\u01e8\b\24\1\2\u01e8\u01ea\3\2\2\2\u01e9\u01e5\3\2\2")
        buf.write("\2\u01e9\u01ea\3\2\2\2\u01ea\u01fc\3\2\2\2\u01eb\u01ec")
        buf.write("\7;\2\2\u01ec\u01ed\5&\24\2\u01ed\u01ee\b\24\1\2\u01ee")
        buf.write("\u01fc\3\2\2\2\u01ef\u01f0\7<\2\2\u01f0\u01f1\5&\24\2")
        buf.write("\u01f1\u01f2\b\24\1\2\u01f2\u01fc\3\2\2\2\u01f3\u01f4")
        buf.write("\7>\2\2\u01f4\u01f5\5&\24\2\u01f5\u01f6\b\24\1\2\u01f6")
        buf.write("\u01fc\3\2\2\2\u01f7\u01f8\7\65\2\2\u01f8\u01f9\5&\24")
        buf.write("\2\u01f9\u01fa\b\24\1\2\u01fa\u01fc\3\2\2\2\u01fb\u01e3")
        buf.write("\3\2\2\2\u01fb\u01eb\3\2\2\2\u01fb\u01ef\3\2\2\2\u01fb")
        buf.write("\u01f3\3\2\2\2\u01fb\u01f7\3\2\2\2\u01fc\'\3\2\2\2\u01fd")
        buf.write("\u01fe\7?\2\2\u01fe\u01ff\5(\25\2\u01ff\u0200\b\25\1\2")
        buf.write("\u0200\u0235\3\2\2\2\u0201\u0202\7@\2\2\u0202\u0203\7")
        buf.write("\4\2\2\u0203\u0204\5> \2\u0204\u0205\7\16\2\2\u0205\u0206")
        buf.write("\5F$\2\u0206\u0207\7\5\2\2\u0207\u0208\b\25\1\2\u0208")
        buf.write("\u0235\3\2\2\2\u0209\u020a\7A\2\2\u020a\u020b\7\4\2\2")
        buf.write("\u020b\u020c\5> \2\u020c\u020d\7\16\2\2\u020d\u020e\5")
        buf.write("F$\2\u020e\u020f\7\5\2\2\u020f\u0210\b\25\1\2\u0210\u0235")
        buf.write("\3\2\2\2\u0211\u0212\7\4\2\2\u0212\u0213\5\22\n\2\u0213")
        buf.write("\u0214\7\5\2\2\u0214\u0215\b\25\1\2\u0215\u021d\3\2\2")
        buf.write("\2\u0216\u0217\5*\26\2\u0217\u0218\b\25\1\2\u0218\u021d")
        buf.write("\3\2\2\2\u0219\u021a\5D#\2\u021a\u021b\b\25\1\2\u021b")
        buf.write("\u021d\3\2\2\2\u021c\u0211\3\2\2\2\u021c\u0216\3\2\2\2")
        buf.write("\u021c\u0219\3\2\2\2\u021d\u0227\3\2\2\2\u021e\u021f\7")
        buf.write("\"\2\2\u021f\u0220\5D#\2\u0220\u0221\b\25\1\2\u0221\u0226")
        buf.write("\3\2\2\2\u0222\u0223\5\64\33\2\u0223\u0224\b\25\1\2\u0224")
        buf.write("\u0226\3\2\2\2\u0225\u021e\3\2\2\2\u0225\u0222\3\2\2\2")
        buf.write("\u0226\u0229\3\2\2\2\u0227\u0225\3\2\2\2\u0227\u0228\3")
        buf.write("\2\2\2\u0228\u022c\3\2\2\2\u0229\u0227\3\2\2\2\u022a\u022b")
        buf.write("\7?\2\2\u022b\u022d\b\25\1\2\u022c\u022a\3\2\2\2\u022c")
        buf.write("\u022d\3\2\2\2\u022d\u0235\3\2\2\2\u022e\u022f\5:\36\2")
        buf.write("\u022f\u0232\b\25\1\2\u0230\u0231\7?\2\2\u0231\u0233\b")
        buf.write("\25\1\2\u0232\u0230\3\2\2\2\u0232\u0233\3\2\2\2\u0233")
        buf.write("\u0235\3\2\2\2\u0234\u01fd\3\2\2\2\u0234\u0201\3\2\2\2")
        buf.write("\u0234\u0209\3\2\2\2\u0234\u021c\3\2\2\2\u0234\u022e\3")
        buf.write("\2\2\2\u0235)\3\2\2\2\u0236\u0237\7B\2\2\u0237\u0238\7")
        buf.write("\4\2\2\u0238\u0239\5,\27\2\u0239\u023a\7\5\2\2\u023a\u023b")
        buf.write("\7\6\2\2\u023b\u023c\5\2\2\2\u023c\u023d\7\7\2\2\u023d")
        buf.write("\u023e\b\26\1\2\u023e\u0252\3\2\2\2\u023f\u0240\7C\2\2")
        buf.write("\u0240\u0241\7\4\2\2\u0241\u0242\5,\27\2\u0242\u0243\7")
        buf.write("\5\2\2\u0243\u0244\7\6\2\2\u0244\u0245\5\2\2\2\u0245\u0246")
        buf.write("\7\7\2\2\u0246\u0247\b\26\1\2\u0247\u0252\3\2\2\2\u0248")
        buf.write("\u0249\7D\2\2\u0249\u024a\7\4\2\2\u024a\u024b\5,\27\2")
        buf.write("\u024b\u024c\7\5\2\2\u024c\u024d\7\6\2\2\u024d\u024e\5")
        buf.write("\2\2\2\u024e\u024f\7\7\2\2\u024f\u0250\b\26\1\2\u0250")
        buf.write("\u0252\3\2\2\2\u0251\u0236\3\2\2\2\u0251\u023f\3\2\2\2")
        buf.write("\u0251\u0248\3\2\2\2\u0252+\3\2\2\2\u0253\u0254\5.\30")
        buf.write("\2\u0254\u025b\b\27\1\2\u0255\u0256\7\32\2\2\u0256\u0257")
        buf.write("\5.\30\2\u0257\u0258\b\27\1\2\u0258\u025a\3\2\2\2\u0259")
        buf.write("\u0255\3\2\2\2\u025a\u025d\3\2\2\2\u025b\u0259\3\2\2\2")
        buf.write("\u025b\u025c\3\2\2\2\u025c\u0264\3\2\2\2\u025d\u025b\3")
        buf.write("\2\2\2\u025e\u025f\7\32\2\2\u025f\u0260\5\60\31\2\u0260")
        buf.write("\u0261\b\27\1\2\u0261\u0263\3\2\2\2\u0262\u025e\3\2\2")
        buf.write("\2\u0263\u0266\3\2\2\2\u0264\u0262\3\2\2\2\u0264\u0265")
        buf.write("\3\2\2\2\u0265\u026b\3\2\2\2\u0266\u0264\3\2\2\2\u0267")
        buf.write("\u0268\7\32\2\2\u0268\u0269\5\62\32\2\u0269\u026a\b\27")
        buf.write("\1\2\u026a\u026c\3\2\2\2\u026b\u0267\3\2\2\2\u026b\u026c")
        buf.write("\3\2\2\2\u026c\u0283\3\2\2\2\u026d\u026e\5\60\31\2\u026e")
        buf.write("\u0275\b\27\1\2\u026f\u0270\7\32\2\2\u0270\u0271\5\60")
        buf.write("\31\2\u0271\u0272\b\27\1\2\u0272\u0274\3\2\2\2\u0273\u026f")
        buf.write("\3\2\2\2\u0274\u0277\3\2\2\2\u0275\u0273\3\2\2\2\u0275")
        buf.write("\u0276\3\2\2\2\u0276\u027c\3\2\2\2\u0277\u0275\3\2\2\2")
        buf.write("\u0278\u0279\7\32\2\2\u0279\u027a\5\62\32\2\u027a\u027b")
        buf.write("\b\27\1\2\u027b\u027d\3\2\2\2\u027c\u0278\3\2\2\2\u027c")
        buf.write("\u027d\3\2\2\2\u027d\u0283\3\2\2\2\u027e\u027f\5\62\32")
        buf.write("\2\u027f\u0280\b\27\1\2\u0280\u0283\3\2\2\2\u0281\u0283")
        buf.write("\3\2\2\2\u0282\u0253\3\2\2\2\u0282\u026d\3\2\2\2\u0282")
        buf.write("\u027e\3\2\2\2\u0282\u0281\3\2\2\2\u0283-\3\2\2\2\u0284")
        buf.write("\u0285\6\30\3\3\u0285\u0286\7E\2\2\u0286\u0287\5\f\7\2")
        buf.write("\u0287\u0288\b\30\1\2\u0288\u028d\3\2\2\2\u0289\u028a")
        buf.write("\5D#\2\u028a\u028b\b\30\1\2\u028b\u028d\3\2\2\2\u028c")
        buf.write("\u0284\3\2\2\2\u028c\u0289\3\2\2\2\u028d/\3\2\2\2\u028e")
        buf.write("\u028f\5\f\7\2\u028f\u0290\7!\2\2\u0290\u0291\5\16\b\2")
        buf.write("\u0291\u0292\b\31\1\2\u0292\61\3\2\2\2\u0293\u0294\7\66")
        buf.write("\2\2\u0294\u0295\5D#\2\u0295\u0296\b\32\1\2\u0296\63\3")
        buf.write("\2\2\2\u0297\u0298\7\4\2\2\u0298\u0299\58\35\2\u0299\u029a")
        buf.write("\7\5\2\2\u029a\u029b\b\33\1\2\u029b\u02a2\3\2\2\2\u029c")
        buf.write("\u029d\7#\2\2\u029d\u029e\5\66\34\2\u029e\u029f\7$\2\2")
        buf.write("\u029f\u02a0\b\33\1\2\u02a0\u02a2\3\2\2\2\u02a1\u0297")
        buf.write("\3\2\2\2\u02a1\u029c\3\2\2\2\u02a2\65\3\2\2\2\u02a3\u02b6")
        buf.write("\5\16\b\2\u02a4\u02a9\7L\2\2\u02a5\u02a6\5\16\b\2\u02a6")
        buf.write("\u02a7\b\34\1\2\u02a7\u02aa\3\2\2\2\u02a8\u02aa\b\34\1")
        buf.write("\2\u02a9\u02a5\3\2\2\2\u02a9\u02a8\3\2\2\2\u02aa\u02b7")
        buf.write("\3\2\2\2\u02ab\u02ac\7\32\2\2\u02ac\u02ad\5\16\b\2\u02ad")
        buf.write("\u02ae\b\34\1\2\u02ae\u02b0\3\2\2\2\u02af\u02ab\3\2\2")
        buf.write("\2\u02b0\u02b1\3\2\2\2\u02b1\u02af\3\2\2\2\u02b1\u02b2")
        buf.write("\3\2\2\2\u02b2\u02b3\3\2\2\2\u02b3\u02b4\b\34\1\2\u02b4")
        buf.write("\u02b7\3\2\2\2\u02b5\u02b7\b\34\1\2\u02b6\u02a4\3\2\2")
        buf.write("\2\u02b6\u02af\3\2\2\2\u02b6\u02b5\3\2\2\2\u02b7\u02bd")
        buf.write("\3\2\2\2\u02b8\u02b9\7L\2\2\u02b9\u02ba\5\16\b\2\u02ba")
        buf.write("\u02bb\b\34\1\2\u02bb\u02bd\3\2\2\2\u02bc\u02a3\3\2\2")
        buf.write("\2\u02bc\u02b8\3\2\2\2\u02bd\67\3\2\2\2\u02be\u02bf\5")
        buf.write("\20\t\2\u02bf\u02c5\b\35\1\2\u02c0\u02c1\7\32\2\2\u02c1")
        buf.write("\u02c2\7\66\2\2\u02c2\u02c3\5\22\n\2\u02c3\u02c4\b\35")
        buf.write("\1\2\u02c4\u02c6\3\2\2\2\u02c5\u02c0\3\2\2\2\u02c5\u02c6")
        buf.write("\3\2\2\2\u02c6\u02cd\3\2\2\2\u02c7\u02c8\7\66\2\2\u02c8")
        buf.write("\u02c9\5\22\n\2\u02c9\u02ca\b\35\1\2\u02ca\u02cd\3\2\2")
        buf.write("\2\u02cb\u02cd\3\2\2\2\u02cc\u02be\3\2\2\2\u02cc\u02c7")
        buf.write("\3\2\2\2\u02cc\u02cb\3\2\2\2\u02cd9\3\2\2\2\u02ce\u02d2")
        buf.write("\7#\2\2\u02cf\u02d0\5<\37\2\u02d0\u02d1\b\36\1\2\u02d1")
        buf.write("\u02d3\3\2\2\2\u02d2\u02cf\3\2\2\2\u02d2\u02d3\3\2\2\2")
        buf.write("\u02d3\u02d4\3\2\2\2\u02d4\u02d5\7$\2\2\u02d5\u02e9\b")
        buf.write("\36\1\2\u02d6\u02da\7\6\2\2\u02d7\u02d8\5<\37\2\u02d8")
        buf.write("\u02d9\b\36\1\2\u02d9\u02db\3\2\2\2\u02da\u02d7\3\2\2")
        buf.write("\2\u02da\u02db\3\2\2\2\u02db\u02dc\3\2\2\2\u02dc\u02dd")
        buf.write("\7\7\2\2\u02dd\u02e9\b\36\1\2\u02de\u02df\7M\2\2\u02df")
        buf.write("\u02e9\b\36\1\2\u02e0\u02e1\7N\2\2\u02e1\u02e9\b\36\1")
        buf.write("\2\u02e2\u02e3\5B\"\2\u02e3\u02e4\b\36\1\2\u02e4\u02e9")
        buf.write("\3\2\2\2\u02e5\u02e6\6\36\4\3\u02e6\u02e7\7%\2\2\u02e7")
        buf.write("\u02e9\b\36\1\2\u02e8\u02ce\3\2\2\2\u02e8\u02d6\3\2\2")
        buf.write("\2\u02e8\u02de\3\2\2\2\u02e8\u02e0\3\2\2\2\u02e8\u02e2")
        buf.write("\3\2\2\2\u02e8\u02e5\3\2\2\2\u02e9;\3\2\2\2\u02ea\u0319")
        buf.write("\5\16\b\2\u02eb\u02ec\7\32\2\2\u02ec\u0302\5\16\b\2\u02ed")
        buf.write("\u02ee\7L\2\2\u02ee\u02ef\5\16\b\2\u02ef\u02f0\b\37\1")
        buf.write("\2\u02f0\u0303\3\2\2\2\u02f1\u02f8\b\37\1\2\u02f2\u02f3")
        buf.write("\7\32\2\2\u02f3\u02f4\5\16\b\2\u02f4\u02f5\b\37\1\2\u02f5")
        buf.write("\u02f7\3\2\2\2\u02f6\u02f2\3\2\2\2\u02f7\u02fa\3\2\2\2")
        buf.write("\u02f8\u02f6\3\2\2\2\u02f8\u02f9\3\2\2\2\u02f9\u0300\3")
        buf.write("\2\2\2\u02fa\u02f8\3\2\2\2\u02fb\u02fc\7\16\2\2\u02fc")
        buf.write("\u02fd\5\16\b\2\u02fd\u02fe\b\37\1\2\u02fe\u0301\3\2\2")
        buf.write("\2\u02ff\u0301\b\37\1\2\u0300\u02fb\3\2\2\2\u0300\u02ff")
        buf.write("\3\2\2\2\u0301\u0303\3\2\2\2\u0302\u02ed\3\2\2\2\u0302")
        buf.write("\u02f1\3\2\2\2\u0303\u031a\3\2\2\2\u0304\u0305\7L\2\2")
        buf.write("\u0305\u0306\5\16\b\2\u0306\u0307\b\37\1\2\u0307\u031a")
        buf.write("\3\2\2\2\u0308\u030e\b\37\1\2\u0309\u030a\7\16\2\2\u030a")
        buf.write("\u030b\5\16\b\2\u030b\u030c\b\37\1\2\u030c\u030f\3\2\2")
        buf.write("\2\u030d\u030f\b\37\1\2\u030e\u0309\3\2\2\2\u030e\u030d")
        buf.write("\3\2\2\2\u030f\u031a\3\2\2\2\u0310\u0311\7\13\2\2\u0311")
        buf.write("\u0317\5> \2\u0312\u0313\7\16\2\2\u0313\u0314\5F$\2\u0314")
        buf.write("\u0315\b\37\1\2\u0315\u0318\3\2\2\2\u0316\u0318\b\37\1")
        buf.write("\2\u0317\u0312\3\2\2\2\u0317\u0316\3\2\2\2\u0318\u031a")
        buf.write("\3\2\2\2\u0319\u02eb\3\2\2\2\u0319\u0304\3\2\2\2\u0319")
        buf.write("\u0308\3\2\2\2\u0319\u0310\3\2\2\2\u031a=\3\2\2\2\u031b")
        buf.write("\u031c\5@!\2\u031c\u0323\b \1\2\u031d\u031e\7\32\2\2\u031e")
        buf.write("\u031f\5@!\2\u031f\u0320\b \1\2\u0320\u0322\3\2\2\2\u0321")
        buf.write("\u031d\3\2\2\2\u0322\u0325\3\2\2\2\u0323\u0321\3\2\2\2")
        buf.write("\u0323\u0324\3\2\2\2\u0324?\3\2\2\2\u0325\u0323\3\2\2")
        buf.write("\2\u0326\u0327\5\n\6\2\u0327\u0328\7\62\2\2\u0328\u0329")
        buf.write("\5\16\b\2\u0329\u032a\b!\1\2\u032aA\3\2\2\2\u032b\u032c")
        buf.write("\7J\2\2\u032c\u0336\b\"\1\2\u032d\u032e\7K\2\2\u032e\u0336")
        buf.write("\b\"\1\2\u032f\u0330\7F\2\2\u0330\u0336\b\"\1\2\u0331")
        buf.write("\u0332\7G\2\2\u0332\u0336\b\"\1\2\u0333\u0334\7H\2\2\u0334")
        buf.write("\u0336\b\"\1\2\u0335\u032b\3\2\2\2\u0335\u032d\3\2\2\2")
        buf.write("\u0335\u032f\3\2\2\2\u0335\u0331\3\2\2\2\u0335\u0333\3")
        buf.write("\2\2\2\u0336C\3\2\2\2\u0337\u0338\7I\2\2\u0338\u0339\b")
        buf.write("#\1\2\u0339E\3\2\2\2\u033a\u033b\5\16\b\2\u033b\u033c")
        buf.write("\b$\1\2\u033cG\3\2\2\2\u033d\u033e\5\n\6\2\u033e\u0345")
        buf.write("\b%\1\2\u033f\u0340\7\32\2\2\u0340\u0341\5\n\6\2\u0341")
        buf.write("\u0342\b%\1\2\u0342\u0344\3\2\2\2\u0343\u033f\3\2\2\2")
        buf.write("\u0344\u0347\3\2\2\2\u0345\u0343\3\2\2\2\u0345\u0346\3")
        buf.write("\2\2\2\u0346I\3\2\2\2\u0347\u0345\3\2\2\2DOgp~\u0084\u008f")
        buf.write("\u00b8\u00cc\u00e5\u0100\u010f\u0111\u011e\u0120\u012b")
        buf.write("\u013b\u014b\u014d\u0160\u0163\u0166\u016e\u0178\u0183")
        buf.write("\u01a8\u01b4\u01b6\u01cf\u01d1\u01de\u01e0\u01e9\u01fb")
        buf.write("\u021c\u0225\u0227\u022c\u0232\u0234\u0251\u025b\u0264")
        buf.write("\u026b\u0275\u027c\u0282\u028c\u02a1\u02a9\u02b1\u02b6")
        buf.write("\u02bc\u02c5\u02cc\u02d2\u02da\u02e8\u02f8\u0300\u0302")
        buf.write("\u030e\u0317\u0319\u0323\u0335\u0345")
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
            self.state = 227
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,8,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 82
                self.match(SetlXgrammarParser.T__0)
                self.state = 83
                self.match(SetlXgrammarParser.T__1)
                self.state = 84
                localctx.c1 = self.condition()
                self.state = 85
                self.match(SetlXgrammarParser.T__2)
                self.state = 86
                self.match(SetlXgrammarParser.T__3)
                self.state = 87
                localctx.b1 = self.block()
                self.state = 88
                self.match(SetlXgrammarParser.T__4)
                self.state = 101
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,1,self._ctx)
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1:
                        self.state = 89
                        self.match(SetlXgrammarParser.T__5)
                        self.state = 90
                        self.match(SetlXgrammarParser.T__0)
                        self.state = 91
                        self.match(SetlXgrammarParser.T__1)
                        self.state = 92
                        localctx.c2 = self.condition()
                        self.state = 93
                        self.match(SetlXgrammarParser.T__2)
                        self.state = 94
                        self.match(SetlXgrammarParser.T__3)
                        self.state = 95
                        localctx.b2 = self.block()
                        self.state = 96
                        self.match(SetlXgrammarParser.T__4)
                        else_list.append(IfThenBranch(localctx.c2.cnd,localctx.b2.blk)) 
                        			 
                    self.state = 103
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,1,self._ctx)

                self.state = 110
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
                if la_ == 1:
                    self.state = 104
                    self.match(SetlXgrammarParser.T__5)
                    self.state = 105
                    self.match(SetlXgrammarParser.T__3)
                    self.state = 106
                    localctx.b3 = self.block()
                    self.state = 107
                    self.match(SetlXgrammarParser.T__4)
                    else_list.append(localctx.b3.blk) 


                localctx.stmnt = IfThen(localctx.c1.cnd,localctx.b1.blk,else_list) 
                		
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 114
                self.match(SetlXgrammarParser.T__6)
                self.state = 115
                self.match(SetlXgrammarParser.T__3)
                self.state = 124
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==SetlXgrammarParser.T__7:
                    self.state = 116
                    self.match(SetlXgrammarParser.T__7)
                    self.state = 117
                    localctx.c1 = self.condition()
                    self.state = 118
                    self.match(SetlXgrammarParser.T__8)
                    self.state = 119
                    localctx.b1 = self.block()
                    caseList.append((localctx.c1.cnd, localctx.b1.blk)) 
                    self.state = 126
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 130
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==SetlXgrammarParser.T__9:
                    self.state = 127
                    self.match(SetlXgrammarParser.T__9)
                    self.state = 128
                    self.match(SetlXgrammarParser.T__8)
                    self.state = 129
                    localctx.b2 = self.block()


                self.state = 132
                self.match(SetlXgrammarParser.T__4)
                localctx.stmnt = Switch(caseList,localctx.b2.blk) 
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 134
                self.match(SetlXgrammarParser.T__10)
                self.state = 135
                self.match(SetlXgrammarParser.T__1)
                self.state = 136
                localctx._iteratorChain = self.iteratorChain(False)
                self.state = 141
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==SetlXgrammarParser.T__11:
                    self.state = 137
                    self.match(SetlXgrammarParser.T__11)
                    self.state = 138
                    localctx._condition = self.condition()
                    condition = localctx._condition.cnd


                self.state = 143
                self.match(SetlXgrammarParser.T__2)
                self.state = 144
                self.match(SetlXgrammarParser.T__3)
                self.state = 145
                localctx._block = self.block()
                self.state = 146
                self.match(SetlXgrammarParser.T__4)
                localctx.stmnt = For(localctx._iteratorChain.ic, condition, localctx._block.blk) 
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 149
                self.match(SetlXgrammarParser.T__12)
                self.state = 150
                self.match(SetlXgrammarParser.T__1)
                self.state = 151
                localctx._condition = self.condition()
                self.state = 152
                self.match(SetlXgrammarParser.T__2)
                self.state = 153
                self.match(SetlXgrammarParser.T__3)
                self.state = 154
                localctx._block = self.block()
                self.state = 155
                self.match(SetlXgrammarParser.T__4)
                localctx.stmnt = While(localctx._condition.cnd, localctx._block.blk) 
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 158
                self.match(SetlXgrammarParser.T__13)
                self.state = 159
                self.match(SetlXgrammarParser.T__3)
                self.state = 160
                localctx._block = self.block()
                self.state = 161
                self.match(SetlXgrammarParser.T__4)
                self.state = 162
                self.match(SetlXgrammarParser.T__12)
                self.state = 163
                self.match(SetlXgrammarParser.T__1)
                self.state = 164
                localctx._condition = self.condition()
                self.state = 165
                self.match(SetlXgrammarParser.T__2)
                self.state = 166
                self.match(SetlXgrammarParser.T__14)
                localctx.stmnt = DoWhile(localctx._condition.cnd, localctx._block.blk) 
                		
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 169
                self.match(SetlXgrammarParser.T__15)
                self.state = 170
                self.match(SetlXgrammarParser.T__3)
                self.state = 171
                localctx.b1 = self.block()
                self.state = 172
                self.match(SetlXgrammarParser.T__4)
                self.state = 182
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,6,self._ctx)
                if la_ == 1:
                    self.state = 173
                    self.match(SetlXgrammarParser.T__16)
                    self.state = 174
                    self.match(SetlXgrammarParser.T__1)
                    self.state = 175
                    localctx.v2 = self.assignableVariable()
                    self.state = 176
                    self.match(SetlXgrammarParser.T__2)
                    self.state = 177
                    self.match(SetlXgrammarParser.T__3)
                    self.state = 178
                    localctx.b3 = self.block()
                    self.state = 179
                    self.match(SetlXgrammarParser.T__4)
                    tryList.append(TryCatchBranch(localctx.v2.v, localctx.b3.blk))         
                    			


                localctx.stmnt = TryCatch(localctx.b1.blk, tryList) 
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 186
                self.match(SetlXgrammarParser.T__17)
                self.state = 187
                self.match(SetlXgrammarParser.T__14)
                localctx.stmnt = Backtrack() 
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 189
                self.match(SetlXgrammarParser.T__18)
                self.state = 190
                self.match(SetlXgrammarParser.T__14)
                localctx.stmnt = Break() 
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 192
                self.match(SetlXgrammarParser.T__19)
                self.state = 193
                self.match(SetlXgrammarParser.T__14)
                localctx.stmnt = Continue() 
                pass

            elif la_ == 10:
                self.enterOuterAlt(localctx, 10)
                self.state = 195
                self.match(SetlXgrammarParser.T__20)
                self.state = 196
                self.match(SetlXgrammarParser.T__14)
                localctx.stmnt = Exit() 
                pass

            elif la_ == 11:
                self.enterOuterAlt(localctx, 11)
                self.state = 198
                self.match(SetlXgrammarParser.T__21)
                self.state = 202
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,7,self._ctx)
                if la_ == 1:
                    self.state = 199
                    localctx._expr = self.expr(False)
                    expression = localctx._expr.ex 


                self.state = 204
                self.match(SetlXgrammarParser.T__14)
                localctx.stmnt = Return(expression) 
                pass

            elif la_ == 12:
                self.enterOuterAlt(localctx, 12)
                self.state = 206
                self.match(SetlXgrammarParser.T__22)
                self.state = 207
                self.match(SetlXgrammarParser.T__1)
                self.state = 208
                localctx._condition = self.condition()
                self.state = 209
                self.match(SetlXgrammarParser.T__23)
                self.state = 210
                localctx._expr = self.expr(False)
                self.state = 211
                self.match(SetlXgrammarParser.T__2)
                self.state = 212
                self.match(SetlXgrammarParser.T__14)
                localctx.stmnt = Assert(localctx._condition.cnd, localctx._expr.ex)
                pass

            elif la_ == 13:
                self.enterOuterAlt(localctx, 13)
                self.state = 215
                localctx._assignmentOther = self.assignmentOther()
                self.state = 216
                self.match(SetlXgrammarParser.T__14)
                localctx.stmnt = localctx._assignmentOther.assign 
                pass

            elif la_ == 14:
                self.enterOuterAlt(localctx, 14)
                self.state = 219
                localctx._assignmentDirect = self.assignmentDirect()
                self.state = 220
                self.match(SetlXgrammarParser.T__14)
                localctx.stmnt = localctx._assignmentDirect.assign 
                pass

            elif la_ == 15:
                self.enterOuterAlt(localctx, 15)
                self.state = 223
                localctx._expr = self.expr(False)
                self.state = 224
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
            self.state = 229
            localctx._assignable = self.assignable(False)
            self.state = 254
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [SetlXgrammarParser.T__24]:
                self.state = 230
                self.match(SetlXgrammarParser.T__24)
                self.state = 231
                localctx.e = self.expr(False)
                localctx.assign = SumAssignment(localctx._assignable.a, localctx.e.ex) 
                pass
            elif token in [SetlXgrammarParser.T__25]:
                self.state = 234
                self.match(SetlXgrammarParser.T__25)
                self.state = 235
                localctx.e = self.expr(False)
                localctx.assign = DifferenceAssignment(localctx._assignable.a, localctx.e.ex) 
                pass
            elif token in [SetlXgrammarParser.T__26]:
                self.state = 238
                self.match(SetlXgrammarParser.T__26)
                self.state = 239
                localctx.e = self.expr(False)
                localctx.assign = ProductAssignment(localctx._assignable.a, localctx.e.ex) 
                pass
            elif token in [SetlXgrammarParser.T__27]:
                self.state = 242
                self.match(SetlXgrammarParser.T__27)
                self.state = 243
                localctx.e = self.expr(False)
                localctx.assign = QuotientAssignment(localctx._assignable.a, localctx.e.ex) 
                pass
            elif token in [SetlXgrammarParser.T__28]:
                self.state = 246
                self.match(SetlXgrammarParser.T__28)
                self.state = 247
                localctx.e = self.expr(False)
                localctx.assign = IntegerDivisionAssignment(localctx._assignable.a, localctx.e.ex) 
                pass
            elif token in [SetlXgrammarParser.T__29]:
                self.state = 250
                self.match(SetlXgrammarParser.T__29)
                self.state = 251
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
            self.state = 271
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,11,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 256
                localctx._variable = self.variable()
                self.state = 257
                self.match(SetlXgrammarParser.T__30)
                self.state = 258
                localctx._procedure = self.procedure()

                localctx._procedure.pd.name = localctx._variable.v.id
                localctx.assign = localctx._procedure.pd
                    
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 261
                localctx._assignable = self.assignable(False)
                self.state = 262
                self.match(SetlXgrammarParser.T__30)
                self.state = 269
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,10,self._ctx)
                if la_ == 1:
                    self.state = 263
                    localctx._assignmentDirect = self.assignmentDirect()
                    localctx.assign = Assignment(localctx._assignable.a, localctx._assignmentDirect.assign) 
                    pass

                elif la_ == 2:
                    self.state = 266
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
            self.state = 297
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,14,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 273
                localctx._assignableVariable = self.assignableVariable()
                localctx.a = localctx._assignableVariable.v
                self.state = 286
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==SetlXgrammarParser.T__31 or _la==SetlXgrammarParser.T__32:
                    self.state = 284
                    self._errHandler.sync(self)
                    token = self._input.LA(1)
                    if token in [SetlXgrammarParser.T__31]:
                        self.state = 275
                        self.match(SetlXgrammarParser.T__31)
                        self.state = 276
                        localctx._variable = self.variable()
                        localctx.a = AssignableMember(localctx.a, localctx._variable.v)
                        pass
                    elif token in [SetlXgrammarParser.T__32]:
                        self.state = 279
                        self.match(SetlXgrammarParser.T__32)
                        self.state = 280
                        localctx._exprList = self.exprList(False)
                        self.state = 281
                        self.match(SetlXgrammarParser.T__33)
                        localctx.a = AssignableCollectionAccess(localctx.a, localctx._exprList.exprs)
                        pass
                    else:
                        raise NoViableAltException(self)

                    self.state = 288
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 289
                self.match(SetlXgrammarParser.T__32)
                self.state = 290
                localctx._assignmentList = self.assignmentList()
                self.state = 291
                self.match(SetlXgrammarParser.T__33)
                localctx.a = AssignableList(localctx._assignmentList.al)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 294
                if not localctx.enableIgnore:
                    from antlr4.error.Errors import FailedPredicateException
                    raise FailedPredicateException(self, "$enableIgnore")
                self.state = 295
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
            self.state = 299
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
            self.state = 302
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
            self.state = 305
            localctx._exprContent = self.exprContent(localctx.enableIgnore)
            localctx.exprs.append(localctx._exprContent.ex)
            self.state = 313
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,15,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 307
                    self.match(SetlXgrammarParser.T__23)
                    self.state = 308
                    localctx._exprContent = self.exprContent(localctx.enableIgnore)
                    localctx.exprs.append(localctx._exprContent.ex) 
                self.state = 315
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,15,self._ctx)

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
            self.state = 331
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,17,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 316
                localctx._lambdaProcedure = self.lambdaProcedure()
                localctx.ex = localctx._lambdaProcedure.lp 
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 319
                localctx._implication = self.implication(localctx.enableIgnore)
                localctx.ex = localctx._implication.i
                self.state = 329
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [SetlXgrammarParser.T__35]:
                    self.state = 321
                    self.match(SetlXgrammarParser.T__35)
                    self.state = 322
                    localctx._implication = self.implication(localctx.enableIgnore)
                    localctx.ex = BooleanEqual(localctx.ex,localctx._implication.i) 
                    pass
                elif token in [SetlXgrammarParser.T__36]:
                    self.state = 325
                    self.match(SetlXgrammarParser.T__36)
                    self.state = 326
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
            self.state = 333
            localctx._lambdaParameters = self.lambdaParameters()

            self.state = 334
            self.match(SetlXgrammarParser.T__37)
            self.state = 335
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
            self.state = 356
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [SetlXgrammarParser.ID]:
                self.enterOuterAlt(localctx, 1)
                self.state = 338
                localctx._variable = self.variable()
                localctx.paramList.append(Parameter(localctx._variable.v.id)) 
                pass
            elif token in [SetlXgrammarParser.T__32]:
                self.enterOuterAlt(localctx, 2)
                self.state = 341
                self.match(SetlXgrammarParser.T__32)
                self.state = 353
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==SetlXgrammarParser.ID:
                    self.state = 342
                    localctx.v1 = self.variable()
                    localctx.paramList.append(Parameter(localctx.v1.v.id))
                    self.state = 350
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    while _la==SetlXgrammarParser.T__23:
                        self.state = 344
                        self.match(SetlXgrammarParser.T__23)
                        self.state = 345
                        localctx.v2 = self.variable()
                        localctx.paramList.append(Parameter(localctx.v2.v.id))
                        self.state = 352
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)



                self.state = 355
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
            self.state = 358
            localctx._disjunction = self.disjunction(localctx.enableIgnore)
            localctx.i = localctx._disjunction.d
            self.state = 364
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==SetlXgrammarParser.T__38:
                self.state = 360
                self.match(SetlXgrammarParser.T__38)
                self.state = 361
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
            self.state = 366
            localctx._conjunction = self.conjunction(localctx.enableIgnore)
            localctx.d = localctx._conjunction.c
            self.state = 374
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==SetlXgrammarParser.T__39:
                self.state = 368
                self.match(SetlXgrammarParser.T__39)
                self.state = 369
                localctx._conjunction = self.conjunction(localctx.enableIgnore)
                localctx.d = Disjunction(localctx.d, localctx._conjunction.c) 
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
            self.state = 377
            localctx._comparison = self.comparison(localctx.enableIgnore)
            localctx.c = localctx._comparison.c
            self.state = 385
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==SetlXgrammarParser.T__40:
                self.state = 379
                self.match(SetlXgrammarParser.T__40)
                self.state = 380
                localctx._comparison = self.comparison(localctx.enableIgnore)
                localctx.c = Conjunction(localctx.c, localctx._comparison.c) 
                self.state = 387
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
            self.state = 388
            localctx.s1 = self.setlxSum(localctx.enableIgnore)
            localctx.c = localctx.s1.s 
            self.state = 422
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [SetlXgrammarParser.T__41]:
                self.state = 390
                self.match(SetlXgrammarParser.T__41)
                self.state = 391
                localctx.s2 = self.setlxSum(localctx.enableIgnore)
                localctx.c = Equal(localctx.s1.s,localctx.s2.s) 
                pass
            elif token in [SetlXgrammarParser.T__42]:
                self.state = 394
                self.match(SetlXgrammarParser.T__42)
                self.state = 395
                localctx.s2 = self.setlxSum(localctx.enableIgnore)
                localctx.c = NotEqual(localctx.s1.s,localctx.s2.s) 
                pass
            elif token in [SetlXgrammarParser.T__43]:
                self.state = 398
                self.match(SetlXgrammarParser.T__43)
                self.state = 399
                localctx.s2 = self.setlxSum(localctx.enableIgnore)
                localctx.c = LessThan(localctx.s1.s,localctx.s2.s) 
                pass
            elif token in [SetlXgrammarParser.T__44]:
                self.state = 402
                self.match(SetlXgrammarParser.T__44)
                self.state = 403
                localctx.s2 = self.setlxSum(localctx.enableIgnore)
                localctx.c = LessOrEqual(localctx.s1.s,localctx.s2.s) 
                pass
            elif token in [SetlXgrammarParser.T__45]:
                self.state = 406
                self.match(SetlXgrammarParser.T__45)
                self.state = 407
                localctx.s2 = self.setlxSum(localctx.enableIgnore)
                localctx.c = GreaterThan(localctx.s1.s,localctx.s2.s) 
                pass
            elif token in [SetlXgrammarParser.T__46]:
                self.state = 410
                self.match(SetlXgrammarParser.T__46)
                self.state = 411
                localctx.s2 = self.setlxSum(localctx.enableIgnore)
                localctx.c = GreaterOrEqual(localctx.s1.s,localctx.s2.s) 
                pass
            elif token in [SetlXgrammarParser.T__47]:
                self.state = 414
                self.match(SetlXgrammarParser.T__47)
                self.state = 415
                localctx.s2 = self.setlxSum(localctx.enableIgnore)
                localctx.c = In(localctx.s1.s,localctx.s2.s) 
                pass
            elif token in [SetlXgrammarParser.T__48]:
                self.state = 418
                self.match(SetlXgrammarParser.T__48)
                self.state = 419
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
            self.state = 424
            localctx.p1 = self.product(localctx.enableIgnore)
            localctx.s = localctx.p1.p
            self.state = 436
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==SetlXgrammarParser.T__49 or _la==SetlXgrammarParser.T__50:
                self.state = 434
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [SetlXgrammarParser.T__49]:
                    self.state = 426
                    self.match(SetlXgrammarParser.T__49)
                    self.state = 427
                    localctx.p2 = self.product(localctx.enableIgnore)
                    localctx.s = Sum(localctx.p1.p,localctx.p2.p) 
                    pass
                elif token in [SetlXgrammarParser.T__50]:
                    self.state = 430
                    self.match(SetlXgrammarParser.T__50)
                    self.state = 431
                    localctx.p2 = self.product(localctx.enableIgnore)
                    localctx.s = Difference(localctx.p1.p,localctx.p2.p) 
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 438
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
            self.state = 439
            localctx.r1 = self.setlxReduce(localctx.enableIgnore)
            localctx.p = localctx.r1.r
            self.state = 463
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << SetlXgrammarParser.T__51) | (1 << SetlXgrammarParser.T__52) | (1 << SetlXgrammarParser.T__53) | (1 << SetlXgrammarParser.T__54) | (1 << SetlXgrammarParser.T__55))) != 0):
                self.state = 461
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [SetlXgrammarParser.T__51]:
                    self.state = 441
                    self.match(SetlXgrammarParser.T__51)
                    self.state = 442
                    localctx.r2 = self.setlxReduce(localctx.enableIgnore)
                    localctx.p = Product(localctx.p,localctx.r2.r) 
                    pass
                elif token in [SetlXgrammarParser.T__52]:
                    self.state = 445
                    self.match(SetlXgrammarParser.T__52)
                    self.state = 446
                    localctx.r2 = self.setlxReduce(localctx.enableIgnore)
                    localctx.p = Quotient(localctx.p,localctx.r2.r) 
                    pass
                elif token in [SetlXgrammarParser.T__53]:
                    self.state = 449
                    self.match(SetlXgrammarParser.T__53)
                    self.state = 450
                    localctx.r2 = self.setlxReduce(localctx.enableIgnore)
                    localctx.p = IntegerDivision(localctx.p,localctx.r2.r) 
                    pass
                elif token in [SetlXgrammarParser.T__54]:
                    self.state = 453
                    self.match(SetlXgrammarParser.T__54)
                    self.state = 454
                    localctx.r2 = self.setlxReduce(localctx.enableIgnore)
                    localctx.p = Modulo(localctx.p,localctx.r2.r) 
                    pass
                elif token in [SetlXgrammarParser.T__55]:
                    self.state = 457
                    self.match(SetlXgrammarParser.T__55)
                    self.state = 458
                    localctx.r2 = self.setlxReduce(localctx.enableIgnore)
                    localctx.p = CartesianProduct(localctx.p,localctx.r2.r) 
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 465
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
            self.state = 466
            localctx.p1 = self.prefixOperation(localctx.enableIgnore)
            localctx.r = localctx.p1.p
            self.state = 478
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==SetlXgrammarParser.T__56 or _la==SetlXgrammarParser.T__57:
                self.state = 476
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [SetlXgrammarParser.T__56]:
                    self.state = 468
                    self.match(SetlXgrammarParser.T__56)
                    self.state = 469
                    localctx.p2 = self.prefixOperation(localctx.enableIgnore)
                    localctx.r = SumOfMembersBinary(localctx.r,localctx.p2.p) 
                    pass
                elif token in [SetlXgrammarParser.T__57]:
                    self.state = 472
                    self.match(SetlXgrammarParser.T__57)
                    self.state = 473
                    localctx.p2 = self.prefixOperation(localctx.enableIgnore)
                    localctx.r = ProductOfMembersBinary(localctx.r,localctx.p2.p) 
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 480
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
            self.state = 505
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,32,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 481
                localctx._factor = self.factor(localctx.enableIgnore)
                localctx.p = localctx._factor.f
                self.state = 487
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==SetlXgrammarParser.T__58:
                    self.state = 483
                    self.match(SetlXgrammarParser.T__58)
                    self.state = 484
                    localctx._prefixOperation = self.prefixOperation(localctx.enableIgnore)
                    localctx.p = Power(localctx.p,localctx._prefixOperation.p) 


                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 489
                self.match(SetlXgrammarParser.T__56)
                self.state = 490
                localctx._prefixOperation = self.prefixOperation(localctx.enableIgnore)
                localctx.p = SumOfMembers(localctx._prefixOperation.p) 
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 493
                self.match(SetlXgrammarParser.T__57)
                self.state = 494
                localctx._prefixOperation = self.prefixOperation(localctx.enableIgnore)
                localctx.p = ProductOfMembers(localctx._prefixOperation.p) 
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 497
                self.match(SetlXgrammarParser.T__59)
                self.state = 498
                localctx._prefixOperation = self.prefixOperation(localctx.enableIgnore)
                localctx.p = Cardinality(localctx._prefixOperation.p) 
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 501
                self.match(SetlXgrammarParser.T__50)
                self.state = 502
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
            self.state = 562
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,38,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 507
                self.match(SetlXgrammarParser.T__60)
                self.state = 508
                localctx._factor = self.factor(localctx.enableIgnore)
                localctx.f = Not(localctx._factor.f) 
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 511
                self.match(SetlXgrammarParser.T__61)
                self.state = 512
                self.match(SetlXgrammarParser.T__1)
                self.state = 513
                localctx._iteratorChain = self.iteratorChain(localctx.enableIgnore)
                self.state = 514
                self.match(SetlXgrammarParser.T__11)
                self.state = 515
                localctx._condition = self.condition()
                self.state = 516
                self.match(SetlXgrammarParser.T__2)
                localctx.f = Forall(localctx._iteratorChain.ic,localctx._condition.cnd)
                		
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 519
                self.match(SetlXgrammarParser.T__62)
                self.state = 520
                self.match(SetlXgrammarParser.T__1)
                self.state = 521
                localctx._iteratorChain = self.iteratorChain(localctx.enableIgnore)
                self.state = 522
                self.match(SetlXgrammarParser.T__11)
                self.state = 523
                localctx._condition = self.condition()
                self.state = 524
                self.match(SetlXgrammarParser.T__2)
                localctx.f = Exists(localctx._iteratorChain.ic,localctx._condition.cnd)
                		
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 538
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [SetlXgrammarParser.T__1]:
                    self.state = 527
                    self.match(SetlXgrammarParser.T__1)
                    self.state = 528
                    localctx._exprContent = self.exprContent(localctx.enableIgnore)
                    self.state = 529
                    self.match(SetlXgrammarParser.T__2)
                    localctx.f = localctx._exprContent.ex 
                    pass
                elif token in [SetlXgrammarParser.T__63, SetlXgrammarParser.T__64, SetlXgrammarParser.T__65]:
                    self.state = 532
                    localctx._procedure = self.procedure()
                    localctx.f = localctx._procedure.pd 
                    pass
                elif token in [SetlXgrammarParser.ID]:
                    self.state = 535
                    localctx._variable = self.variable()
                    localctx.f = localctx._variable.v 
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 549
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << SetlXgrammarParser.T__1) | (1 << SetlXgrammarParser.T__31) | (1 << SetlXgrammarParser.T__32))) != 0):
                    self.state = 547
                    self._errHandler.sync(self)
                    token = self._input.LA(1)
                    if token in [SetlXgrammarParser.T__31]:
                        self.state = 540
                        self.match(SetlXgrammarParser.T__31)
                        self.state = 541
                        localctx._variable = self.variable()
                        localctx.f = MemberAccess(localctx.f,localctx._variable.v) 
                        pass
                    elif token in [SetlXgrammarParser.T__1, SetlXgrammarParser.T__32]:
                        self.state = 544
                        localctx._call = self.call(localctx.enableIgnore)

                        localctx._call.c.callable = localctx.f
                        localctx.f = localctx._call.c
                                
                        pass
                    else:
                        raise NoViableAltException(self)

                    self.state = 551
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 554
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==SetlXgrammarParser.T__60:
                    self.state = 552
                    self.match(SetlXgrammarParser.T__60)
                    localctx.f = Factorial(localctx.f) 


                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 556
                localctx._value = self.value(localctx.enableIgnore)
                localctx.f = localctx._value.v 
                self.state = 560
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==SetlXgrammarParser.T__60:
                    self.state = 558
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
            self.state = 591
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [SetlXgrammarParser.T__63]:
                self.enterOuterAlt(localctx, 1)
                self.state = 564
                self.match(SetlXgrammarParser.T__63)
                self.state = 565
                self.match(SetlXgrammarParser.T__1)
                self.state = 566
                localctx._procedureParameters = self.procedureParameters(True)
                self.state = 567
                self.match(SetlXgrammarParser.T__2)
                self.state = 568
                self.match(SetlXgrammarParser.T__3)
                self.state = 569
                localctx._block = self.block()
                self.state = 570
                self.match(SetlXgrammarParser.T__4)
                localctx.pd = Procedure(localctx._procedureParameters.paramList, localctx._block.blk) 
                		
                pass
            elif token in [SetlXgrammarParser.T__64]:
                self.enterOuterAlt(localctx, 2)
                self.state = 573
                self.match(SetlXgrammarParser.T__64)
                self.state = 574
                self.match(SetlXgrammarParser.T__1)
                self.state = 575
                localctx._procedureParameters = self.procedureParameters(False)
                self.state = 576
                self.match(SetlXgrammarParser.T__2)
                self.state = 577
                self.match(SetlXgrammarParser.T__3)
                self.state = 578
                localctx._block = self.block()
                self.state = 579
                self.match(SetlXgrammarParser.T__4)
                localctx.pd = CachedProcedure(localctx._procedureParameters.paramList, localctx._block.blk) 
                		
                pass
            elif token in [SetlXgrammarParser.T__65]:
                self.enterOuterAlt(localctx, 3)
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
            self.state = 640
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,45,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 593
                localctx.pp1 = self.procedureParameter(localctx.enableRw)
                localctx.paramList.append(localctx.pp1.param) 
                self.state = 601
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,40,self._ctx)
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1:
                        self.state = 595
                        self.match(SetlXgrammarParser.T__23)
                        self.state = 596
                        localctx.pp2 = self.procedureParameter(localctx.enableRw)
                        localctx.paramList.append(localctx.pp2.param)  
                    self.state = 603
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,40,self._ctx)

                self.state = 610
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,41,self._ctx)
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1:
                        self.state = 604
                        self.match(SetlXgrammarParser.T__23)
                        self.state = 605
                        localctx.dp1 = self.procedureDefaultParameter()
                        localctx.paramList.append(localctx.dp1.param)  
                    self.state = 612
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,41,self._ctx)

                self.state = 617
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==SetlXgrammarParser.T__23:
                    self.state = 613
                    self.match(SetlXgrammarParser.T__23)
                    self.state = 614
                    localctx.lp1 = self.procedureListParameter()
                    localctx.paramList.append(localctx.lp1.param) 


                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 619
                localctx.dp2 = self.procedureDefaultParameter()
                localctx.paramList.append(localctx.dp2.param) 
                self.state = 627
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,43,self._ctx)
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1:
                        self.state = 621
                        self.match(SetlXgrammarParser.T__23)
                        self.state = 622
                        localctx.dp3 = self.procedureDefaultParameter()
                        localctx.paramList.append(localctx.dp3.param)  
                    self.state = 629
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,43,self._ctx)

                self.state = 634
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==SetlXgrammarParser.T__23:
                    self.state = 630
                    self.match(SetlXgrammarParser.T__23)
                    self.state = 631
                    localctx.lp2 = self.procedureListParameter()
                    localctx.paramList.append(localctx.lp2.param) 


                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 636
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
            self.state = 650
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,46,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 642
                if not localctx.enableRw:
                    from antlr4.error.Errors import FailedPredicateException
                    raise FailedPredicateException(self, "$enableRw")
                self.state = 643
                self.match(SetlXgrammarParser.T__66)
                self.state = 644
                localctx._assignableVariable = self.assignableVariable()
                localctx.param = ReadWriteParameter(localctx._assignableVariable.v.id) 
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 647
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
            self.state = 652
            localctx._assignableVariable = self.assignableVariable()
            self.state = 653
            self.match(SetlXgrammarParser.T__30)
            self.state = 654
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
            self.state = 657
            self.match(SetlXgrammarParser.T__51)
            self.state = 658
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
            self.state = 671
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [SetlXgrammarParser.T__1]:
                self.enterOuterAlt(localctx, 1)
                self.state = 661
                self.match(SetlXgrammarParser.T__1)
                self.state = 662
                localctx._callParameters = self.callParameters(localctx.enableIgnore)
                self.state = 663
                self.match(SetlXgrammarParser.T__2)
                localctx.c = FunctionCall(localctx._callParameters.params) 
                		
                pass
            elif token in [SetlXgrammarParser.T__32]:
                self.enterOuterAlt(localctx, 2)
                self.state = 666
                self.match(SetlXgrammarParser.T__32)
                self.state = 667
                localctx._collectionAccessParams = self.collectionAccessParams(localctx.enableIgnore)
                self.state = 668
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
        self.enterRule(localctx, 52, self.RULE_collectionAccessParams)

        params = []
            
        self._la = 0 # Token type
        try:
            self.state = 698
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,51,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 673
                localctx.e1 = self.expr(localctx.enableIgnore)
                self.state = 692
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [SetlXgrammarParser.RANGE_SIGN]:
                    self.state = 674
                    self.match(SetlXgrammarParser.RANGE_SIGN)
                    self.state = 679
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,48,self._ctx)
                    if la_ == 1:
                        self.state = 675
                        localctx.e2 = self.expr(localctx.enableIgnore)
                        localctx.p = ListRange(localctx.e1.ex,localctx.e2.ex) 
                        pass

                    elif la_ == 2:
                        localctx.p = ListRange(localctx.e1.ex,None) 
                        pass


                    pass
                elif token in [SetlXgrammarParser.T__23]:
                    self.state = 685 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    while True:
                        self.state = 681
                        self.match(SetlXgrammarParser.T__23)
                        self.state = 682
                        localctx.e3 = self.expr(False)
                        params.append(localctx.e3.ex) 
                        self.state = 687 
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
                self.state = 694
                self.match(SetlXgrammarParser.RANGE_SIGN)
                self.state = 695
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
            self.state = 714
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,53,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 700
                localctx._exprList = self.exprList(localctx.enableIgnore)
                localctx.params = localctx._exprList.exprs
                self.state = 707
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==SetlXgrammarParser.T__23:
                    self.state = 702
                    self.match(SetlXgrammarParser.T__23)
                    self.state = 703
                    self.match(SetlXgrammarParser.T__51)
                    self.state = 704
                    localctx._exprContent = self.exprContent(False)
                    localctx.params.append(OperatorExpression(localctx._exprContent.ex))


                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 709
                self.match(SetlXgrammarParser.T__51)
                self.state = 710
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
            self.state = 742
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,56,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 716
                self.match(SetlXgrammarParser.T__32)
                self.state = 720
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,54,self._ctx)
                if la_ == 1:
                    self.state = 717
                    localctx._collectionBuilder = self.collectionBuilder(localctx.enableIgnore)
                    cb = localctx._collectionBuilder.cb; 


                self.state = 722
                self.match(SetlXgrammarParser.T__33)
                localctx.v = SetlXList(cb) 
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 724
                self.match(SetlXgrammarParser.T__3)
                self.state = 728
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,55,self._ctx)
                if la_ == 1:
                    self.state = 725
                    localctx._collectionBuilder = self.collectionBuilder(localctx.enableIgnore)
                    cb = localctx._collectionBuilder.cb; 


                self.state = 730
                self.match(SetlXgrammarParser.T__4)
                localctx.v = SetListConstructor(cb) 
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 732
                localctx._STRING = self.match(SetlXgrammarParser.STRING)
                localctx.v = SetlXString((None if localctx._STRING is None else localctx._STRING.text)) 
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 734
                localctx._LITERAL = self.match(SetlXgrammarParser.LITERAL)
                localctx.v = SetlXLiteral((None if localctx._LITERAL is None else localctx._LITERAL.text)) 
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 736
                localctx._atomicValue = self.atomicValue()
                localctx.v = localctx._atomicValue.av 
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 739
                if not localctx.enableIgnore:
                    from antlr4.error.Errors import FailedPredicateException
                    raise FailedPredicateException(self, "$enableIgnore")
                self.state = 740
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
        self.enterRule(localctx, 58, self.RULE_collectionBuilder)

        exprs = []
            
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 744
            localctx.e1 = self.expr(localctx.enableIgnore)
            self.state = 791
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [SetlXgrammarParser.T__23]:
                self.state = 745
                self.match(SetlXgrammarParser.T__23)
                self.state = 746
                localctx.e2 = self.expr(localctx.enableIgnore)
                self.state = 768
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [SetlXgrammarParser.RANGE_SIGN]:
                    self.state = 747
                    self.match(SetlXgrammarParser.RANGE_SIGN)
                    self.state = 748
                    localctx.e3 = self.expr(localctx.enableIgnore)
                    localctx.cb = Range(localctx.e1.ex, localctx.e2.ex, localctx.e3.ex) 
                    pass
                elif token in [SetlXgrammarParser.T__4, SetlXgrammarParser.T__11, SetlXgrammarParser.T__23, SetlXgrammarParser.T__33]:
                    exprs.append(localctx.e1.ex); exprs.append(localctx.e2.ex) 
                    self.state = 758
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    while _la==SetlXgrammarParser.T__23:
                        self.state = 752
                        self.match(SetlXgrammarParser.T__23)
                        self.state = 753
                        localctx.e3 = self.expr(localctx.enableIgnore)
                        exprs.append(localctx.e3.ex) 
                        self.state = 760
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)

                    self.state = 766
                    self._errHandler.sync(self)
                    token = self._input.LA(1)
                    if token in [SetlXgrammarParser.T__11]:
                        self.state = 761
                        self.match(SetlXgrammarParser.T__11)
                        self.state = 762
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
                self.state = 770
                self.match(SetlXgrammarParser.RANGE_SIGN)
                self.state = 771
                localctx.e3 = self.expr(localctx.enableIgnore)
                localctx.cb = Range(localctx.e1.ex, None, localctx.e3.ex) 
                pass
            elif token in [SetlXgrammarParser.T__4, SetlXgrammarParser.T__11, SetlXgrammarParser.T__33]:
                exprs.append(localctx.e1.ex) 
                self.state = 780
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [SetlXgrammarParser.T__11]:
                    self.state = 775
                    self.match(SetlXgrammarParser.T__11)
                    self.state = 776
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
                self.state = 782
                self.match(SetlXgrammarParser.T__8)
                self.state = 783
                localctx._iteratorChain = self.iteratorChain(localctx.enableIgnore)
                self.state = 789
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [SetlXgrammarParser.T__11]:
                    self.state = 784
                    self.match(SetlXgrammarParser.T__11)
                    self.state = 785
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
        self.enterRule(localctx, 60, self.RULE_iteratorChain)

        localctx.ic = []
            
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 793
            localctx.i1 = self.iterator(localctx.enableIgnore)
            localctx.ic.append(localctx.i1.iter)
            self.state = 801
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==SetlXgrammarParser.T__23:
                self.state = 795
                self.match(SetlXgrammarParser.T__23)
                self.state = 796
                localctx.i2 = self.iterator(localctx.enableIgnore)
                localctx.ic.append(localctx.i2.iter) 
                self.state = 803
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
            self.state = 804
            localctx._assignable = self.assignable(True)
            self.state = 805
            self.match(SetlXgrammarParser.T__47)
            self.state = 806
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
            self.state = 819
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [SetlXgrammarParser.NUMBER]:
                self.enterOuterAlt(localctx, 1)
                self.state = 809
                localctx._NUMBER = self.match(SetlXgrammarParser.NUMBER)
                localctx.av = SetlXFraction((None if localctx._NUMBER is None else localctx._NUMBER.text)) 
                pass
            elif token in [SetlXgrammarParser.DOUBLE]:
                self.enterOuterAlt(localctx, 2)
                self.state = 811
                localctx._DOUBLE = self.match(SetlXgrammarParser.DOUBLE)
                localctx.av = float((None if localctx._DOUBLE is None else localctx._DOUBLE.text)) 
                pass
            elif token in [SetlXgrammarParser.T__67]:
                self.enterOuterAlt(localctx, 3)
                self.state = 813
                self.match(SetlXgrammarParser.T__67)
                localctx.av = SetlXOm() 
                pass
            elif token in [SetlXgrammarParser.T__68]:
                self.enterOuterAlt(localctx, 4)
                self.state = 815
                self.match(SetlXgrammarParser.T__68)
                localctx.av = SetlXTrue() 
                pass
            elif token in [SetlXgrammarParser.T__69]:
                self.enterOuterAlt(localctx, 5)
                self.state = 817
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
        self.enterRule(localctx, 66, self.RULE_variable)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 821
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
            self.state = 824
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
            self.state = 827
            localctx.a1 = self.assignable(True)
            localctx.al.append(localctx.a1.a) 
            self.state = 835
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==SetlXgrammarParser.T__23:
                self.state = 829
                self.match(SetlXgrammarParser.T__23)
                self.state = 830
                localctx.a2 = self.assignable(True)
                localctx.al.append(localctx.a2.a) 
                self.state = 837
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
         




