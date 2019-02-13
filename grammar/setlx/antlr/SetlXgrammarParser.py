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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3O")
        buf.write("\u0310\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
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
        buf.write("\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\5\3\u00ba\n\3\3\3\3")
        buf.write("\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\5\3")
        buf.write("\u00ca\n\3\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4")
        buf.write("\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3")
        buf.write("\4\5\4\u00e5\n\4\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3")
        buf.write("\5\3\5\3\5\3\5\5\5\u00f4\n\5\5\5\u00f6\n\5\3\6\3\6\3\6")
        buf.write("\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\7\6\u0103\n\6\f\6\16")
        buf.write("\6\u0106\13\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\5\6\u0110")
        buf.write("\n\6\3\7\3\7\3\7\3\b\3\b\3\b\3\t\3\t\3\t\3\t\3\t\3\t\7")
        buf.write("\t\u011e\n\t\f\t\16\t\u0121\13\t\3\n\3\n\3\n\3\n\3\n\3")
        buf.write("\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n\5\n\u0130\n\n\5\n\u0132")
        buf.write("\n\n\3\13\3\13\3\13\3\13\3\13\3\f\3\f\3\f\3\f\3\f\3\f")
        buf.write("\3\f\3\f\3\f\3\f\7\f\u0143\n\f\f\f\16\f\u0146\13\f\5\f")
        buf.write("\u0148\n\f\3\f\5\f\u014b\n\f\3\r\3\r\3\r\3\r\3\r\3\r\5")
        buf.write("\r\u0153\n\r\3\16\3\16\3\16\3\16\3\16\3\16\7\16\u015b")
        buf.write("\n\16\f\16\16\16\u015e\13\16\3\17\3\17\3\17\3\17\3\17")
        buf.write("\3\17\7\17\u0166\n\17\f\17\16\17\u0169\13\17\3\20\3\20")
        buf.write("\3\20\3\20\3\20\3\20\3\20\3\20\3\20\3\20\3\20\3\20\3\20")
        buf.write("\3\20\3\20\3\20\3\20\3\20\3\20\3\20\3\20\3\20\3\20\3\20")
        buf.write("\3\20\3\20\3\20\3\20\3\20\3\20\3\20\3\20\3\20\3\20\5\20")
        buf.write("\u018d\n\20\3\21\3\21\3\21\3\21\3\21\3\21\3\21\3\21\3")
        buf.write("\21\3\21\7\21\u0199\n\21\f\21\16\21\u019c\13\21\3\22\3")
        buf.write("\22\3\22\3\22\3\22\3\22\3\22\3\22\3\22\3\22\3\22\3\22")
        buf.write("\3\22\3\22\3\22\3\22\3\22\3\22\3\22\3\22\3\22\3\22\7\22")
        buf.write("\u01b4\n\22\f\22\16\22\u01b7\13\22\3\23\3\23\3\23\3\23")
        buf.write("\3\23\3\23\3\23\3\23\3\23\3\23\7\23\u01c3\n\23\f\23\16")
        buf.write("\23\u01c6\13\23\3\24\3\24\3\24\3\24\3\24\3\24\5\24\u01ce")
        buf.write("\n\24\3\24\3\24\3\24\3\24\3\24\3\24\3\24\3\24\3\24\3\24")
        buf.write("\3\24\3\24\3\24\3\24\3\24\3\24\5\24\u01e0\n\24\3\25\3")
        buf.write("\25\3\25\3\25\3\25\3\25\3\25\3\25\3\25\3\25\3\25\3\25")
        buf.write("\3\25\3\25\3\25\3\25\3\25\3\25\3\25\3\25\3\25\3\25\3\25")
        buf.write("\3\25\3\25\3\25\3\25\3\25\3\25\3\25\3\25\5\25\u0201\n")
        buf.write("\25\3\25\3\25\3\25\3\25\3\25\3\25\3\25\7\25\u020a\n\25")
        buf.write("\f\25\16\25\u020d\13\25\3\25\3\25\5\25\u0211\n\25\3\25")
        buf.write("\3\25\3\25\3\25\5\25\u0217\n\25\5\25\u0219\n\25\3\26\3")
        buf.write("\26\3\26\3\26\3\26\3\26\3\26\3\26\3\26\3\26\3\26\3\26")
        buf.write("\3\26\3\26\3\26\3\26\3\26\3\26\3\26\3\26\3\26\3\26\3\26")
        buf.write("\3\26\3\26\3\26\3\26\5\26\u0236\n\26\3\27\3\27\3\27\3")
        buf.write("\27\3\27\3\27\7\27\u023e\n\27\f\27\16\27\u0241\13\27\3")
        buf.write("\27\3\27\3\27\3\27\7\27\u0247\n\27\f\27\16\27\u024a\13")
        buf.write("\27\3\27\3\27\3\27\3\27\3\27\3\27\7\27\u0252\n\27\f\27")
        buf.write("\16\27\u0255\13\27\3\27\5\27\u0258\n\27\3\30\3\30\3\30")
        buf.write("\3\30\3\30\3\30\3\30\3\30\5\30\u0262\n\30\3\31\3\31\3")
        buf.write("\31\3\31\3\31\3\32\3\32\3\32\3\32\3\32\3\32\3\32\3\32")
        buf.write("\3\32\3\32\5\32\u0273\n\32\3\33\3\33\3\33\3\33\3\33\3")
        buf.write("\33\5\33\u027b\n\33\3\33\3\33\3\33\3\33\6\33\u0281\n\33")
        buf.write("\r\33\16\33\u0282\3\33\3\33\3\33\5\33\u0288\n\33\3\33")
        buf.write("\3\33\3\33\3\33\5\33\u028e\n\33\3\34\3\34\3\34\3\34\5")
        buf.write("\34\u0294\n\34\3\35\3\35\3\35\3\35\5\35\u029a\n\35\3\35")
        buf.write("\3\35\3\35\3\35\3\35\3\35\5\35\u02a2\n\35\3\35\3\35\3")
        buf.write("\35\3\35\3\35\3\35\3\35\3\35\3\35\3\35\3\35\3\35\5\35")
        buf.write("\u02b0\n\35\3\36\3\36\3\36\3\36\3\36\3\36\3\36\3\36\3")
        buf.write("\36\3\36\3\36\3\36\7\36\u02be\n\36\f\36\16\36\u02c1\13")
        buf.write("\36\3\36\3\36\3\36\3\36\3\36\5\36\u02c8\n\36\5\36\u02ca")
        buf.write("\n\36\3\36\3\36\3\36\3\36\3\36\3\36\3\36\3\36\3\36\3\36")
        buf.write("\5\36\u02d6\n\36\3\36\3\36\3\36\3\36\3\36\3\36\3\36\5")
        buf.write("\36\u02df\n\36\5\36\u02e1\n\36\3\37\3\37\3\37\3\37\3\37")
        buf.write("\3\37\7\37\u02e9\n\37\f\37\16\37\u02ec\13\37\3 \3 \3 ")
        buf.write("\3 \3 \3!\3!\3!\3!\3!\3!\3!\3!\3!\3!\5!\u02fd\n!\3\"\3")
        buf.write("\"\3\"\3#\3#\3#\3$\3$\3$\3$\3$\3$\7$\u030b\n$\f$\16$\u030e")
        buf.write("\13$\3$\2\2%\2\4\6\b\n\f\16\20\22\24\26\30\32\34\36 \"")
        buf.write("$&(*,.\60\62\64\668:<>@BDF\2\2\2\u0358\2M\3\2\2\2\4\u00c9")
        buf.write("\3\2\2\2\6\u00cb\3\2\2\2\b\u00f5\3\2\2\2\n\u010f\3\2\2")
        buf.write("\2\f\u0111\3\2\2\2\16\u0114\3\2\2\2\20\u0117\3\2\2\2\22")
        buf.write("\u0131\3\2\2\2\24\u0133\3\2\2\2\26\u014a\3\2\2\2\30\u014c")
        buf.write("\3\2\2\2\32\u0154\3\2\2\2\34\u015f\3\2\2\2\36\u016a\3")
        buf.write("\2\2\2 \u018e\3\2\2\2\"\u019d\3\2\2\2$\u01b8\3\2\2\2&")
        buf.write("\u01df\3\2\2\2(\u0218\3\2\2\2*\u0235\3\2\2\2,\u0257\3")
        buf.write("\2\2\2.\u0261\3\2\2\2\60\u0263\3\2\2\2\62\u0272\3\2\2")
        buf.write("\2\64\u028d\3\2\2\2\66\u0293\3\2\2\28\u02af\3\2\2\2:\u02b1")
        buf.write("\3\2\2\2<\u02e2\3\2\2\2>\u02ed\3\2\2\2@\u02fc\3\2\2\2")
        buf.write("B\u02fe\3\2\2\2D\u0301\3\2\2\2F\u0304\3\2\2\2HI\5\4\3")
        buf.write("\2IJ\b\2\1\2JL\3\2\2\2KH\3\2\2\2LO\3\2\2\2MK\3\2\2\2M")
        buf.write("N\3\2\2\2NP\3\2\2\2OM\3\2\2\2PQ\b\2\1\2Q\3\3\2\2\2RS\7")
        buf.write("\3\2\2ST\7\4\2\2TU\5D#\2UV\7\5\2\2VW\7\6\2\2WX\5\2\2\2")
        buf.write("Xe\7\7\2\2YZ\7\b\2\2Z[\7\3\2\2[\\\7\4\2\2\\]\5D#\2]^\7")
        buf.write("\5\2\2^_\7\6\2\2_`\5\2\2\2`a\7\7\2\2ab\b\3\1\2bd\3\2\2")
        buf.write("\2cY\3\2\2\2dg\3\2\2\2ec\3\2\2\2ef\3\2\2\2fn\3\2\2\2g")
        buf.write("e\3\2\2\2hi\7\b\2\2ij\7\6\2\2jk\5\2\2\2kl\7\7\2\2lm\b")
        buf.write("\3\1\2mo\3\2\2\2nh\3\2\2\2no\3\2\2\2op\3\2\2\2pq\b\3\1")
        buf.write("\2q\u00ca\3\2\2\2rs\7\t\2\2s|\7\6\2\2tu\7\n\2\2uv\5D#")
        buf.write("\2vw\7\13\2\2wx\5\2\2\2xy\b\3\1\2y{\3\2\2\2zt\3\2\2\2")
        buf.write("{~\3\2\2\2|z\3\2\2\2|}\3\2\2\2}\u0082\3\2\2\2~|\3\2\2")
        buf.write("\2\177\u0080\7\f\2\2\u0080\u0081\7\13\2\2\u0081\u0083")
        buf.write("\5\2\2\2\u0082\177\3\2\2\2\u0082\u0083\3\2\2\2\u0083\u0084")
        buf.write("\3\2\2\2\u0084\u0085\7\7\2\2\u0085\u00ca\b\3\1\2\u0086")
        buf.write("\u0087\7\r\2\2\u0087\u0088\7\4\2\2\u0088\u008d\5<\37\2")
        buf.write("\u0089\u008a\7\16\2\2\u008a\u008b\5D#\2\u008b\u008c\b")
        buf.write("\3\1\2\u008c\u008e\3\2\2\2\u008d\u0089\3\2\2\2\u008d\u008e")
        buf.write("\3\2\2\2\u008e\u008f\3\2\2\2\u008f\u0090\7\5\2\2\u0090")
        buf.write("\u0091\7\6\2\2\u0091\u0092\5\2\2\2\u0092\u0093\7\7\2\2")
        buf.write("\u0093\u0094\b\3\1\2\u0094\u00ca\3\2\2\2\u0095\u0096\7")
        buf.write("\17\2\2\u0096\u0097\7\4\2\2\u0097\u0098\5D#\2\u0098\u0099")
        buf.write("\7\5\2\2\u0099\u009a\7\6\2\2\u009a\u009b\5\2\2\2\u009b")
        buf.write("\u009c\7\7\2\2\u009c\u009d\b\3\1\2\u009d\u00ca\3\2\2\2")
        buf.write("\u009e\u009f\7\20\2\2\u009f\u00a0\7\6\2\2\u00a0\u00a1")
        buf.write("\5\2\2\2\u00a1\u00a2\7\7\2\2\u00a2\u00a3\7\17\2\2\u00a3")
        buf.write("\u00a4\7\4\2\2\u00a4\u00a5\5D#\2\u00a5\u00a6\7\5\2\2\u00a6")
        buf.write("\u00a7\7\21\2\2\u00a7\u00a8\b\3\1\2\u00a8\u00ca\3\2\2")
        buf.write("\2\u00a9\u00aa\7\22\2\2\u00aa\u00ab\7\21\2\2\u00ab\u00ca")
        buf.write("\b\3\1\2\u00ac\u00ad\7\23\2\2\u00ad\u00ae\7\21\2\2\u00ae")
        buf.write("\u00ca\b\3\1\2\u00af\u00b0\7\24\2\2\u00b0\u00b1\7\21\2")
        buf.write("\2\u00b1\u00ca\b\3\1\2\u00b2\u00b3\7\25\2\2\u00b3\u00b4")
        buf.write("\7\21\2\2\u00b4\u00ca\b\3\1\2\u00b5\u00b9\7\26\2\2\u00b6")
        buf.write("\u00b7\5\16\b\2\u00b7\u00b8\b\3\1\2\u00b8\u00ba\3\2\2")
        buf.write("\2\u00b9\u00b6\3\2\2\2\u00b9\u00ba\3\2\2\2\u00ba\u00bb")
        buf.write("\3\2\2\2\u00bb\u00bc\7\21\2\2\u00bc\u00ca\b\3\1\2\u00bd")
        buf.write("\u00be\5\6\4\2\u00be\u00bf\7\21\2\2\u00bf\u00c0\b\3\1")
        buf.write("\2\u00c0\u00ca\3\2\2\2\u00c1\u00c2\5\b\5\2\u00c2\u00c3")
        buf.write("\7\21\2\2\u00c3\u00c4\b\3\1\2\u00c4\u00ca\3\2\2\2\u00c5")
        buf.write("\u00c6\5\16\b\2\u00c6\u00c7\7\21\2\2\u00c7\u00c8\b\3\1")
        buf.write("\2\u00c8\u00ca\3\2\2\2\u00c9R\3\2\2\2\u00c9r\3\2\2\2\u00c9")
        buf.write("\u0086\3\2\2\2\u00c9\u0095\3\2\2\2\u00c9\u009e\3\2\2\2")
        buf.write("\u00c9\u00a9\3\2\2\2\u00c9\u00ac\3\2\2\2\u00c9\u00af\3")
        buf.write("\2\2\2\u00c9\u00b2\3\2\2\2\u00c9\u00b5\3\2\2\2\u00c9\u00bd")
        buf.write("\3\2\2\2\u00c9\u00c1\3\2\2\2\u00c9\u00c5\3\2\2\2\u00ca")
        buf.write("\5\3\2\2\2\u00cb\u00e4\5\n\6\2\u00cc\u00cd\7\27\2\2\u00cd")
        buf.write("\u00ce\5\16\b\2\u00ce\u00cf\b\4\1\2\u00cf\u00e5\3\2\2")
        buf.write("\2\u00d0\u00d1\7\30\2\2\u00d1\u00d2\5\16\b\2\u00d2\u00d3")
        buf.write("\b\4\1\2\u00d3\u00e5\3\2\2\2\u00d4\u00d5\7\31\2\2\u00d5")
        buf.write("\u00d6\5\16\b\2\u00d6\u00d7\b\4\1\2\u00d7\u00e5\3\2\2")
        buf.write("\2\u00d8\u00d9\7\32\2\2\u00d9\u00da\5\16\b\2\u00da\u00db")
        buf.write("\b\4\1\2\u00db\u00e5\3\2\2\2\u00dc\u00dd\7\33\2\2\u00dd")
        buf.write("\u00de\5\16\b\2\u00de\u00df\b\4\1\2\u00df\u00e5\3\2\2")
        buf.write("\2\u00e0\u00e1\7\34\2\2\u00e1\u00e2\5\16\b\2\u00e2\u00e3")
        buf.write("\b\4\1\2\u00e3\u00e5\3\2\2\2\u00e4\u00cc\3\2\2\2\u00e4")
        buf.write("\u00d0\3\2\2\2\u00e4\u00d4\3\2\2\2\u00e4\u00d8\3\2\2\2")
        buf.write("\u00e4\u00dc\3\2\2\2\u00e4\u00e0\3\2\2\2\u00e5\7\3\2\2")
        buf.write("\2\u00e6\u00e7\5B\"\2\u00e7\u00e8\7\35\2\2\u00e8\u00e9")
        buf.write("\5*\26\2\u00e9\u00ea\b\5\1\2\u00ea\u00f6\3\2\2\2\u00eb")
        buf.write("\u00ec\5\n\6\2\u00ec\u00f3\7\35\2\2\u00ed\u00ee\5\b\5")
        buf.write("\2\u00ee\u00ef\b\5\1\2\u00ef\u00f4\3\2\2\2\u00f0\u00f1")
        buf.write("\5\22\n\2\u00f1\u00f2\b\5\1\2\u00f2\u00f4\3\2\2\2\u00f3")
        buf.write("\u00ed\3\2\2\2\u00f3\u00f0\3\2\2\2\u00f4\u00f6\3\2\2\2")
        buf.write("\u00f5\u00e6\3\2\2\2\u00f5\u00eb\3\2\2\2\u00f6\t\3\2\2")
        buf.write("\2\u00f7\u00f8\5\f\7\2\u00f8\u0104\b\6\1\2\u00f9\u00fa")
        buf.write("\7\36\2\2\u00fa\u00fb\5B\"\2\u00fb\u00fc\b\6\1\2\u00fc")
        buf.write("\u0103\3\2\2\2\u00fd\u00fe\7\37\2\2\u00fe\u00ff\5\20\t")
        buf.write("\2\u00ff\u0100\7 \2\2\u0100\u0101\b\6\1\2\u0101\u0103")
        buf.write("\3\2\2\2\u0102\u00f9\3\2\2\2\u0102\u00fd\3\2\2\2\u0103")
        buf.write("\u0106\3\2\2\2\u0104\u0102\3\2\2\2\u0104\u0105\3\2\2\2")
        buf.write("\u0105\u0110\3\2\2\2\u0106\u0104\3\2\2\2\u0107\u0108\7")
        buf.write("\37\2\2\u0108\u0109\5F$\2\u0109\u010a\7 \2\2\u010a\u010b")
        buf.write("\b\6\1\2\u010b\u0110\3\2\2\2\u010c\u010d\6\6\2\3\u010d")
        buf.write("\u010e\7!\2\2\u010e\u0110\b\6\1\2\u010f\u00f7\3\2\2\2")
        buf.write("\u010f\u0107\3\2\2\2\u010f\u010c\3\2\2\2\u0110\13\3\2")
        buf.write("\2\2\u0111\u0112\7F\2\2\u0112\u0113\b\7\1\2\u0113\r\3")
        buf.write("\2\2\2\u0114\u0115\5\22\n\2\u0115\u0116\b\b\1\2\u0116")
        buf.write("\17\3\2\2\2\u0117\u0118\5\22\n\2\u0118\u011f\b\t\1\2\u0119")
        buf.write("\u011a\7\"\2\2\u011a\u011b\5\22\n\2\u011b\u011c\b\t\1")
        buf.write("\2\u011c\u011e\3\2\2\2\u011d\u0119\3\2\2\2\u011e\u0121")
        buf.write("\3\2\2\2\u011f\u011d\3\2\2\2\u011f\u0120\3\2\2\2\u0120")
        buf.write("\21\3\2\2\2\u0121\u011f\3\2\2\2\u0122\u0123\5\24\13\2")
        buf.write("\u0123\u0124\b\n\1\2\u0124\u0132\3\2\2\2\u0125\u0126\5")
        buf.write("\30\r\2\u0126\u012f\b\n\1\2\u0127\u0128\7#\2\2\u0128\u0129")
        buf.write("\5\30\r\2\u0129\u012a\b\n\1\2\u012a\u0130\3\2\2\2\u012b")
        buf.write("\u012c\7$\2\2\u012c\u012d\5\30\r\2\u012d\u012e\b\n\1\2")
        buf.write("\u012e\u0130\3\2\2\2\u012f\u0127\3\2\2\2\u012f\u012b\3")
        buf.write("\2\2\2\u012f\u0130\3\2\2\2\u0130\u0132\3\2\2\2\u0131\u0122")
        buf.write("\3\2\2\2\u0131\u0125\3\2\2\2\u0132\23\3\2\2\2\u0133\u0134")
        buf.write("\5\26\f\2\u0134\u0135\7%\2\2\u0135\u0136\5\16\b\2\u0136")
        buf.write("\u0137\b\13\1\2\u0137\25\3\2\2\2\u0138\u0139\5B\"\2\u0139")
        buf.write("\u013a\b\f\1\2\u013a\u014b\3\2\2\2\u013b\u0147\7\37\2")
        buf.write("\2\u013c\u013d\5B\"\2\u013d\u0144\b\f\1\2\u013e\u013f")
        buf.write("\7\"\2\2\u013f\u0140\5B\"\2\u0140\u0141\b\f\1\2\u0141")
        buf.write("\u0143\3\2\2\2\u0142\u013e\3\2\2\2\u0143\u0146\3\2\2\2")
        buf.write("\u0144\u0142\3\2\2\2\u0144\u0145\3\2\2\2\u0145\u0148\3")
        buf.write("\2\2\2\u0146\u0144\3\2\2\2\u0147\u013c\3\2\2\2\u0147\u0148")
        buf.write("\3\2\2\2\u0148\u0149\3\2\2\2\u0149\u014b\7 \2\2\u014a")
        buf.write("\u0138\3\2\2\2\u014a\u013b\3\2\2\2\u014b\27\3\2\2\2\u014c")
        buf.write("\u014d\5\32\16\2\u014d\u0152\b\r\1\2\u014e\u014f\7&\2")
        buf.write("\2\u014f\u0150\5\30\r\2\u0150\u0151\b\r\1\2\u0151\u0153")
        buf.write("\3\2\2\2\u0152\u014e\3\2\2\2\u0152\u0153\3\2\2\2\u0153")
        buf.write("\31\3\2\2\2\u0154\u0155\5\34\17\2\u0155\u015c\b\16\1\2")
        buf.write("\u0156\u0157\7\'\2\2\u0157\u0158\5\34\17\2\u0158\u0159")
        buf.write("\b\16\1\2\u0159\u015b\3\2\2\2\u015a\u0156\3\2\2\2\u015b")
        buf.write("\u015e\3\2\2\2\u015c\u015a\3\2\2\2\u015c\u015d\3\2\2\2")
        buf.write("\u015d\33\3\2\2\2\u015e\u015c\3\2\2\2\u015f\u0160\5\36")
        buf.write("\20\2\u0160\u0167\b\17\1\2\u0161\u0162\7(\2\2\u0162\u0163")
        buf.write("\5\36\20\2\u0163\u0164\b\17\1\2\u0164\u0166\3\2\2\2\u0165")
        buf.write("\u0161\3\2\2\2\u0166\u0169\3\2\2\2\u0167\u0165\3\2\2\2")
        buf.write("\u0167\u0168\3\2\2\2\u0168\35\3\2\2\2\u0169\u0167\3\2")
        buf.write("\2\2\u016a\u016b\5 \21\2\u016b\u018c\b\20\1\2\u016c\u016d")
        buf.write("\7)\2\2\u016d\u016e\5 \21\2\u016e\u016f\b\20\1\2\u016f")
        buf.write("\u018d\3\2\2\2\u0170\u0171\7*\2\2\u0171\u0172\5 \21\2")
        buf.write("\u0172\u0173\b\20\1\2\u0173\u018d\3\2\2\2\u0174\u0175")
        buf.write("\7+\2\2\u0175\u0176\5 \21\2\u0176\u0177\b\20\1\2\u0177")
        buf.write("\u018d\3\2\2\2\u0178\u0179\7,\2\2\u0179\u017a\5 \21\2")
        buf.write("\u017a\u017b\b\20\1\2\u017b\u018d\3\2\2\2\u017c\u017d")
        buf.write("\7-\2\2\u017d\u017e\5 \21\2\u017e\u017f\b\20\1\2\u017f")
        buf.write("\u018d\3\2\2\2\u0180\u0181\7.\2\2\u0181\u0182\5 \21\2")
        buf.write("\u0182\u0183\b\20\1\2\u0183\u018d\3\2\2\2\u0184\u0185")
        buf.write("\7/\2\2\u0185\u0186\5 \21\2\u0186\u0187\b\20\1\2\u0187")
        buf.write("\u018d\3\2\2\2\u0188\u0189\7\60\2\2\u0189\u018a\5 \21")
        buf.write("\2\u018a\u018b\b\20\1\2\u018b\u018d\3\2\2\2\u018c\u016c")
        buf.write("\3\2\2\2\u018c\u0170\3\2\2\2\u018c\u0174\3\2\2\2\u018c")
        buf.write("\u0178\3\2\2\2\u018c\u017c\3\2\2\2\u018c\u0180\3\2\2\2")
        buf.write("\u018c\u0184\3\2\2\2\u018c\u0188\3\2\2\2\u018c\u018d\3")
        buf.write("\2\2\2\u018d\37\3\2\2\2\u018e\u018f\5\"\22\2\u018f\u019a")
        buf.write("\b\21\1\2\u0190\u0191\7\61\2\2\u0191\u0192\5\"\22\2\u0192")
        buf.write("\u0193\b\21\1\2\u0193\u0199\3\2\2\2\u0194\u0195\7\62\2")
        buf.write("\2\u0195\u0196\5\"\22\2\u0196\u0197\b\21\1\2\u0197\u0199")
        buf.write("\3\2\2\2\u0198\u0190\3\2\2\2\u0198\u0194\3\2\2\2\u0199")
        buf.write("\u019c\3\2\2\2\u019a\u0198\3\2\2\2\u019a\u019b\3\2\2\2")
        buf.write("\u019b!\3\2\2\2\u019c\u019a\3\2\2\2\u019d\u019e\5$\23")
        buf.write("\2\u019e\u01b5\b\22\1\2\u019f\u01a0\7\63\2\2\u01a0\u01a1")
        buf.write("\5$\23\2\u01a1\u01a2\b\22\1\2\u01a2\u01b4\3\2\2\2\u01a3")
        buf.write("\u01a4\7\64\2\2\u01a4\u01a5\5$\23\2\u01a5\u01a6\b\22\1")
        buf.write("\2\u01a6\u01b4\3\2\2\2\u01a7\u01a8\7\65\2\2\u01a8\u01a9")
        buf.write("\5$\23\2\u01a9\u01aa\b\22\1\2\u01aa\u01b4\3\2\2\2\u01ab")
        buf.write("\u01ac\7\66\2\2\u01ac\u01ad\5$\23\2\u01ad\u01ae\b\22\1")
        buf.write("\2\u01ae\u01b4\3\2\2\2\u01af\u01b0\7\67\2\2\u01b0\u01b1")
        buf.write("\5$\23\2\u01b1\u01b2\b\22\1\2\u01b2\u01b4\3\2\2\2\u01b3")
        buf.write("\u019f\3\2\2\2\u01b3\u01a3\3\2\2\2\u01b3\u01a7\3\2\2\2")
        buf.write("\u01b3\u01ab\3\2\2\2\u01b3\u01af\3\2\2\2\u01b4\u01b7\3")
        buf.write("\2\2\2\u01b5\u01b3\3\2\2\2\u01b5\u01b6\3\2\2\2\u01b6#")
        buf.write("\3\2\2\2\u01b7\u01b5\3\2\2\2\u01b8\u01b9\5&\24\2\u01b9")
        buf.write("\u01c4\b\23\1\2\u01ba\u01bb\78\2\2\u01bb\u01bc\5&\24\2")
        buf.write("\u01bc\u01bd\b\23\1\2\u01bd\u01c3\3\2\2\2\u01be\u01bf")
        buf.write("\79\2\2\u01bf\u01c0\5&\24\2\u01c0\u01c1\b\23\1\2\u01c1")
        buf.write("\u01c3\3\2\2\2\u01c2\u01ba\3\2\2\2\u01c2\u01be\3\2\2\2")
        buf.write("\u01c3\u01c6\3\2\2\2\u01c4\u01c2\3\2\2\2\u01c4\u01c5\3")
        buf.write("\2\2\2\u01c5%\3\2\2\2\u01c6\u01c4\3\2\2\2\u01c7\u01c8")
        buf.write("\5(\25\2\u01c8\u01cd\b\24\1\2\u01c9\u01ca\7:\2\2\u01ca")
        buf.write("\u01cb\5&\24\2\u01cb\u01cc\b\24\1\2\u01cc\u01ce\3\2\2")
        buf.write("\2\u01cd\u01c9\3\2\2\2\u01cd\u01ce\3\2\2\2\u01ce\u01e0")
        buf.write("\3\2\2\2\u01cf\u01d0\78\2\2\u01d0\u01d1\5&\24\2\u01d1")
        buf.write("\u01d2\b\24\1\2\u01d2\u01e0\3\2\2\2\u01d3\u01d4\79\2\2")
        buf.write("\u01d4\u01d5\5&\24\2\u01d5\u01d6\b\24\1\2\u01d6\u01e0")
        buf.write("\3\2\2\2\u01d7\u01d8\7;\2\2\u01d8\u01d9\5&\24\2\u01d9")
        buf.write("\u01da\b\24\1\2\u01da\u01e0\3\2\2\2\u01db\u01dc\7\62\2")
        buf.write("\2\u01dc\u01dd\5&\24\2\u01dd\u01de\b\24\1\2\u01de\u01e0")
        buf.write("\3\2\2\2\u01df\u01c7\3\2\2\2\u01df\u01cf\3\2\2\2\u01df")
        buf.write("\u01d3\3\2\2\2\u01df\u01d7\3\2\2\2\u01df\u01db\3\2\2\2")
        buf.write("\u01e0\'\3\2\2\2\u01e1\u01e2\7<\2\2\u01e2\u01e3\5(\25")
        buf.write("\2\u01e3\u01e4\b\25\1\2\u01e4\u0219\3\2\2\2\u01e5\u01e6")
        buf.write("\7=\2\2\u01e6\u01e7\7\4\2\2\u01e7\u01e8\5<\37\2\u01e8")
        buf.write("\u01e9\7\16\2\2\u01e9\u01ea\5D#\2\u01ea\u01eb\7\5\2\2")
        buf.write("\u01eb\u01ec\b\25\1\2\u01ec\u0219\3\2\2\2\u01ed\u01ee")
        buf.write("\7>\2\2\u01ee\u01ef\7\4\2\2\u01ef\u01f0\5<\37\2\u01f0")
        buf.write("\u01f1\7\16\2\2\u01f1\u01f2\5D#\2\u01f2\u01f3\7\5\2\2")
        buf.write("\u01f3\u01f4\b\25\1\2\u01f4\u0219\3\2\2\2\u01f5\u01f6")
        buf.write("\7\4\2\2\u01f6\u01f7\5\22\n\2\u01f7\u01f8\7\5\2\2\u01f8")
        buf.write("\u01f9\b\25\1\2\u01f9\u0201\3\2\2\2\u01fa\u01fb\5*\26")
        buf.write("\2\u01fb\u01fc\b\25\1\2\u01fc\u0201\3\2\2\2\u01fd\u01fe")
        buf.write("\5B\"\2\u01fe\u01ff\b\25\1\2\u01ff\u0201\3\2\2\2\u0200")
        buf.write("\u01f5\3\2\2\2\u0200\u01fa\3\2\2\2\u0200\u01fd\3\2\2\2")
        buf.write("\u0201\u020b\3\2\2\2\u0202\u0203\7\36\2\2\u0203\u0204")
        buf.write("\5B\"\2\u0204\u0205\b\25\1\2\u0205\u020a\3\2\2\2\u0206")
        buf.write("\u0207\5\62\32\2\u0207\u0208\b\25\1\2\u0208\u020a\3\2")
        buf.write("\2\2\u0209\u0202\3\2\2\2\u0209\u0206\3\2\2\2\u020a\u020d")
        buf.write("\3\2\2\2\u020b\u0209\3\2\2\2\u020b\u020c\3\2\2\2\u020c")
        buf.write("\u0210\3\2\2\2\u020d\u020b\3\2\2\2\u020e\u020f\7<\2\2")
        buf.write("\u020f\u0211\b\25\1\2\u0210\u020e\3\2\2\2\u0210\u0211")
        buf.write("\3\2\2\2\u0211\u0219\3\2\2\2\u0212\u0213\58\35\2\u0213")
        buf.write("\u0216\b\25\1\2\u0214\u0215\7<\2\2\u0215\u0217\b\25\1")
        buf.write("\2\u0216\u0214\3\2\2\2\u0216\u0217\3\2\2\2\u0217\u0219")
        buf.write("\3\2\2\2\u0218\u01e1\3\2\2\2\u0218\u01e5\3\2\2\2\u0218")
        buf.write("\u01ed\3\2\2\2\u0218\u0200\3\2\2\2\u0218\u0212\3\2\2\2")
        buf.write("\u0219)\3\2\2\2\u021a\u021b\7?\2\2\u021b\u021c\7\4\2\2")
        buf.write("\u021c\u021d\5,\27\2\u021d\u021e\7\5\2\2\u021e\u021f\7")
        buf.write("\6\2\2\u021f\u0220\5\2\2\2\u0220\u0221\7\7\2\2\u0221\u0222")
        buf.write("\b\26\1\2\u0222\u0236\3\2\2\2\u0223\u0224\7@\2\2\u0224")
        buf.write("\u0225\7\4\2\2\u0225\u0226\5,\27\2\u0226\u0227\7\5\2\2")
        buf.write("\u0227\u0228\7\6\2\2\u0228\u0229\5\2\2\2\u0229\u022a\7")
        buf.write("\7\2\2\u022a\u022b\b\26\1\2\u022b\u0236\3\2\2\2\u022c")
        buf.write("\u022d\7A\2\2\u022d\u022e\7\4\2\2\u022e\u022f\5,\27\2")
        buf.write("\u022f\u0230\7\5\2\2\u0230\u0231\7\6\2\2\u0231\u0232\5")
        buf.write("\2\2\2\u0232\u0233\7\7\2\2\u0233\u0234\b\26\1\2\u0234")
        buf.write("\u0236\3\2\2\2\u0235\u021a\3\2\2\2\u0235\u0223\3\2\2\2")
        buf.write("\u0235\u022c\3\2\2\2\u0236+\3\2\2\2\u0237\u0238\5.\30")
        buf.write("\2\u0238\u023f\b\27\1\2\u0239\u023a\7\"\2\2\u023a\u023b")
        buf.write("\5.\30\2\u023b\u023c\b\27\1\2\u023c\u023e\3\2\2\2\u023d")
        buf.write("\u0239\3\2\2\2\u023e\u0241\3\2\2\2\u023f\u023d\3\2\2\2")
        buf.write("\u023f\u0240\3\2\2\2\u0240\u0248\3\2\2\2\u0241\u023f\3")
        buf.write("\2\2\2\u0242\u0243\7\"\2\2\u0243\u0244\5\60\31\2\u0244")
        buf.write("\u0245\b\27\1\2\u0245\u0247\3\2\2\2\u0246\u0242\3\2\2")
        buf.write("\2\u0247\u024a\3\2\2\2\u0248\u0246\3\2\2\2\u0248\u0249")
        buf.write("\3\2\2\2\u0249\u0258\3\2\2\2\u024a\u0248\3\2\2\2\u024b")
        buf.write("\u024c\5\60\31\2\u024c\u0253\b\27\1\2\u024d\u024e\7\"")
        buf.write("\2\2\u024e\u024f\5\60\31\2\u024f\u0250\b\27\1\2\u0250")
        buf.write("\u0252\3\2\2\2\u0251\u024d\3\2\2\2\u0252\u0255\3\2\2\2")
        buf.write("\u0253\u0251\3\2\2\2\u0253\u0254\3\2\2\2\u0254\u0258\3")
        buf.write("\2\2\2\u0255\u0253\3\2\2\2\u0256\u0258\3\2\2\2\u0257\u0237")
        buf.write("\3\2\2\2\u0257\u024b\3\2\2\2\u0257\u0256\3\2\2\2\u0258")
        buf.write("-\3\2\2\2\u0259\u025a\6\30\3\3\u025a\u025b\7B\2\2\u025b")
        buf.write("\u025c\5\f\7\2\u025c\u025d\b\30\1\2\u025d\u0262\3\2\2")
        buf.write("\2\u025e\u025f\5B\"\2\u025f\u0260\b\30\1\2\u0260\u0262")
        buf.write("\3\2\2\2\u0261\u0259\3\2\2\2\u0261\u025e\3\2\2\2\u0262")
        buf.write("/\3\2\2\2\u0263\u0264\5\f\7\2\u0264\u0265\7\35\2\2\u0265")
        buf.write("\u0266\5\16\b\2\u0266\u0267\b\31\1\2\u0267\61\3\2\2\2")
        buf.write("\u0268\u0269\7\4\2\2\u0269\u026a\5\66\34\2\u026a\u026b")
        buf.write("\7\5\2\2\u026b\u026c\b\32\1\2\u026c\u0273\3\2\2\2\u026d")
        buf.write("\u026e\7\37\2\2\u026e\u026f\5\64\33\2\u026f\u0270\7 \2")
        buf.write("\2\u0270\u0271\b\32\1\2\u0271\u0273\3\2\2\2\u0272\u0268")
        buf.write("\3\2\2\2\u0272\u026d\3\2\2\2\u0273\63\3\2\2\2\u0274\u0287")
        buf.write("\5\16\b\2\u0275\u027a\7I\2\2\u0276\u0277\5\16\b\2\u0277")
        buf.write("\u0278\b\33\1\2\u0278\u027b\3\2\2\2\u0279\u027b\b\33\1")
        buf.write("\2\u027a\u0276\3\2\2\2\u027a\u0279\3\2\2\2\u027b\u0288")
        buf.write("\3\2\2\2\u027c\u027d\7\"\2\2\u027d\u027e\5\16\b\2\u027e")
        buf.write("\u027f\b\33\1\2\u027f\u0281\3\2\2\2\u0280\u027c\3\2\2")
        buf.write("\2\u0281\u0282\3\2\2\2\u0282\u0280\3\2\2\2\u0282\u0283")
        buf.write("\3\2\2\2\u0283\u0284\3\2\2\2\u0284\u0285\b\33\1\2\u0285")
        buf.write("\u0288\3\2\2\2\u0286\u0288\b\33\1\2\u0287\u0275\3\2\2")
        buf.write("\2\u0287\u0280\3\2\2\2\u0287\u0286\3\2\2\2\u0288\u028e")
        buf.write("\3\2\2\2\u0289\u028a\7I\2\2\u028a\u028b\5\16\b\2\u028b")
        buf.write("\u028c\b\33\1\2\u028c\u028e\3\2\2\2\u028d\u0274\3\2\2")
        buf.write("\2\u028d\u0289\3\2\2\2\u028e\65\3\2\2\2\u028f\u0290\5")
        buf.write("\20\t\2\u0290\u0291\b\34\1\2\u0291\u0294\3\2\2\2\u0292")
        buf.write("\u0294\3\2\2\2\u0293\u028f\3\2\2\2\u0293\u0292\3\2\2\2")
        buf.write("\u0294\67\3\2\2\2\u0295\u0299\7\37\2\2\u0296\u0297\5:")
        buf.write("\36\2\u0297\u0298\b\35\1\2\u0298\u029a\3\2\2\2\u0299\u0296")
        buf.write("\3\2\2\2\u0299\u029a\3\2\2\2\u029a\u029b\3\2\2\2\u029b")
        buf.write("\u029c\7 \2\2\u029c\u02b0\b\35\1\2\u029d\u02a1\7\6\2\2")
        buf.write("\u029e\u029f\5:\36\2\u029f\u02a0\b\35\1\2\u02a0\u02a2")
        buf.write("\3\2\2\2\u02a1\u029e\3\2\2\2\u02a1\u02a2\3\2\2\2\u02a2")
        buf.write("\u02a3\3\2\2\2\u02a3\u02a4\7\7\2\2\u02a4\u02b0\b\35\1")
        buf.write("\2\u02a5\u02a6\7J\2\2\u02a6\u02b0\b\35\1\2\u02a7\u02a8")
        buf.write("\7K\2\2\u02a8\u02b0\b\35\1\2\u02a9\u02aa\5@!\2\u02aa\u02ab")
        buf.write("\b\35\1\2\u02ab\u02b0\3\2\2\2\u02ac\u02ad\6\35\4\3\u02ad")
        buf.write("\u02ae\7!\2\2\u02ae\u02b0\b\35\1\2\u02af\u0295\3\2\2\2")
        buf.write("\u02af\u029d\3\2\2\2\u02af\u02a5\3\2\2\2\u02af\u02a7\3")
        buf.write("\2\2\2\u02af\u02a9\3\2\2\2\u02af\u02ac\3\2\2\2\u02b09")
        buf.write("\3\2\2\2\u02b1\u02e0\5\16\b\2\u02b2\u02b3\7\"\2\2\u02b3")
        buf.write("\u02c9\5\16\b\2\u02b4\u02b5\7I\2\2\u02b5\u02b6\5\16\b")
        buf.write("\2\u02b6\u02b7\b\36\1\2\u02b7\u02ca\3\2\2\2\u02b8\u02bf")
        buf.write("\b\36\1\2\u02b9\u02ba\7\"\2\2\u02ba\u02bb\5\16\b\2\u02bb")
        buf.write("\u02bc\b\36\1\2\u02bc\u02be\3\2\2\2\u02bd\u02b9\3\2\2")
        buf.write("\2\u02be\u02c1\3\2\2\2\u02bf\u02bd\3\2\2\2\u02bf\u02c0")
        buf.write("\3\2\2\2\u02c0\u02c7\3\2\2\2\u02c1\u02bf\3\2\2\2\u02c2")
        buf.write("\u02c3\7\16\2\2\u02c3\u02c4\5\16\b\2\u02c4\u02c5\b\36")
        buf.write("\1\2\u02c5\u02c8\3\2\2\2\u02c6\u02c8\b\36\1\2\u02c7\u02c2")
        buf.write("\3\2\2\2\u02c7\u02c6\3\2\2\2\u02c8\u02ca\3\2\2\2\u02c9")
        buf.write("\u02b4\3\2\2\2\u02c9\u02b8\3\2\2\2\u02ca\u02e1\3\2\2\2")
        buf.write("\u02cb\u02cc\7I\2\2\u02cc\u02cd\5\16\b\2\u02cd\u02ce\b")
        buf.write("\36\1\2\u02ce\u02e1\3\2\2\2\u02cf\u02d5\b\36\1\2\u02d0")
        buf.write("\u02d1\7\16\2\2\u02d1\u02d2\5\16\b\2\u02d2\u02d3\b\36")
        buf.write("\1\2\u02d3\u02d6\3\2\2\2\u02d4\u02d6\b\36\1\2\u02d5\u02d0")
        buf.write("\3\2\2\2\u02d5\u02d4\3\2\2\2\u02d6\u02e1\3\2\2\2\u02d7")
        buf.write("\u02d8\7\13\2\2\u02d8\u02de\5<\37\2\u02d9\u02da\7\16\2")
        buf.write("\2\u02da\u02db\5D#\2\u02db\u02dc\b\36\1\2\u02dc\u02df")
        buf.write("\3\2\2\2\u02dd\u02df\b\36\1\2\u02de\u02d9\3\2\2\2\u02de")
        buf.write("\u02dd\3\2\2\2\u02df\u02e1\3\2\2\2\u02e0\u02b2\3\2\2\2")
        buf.write("\u02e0\u02cb\3\2\2\2\u02e0\u02cf\3\2\2\2\u02e0\u02d7\3")
        buf.write("\2\2\2\u02e1;\3\2\2\2\u02e2\u02e3\5> \2\u02e3\u02ea\b")
        buf.write("\37\1\2\u02e4\u02e5\7\"\2\2\u02e5\u02e6\5> \2\u02e6\u02e7")
        buf.write("\b\37\1\2\u02e7\u02e9\3\2\2\2\u02e8\u02e4\3\2\2\2\u02e9")
        buf.write("\u02ec\3\2\2\2\u02ea\u02e8\3\2\2\2\u02ea\u02eb\3\2\2\2")
        buf.write("\u02eb=\3\2\2\2\u02ec\u02ea\3\2\2\2\u02ed\u02ee\5\n\6")
        buf.write("\2\u02ee\u02ef\7/\2\2\u02ef\u02f0\5\16\b\2\u02f0\u02f1")
        buf.write("\b \1\2\u02f1?\3\2\2\2\u02f2\u02f3\7G\2\2\u02f3\u02fd")
        buf.write("\b!\1\2\u02f4\u02f5\7H\2\2\u02f5\u02fd\b!\1\2\u02f6\u02f7")
        buf.write("\7C\2\2\u02f7\u02fd\b!\1\2\u02f8\u02f9\7D\2\2\u02f9\u02fd")
        buf.write("\b!\1\2\u02fa\u02fb\7E\2\2\u02fb\u02fd\b!\1\2\u02fc\u02f2")
        buf.write("\3\2\2\2\u02fc\u02f4\3\2\2\2\u02fc\u02f6\3\2\2\2\u02fc")
        buf.write("\u02f8\3\2\2\2\u02fc\u02fa\3\2\2\2\u02fdA\3\2\2\2\u02fe")
        buf.write("\u02ff\7F\2\2\u02ff\u0300\b\"\1\2\u0300C\3\2\2\2\u0301")
        buf.write("\u0302\5\16\b\2\u0302\u0303\b#\1\2\u0303E\3\2\2\2\u0304")
        buf.write("\u0305\5\n\6\2\u0305\u030c\b$\1\2\u0306\u0307\7\"\2\2")
        buf.write("\u0307\u0308\5\n\6\2\u0308\u0309\b$\1\2\u0309\u030b\3")
        buf.write("\2\2\2\u030a\u0306\3\2\2\2\u030b\u030e\3\2\2\2\u030c\u030a")
        buf.write("\3\2\2\2\u030c\u030d\3\2\2\2\u030dG\3\2\2\2\u030e\u030c")
        buf.write("\3\2\2\2@Men|\u0082\u008d\u00b9\u00c9\u00e4\u00f3\u00f5")
        buf.write("\u0102\u0104\u010f\u011f\u012f\u0131\u0144\u0147\u014a")
        buf.write("\u0152\u015c\u0167\u018c\u0198\u019a\u01b3\u01b5\u01c2")
        buf.write("\u01c4\u01cd\u01df\u0200\u0209\u020b\u0210\u0216\u0218")
        buf.write("\u0235\u023f\u0248\u0253\u0257\u0261\u0272\u027a\u0282")
        buf.write("\u0287\u028d\u0293\u0299\u02a1\u02af\u02bf\u02c7\u02c9")
        buf.write("\u02d5\u02de\u02e0\u02ea\u02fc\u030c")
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
                     "']'", "'_'", "','", "'<==>'", "'<!=>'", "'|=>'", "'=>'", 
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
                      "ID", "NUMBER", "DOUBLE", "RANGE_SIGN", "STRING", 
                      "LITERAL", "LINE_COMMENT", "MULTI_COMMENT", "WS", 
                      "REMAINDER" ]

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
    ID=68
    NUMBER=69
    DOUBLE=70
    RANGE_SIGN=71
    STRING=72
    LITERAL=73
    LINE_COMMENT=74
    MULTI_COMMENT=75
    WS=76
    REMAINDER=77

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
            self.state = 199
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,7,self._ctx)
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
                self.match(SetlXgrammarParser.T__14)
                localctx.stmnt = Backtrack() 
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 170
                self.match(SetlXgrammarParser.T__16)
                self.state = 171
                self.match(SetlXgrammarParser.T__14)
                localctx.stmnt = Break() 
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 173
                self.match(SetlXgrammarParser.T__17)
                self.state = 174
                self.match(SetlXgrammarParser.T__14)
                localctx.stmnt = Continue() 
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 176
                self.match(SetlXgrammarParser.T__18)
                self.state = 177
                self.match(SetlXgrammarParser.T__14)
                localctx.stmnt = Exit() 
                pass

            elif la_ == 10:
                self.enterOuterAlt(localctx, 10)
                self.state = 179
                self.match(SetlXgrammarParser.T__19)
                self.state = 183
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,6,self._ctx)
                if la_ == 1:
                    self.state = 180
                    localctx._expr = self.expr(False)
                    expression = localctx._expr.ex 


                self.state = 185
                self.match(SetlXgrammarParser.T__14)
                localctx.stmnt = Return(expression) 
                pass

            elif la_ == 11:
                self.enterOuterAlt(localctx, 11)
                self.state = 187
                localctx._assignmentOther = self.assignmentOther()
                self.state = 188
                self.match(SetlXgrammarParser.T__14)
                localctx.stmnt = localctx._assignmentOther.assign 
                pass

            elif la_ == 12:
                self.enterOuterAlt(localctx, 12)
                self.state = 191
                localctx._assignmentDirect = self.assignmentDirect()
                self.state = 192
                self.match(SetlXgrammarParser.T__14)
                localctx.stmnt = localctx._assignmentDirect.assign 
                pass

            elif la_ == 13:
                self.enterOuterAlt(localctx, 13)
                self.state = 195
                localctx._expr = self.expr(False)
                self.state = 196
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
            self.state = 201
            localctx._assignable = self.assignable(False)
            self.state = 226
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [SetlXgrammarParser.T__20]:
                self.state = 202
                self.match(SetlXgrammarParser.T__20)
                self.state = 203
                localctx.e = self.expr(False)
                localctx.assign = SumAssignment(localctx._assignable.a, localctx.e.ex) 
                pass
            elif token in [SetlXgrammarParser.T__21]:
                self.state = 206
                self.match(SetlXgrammarParser.T__21)
                self.state = 207
                localctx.e = self.expr(False)
                localctx.assign = DifferenceAssignment(localctx._assignable.a, localctx.e.ex) 
                pass
            elif token in [SetlXgrammarParser.T__22]:
                self.state = 210
                self.match(SetlXgrammarParser.T__22)
                self.state = 211
                localctx.e = self.expr(False)
                localctx.assign = ProductAssignment(localctx._assignable.a, localctx.e.ex) 
                pass
            elif token in [SetlXgrammarParser.T__23]:
                self.state = 214
                self.match(SetlXgrammarParser.T__23)
                self.state = 215
                localctx.e = self.expr(False)
                localctx.assign = QuotientAssignment(localctx._assignable.a, localctx.e.ex) 
                pass
            elif token in [SetlXgrammarParser.T__24]:
                self.state = 218
                self.match(SetlXgrammarParser.T__24)
                self.state = 219
                localctx.e = self.expr(False)
                localctx.assign = IntegerDivisionAssignment(localctx._assignable.a, localctx.e.ex) 
                pass
            elif token in [SetlXgrammarParser.T__25]:
                self.state = 222
                self.match(SetlXgrammarParser.T__25)
                self.state = 223
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
            self.state = 243
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,10,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 228
                localctx._variable = self.variable()
                self.state = 229
                self.match(SetlXgrammarParser.T__26)
                self.state = 230
                localctx._procedure = self.procedure()

                localctx._procedure.pd.name = localctx._variable.v.id
                localctx.assign = localctx._procedure.pd
                    
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 233
                localctx._assignable = self.assignable(False)
                self.state = 234
                self.match(SetlXgrammarParser.T__26)
                self.state = 241
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,9,self._ctx)
                if la_ == 1:
                    self.state = 235
                    localctx._assignmentDirect = self.assignmentDirect()
                    localctx.assign = Assignment(localctx._assignable.a, localctx._assignmentDirect.assign) 
                    pass

                elif la_ == 2:
                    self.state = 238
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
            self.state = 269
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,13,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 245
                localctx._assignableVariable = self.assignableVariable()
                localctx.a = localctx._assignableVariable.v
                self.state = 258
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==SetlXgrammarParser.T__27 or _la==SetlXgrammarParser.T__28:
                    self.state = 256
                    self._errHandler.sync(self)
                    token = self._input.LA(1)
                    if token in [SetlXgrammarParser.T__27]:
                        self.state = 247
                        self.match(SetlXgrammarParser.T__27)
                        self.state = 248
                        localctx._variable = self.variable()
                        localctx.a = AssignableMember(localctx.a, localctx._variable.v)
                        pass
                    elif token in [SetlXgrammarParser.T__28]:
                        self.state = 251
                        self.match(SetlXgrammarParser.T__28)
                        self.state = 252
                        localctx._exprList = self.exprList(False)
                        self.state = 253
                        self.match(SetlXgrammarParser.T__29)
                        localctx.a = AssignableCollectionAccess(localctx.a, localctx._exprList.exprs)
                        pass
                    else:
                        raise NoViableAltException(self)

                    self.state = 260
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 261
                self.match(SetlXgrammarParser.T__28)
                self.state = 262
                localctx._assignmentList = self.assignmentList()
                self.state = 263
                self.match(SetlXgrammarParser.T__29)
                localctx.a = AssignableList(localctx._assignmentList.al)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 266
                if not localctx.enableIgnore:
                    from antlr4.error.Errors import FailedPredicateException
                    raise FailedPredicateException(self, "$enableIgnore")
                self.state = 267
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
            self.state = 271
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
            self.state = 274
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
            self.state = 277
            localctx._exprContent = self.exprContent(localctx.enableIgnore)
            localctx.exprs.append(localctx._exprContent.ex)
            self.state = 285
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==SetlXgrammarParser.T__31:
                self.state = 279
                self.match(SetlXgrammarParser.T__31)
                self.state = 280
                localctx._exprContent = self.exprContent(localctx.enableIgnore)
                localctx.exprs.append(localctx._exprContent.ex)
                self.state = 287
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
            self.state = 303
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,16,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 288
                localctx._lambdaProcedure = self.lambdaProcedure()
                localctx.ex = localctx._lambdaProcedure.lp 
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 291
                localctx._implication = self.implication(localctx.enableIgnore)
                localctx.ex = localctx._implication.i
                self.state = 301
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [SetlXgrammarParser.T__32]:
                    self.state = 293
                    self.match(SetlXgrammarParser.T__32)
                    self.state = 294
                    localctx._implication = self.implication(localctx.enableIgnore)
                    localctx.ex = BooleanEqual(localctx.ex,localctx._implication.i) 
                    pass
                elif token in [SetlXgrammarParser.T__33]:
                    self.state = 297
                    self.match(SetlXgrammarParser.T__33)
                    self.state = 298
                    localctx._implication = self.implication(localctx.enableIgnore)
                    localctx.ex = BooleanNotEqual(localctx.ex,localctx._implication.i) 
                    pass
                elif token in [SetlXgrammarParser.T__2, SetlXgrammarParser.T__4, SetlXgrammarParser.T__8, SetlXgrammarParser.T__11, SetlXgrammarParser.T__14, SetlXgrammarParser.T__29, SetlXgrammarParser.T__31, SetlXgrammarParser.RANGE_SIGN]:
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
            self.state = 305
            localctx._lambdaParameters = self.lambdaParameters()

            self.state = 306
            self.match(SetlXgrammarParser.T__34)
            self.state = 307
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
            self.state = 328
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [SetlXgrammarParser.ID]:
                self.enterOuterAlt(localctx, 1)
                self.state = 310
                localctx._variable = self.variable()
                localctx.paramList.append(Parameter(localctx._variable.v.id)) 
                pass
            elif token in [SetlXgrammarParser.T__28]:
                self.enterOuterAlt(localctx, 2)
                self.state = 313
                self.match(SetlXgrammarParser.T__28)
                self.state = 325
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==SetlXgrammarParser.ID:
                    self.state = 314
                    localctx.v1 = self.variable()
                    localctx.paramList.append(Parameter(localctx.v1.v.id))
                    self.state = 322
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    while _la==SetlXgrammarParser.T__31:
                        self.state = 316
                        self.match(SetlXgrammarParser.T__31)
                        self.state = 317
                        localctx.v2 = self.variable()
                        localctx.paramList.append(Parameter(localctx.v2.v.id))
                        self.state = 324
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)



                self.state = 327
                self.match(SetlXgrammarParser.T__29)
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
            self.state = 330
            localctx._disjunction = self.disjunction(localctx.enableIgnore)
            localctx.i = localctx._disjunction.d
            self.state = 336
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==SetlXgrammarParser.T__35:
                self.state = 332
                self.match(SetlXgrammarParser.T__35)
                self.state = 333
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
            self.state = 338
            localctx._conjunction = self.conjunction(localctx.enableIgnore)
            localctx.d = localctx._conjunction.c
            self.state = 346
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==SetlXgrammarParser.T__36:
                self.state = 340
                self.match(SetlXgrammarParser.T__36)
                self.state = 341
                localctx._conjunction = self.conjunction(localctx.enableIgnore)
                localctx.d = Disjunction(localctx.d, localctx._conjunction.c) 
                self.state = 348
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
            self.state = 349
            localctx._comparison = self.comparison(localctx.enableIgnore)
            localctx.c = localctx._comparison.c
            self.state = 357
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==SetlXgrammarParser.T__37:
                self.state = 351
                self.match(SetlXgrammarParser.T__37)
                self.state = 352
                localctx._comparison = self.comparison(localctx.enableIgnore)
                localctx.c = Conjunction(localctx.c, localctx._comparison.c) 
                self.state = 359
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
            self.state = 360
            localctx.s1 = self.setlxSum(localctx.enableIgnore)
            localctx.c = localctx.s1.s 
            self.state = 394
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [SetlXgrammarParser.T__38]:
                self.state = 362
                self.match(SetlXgrammarParser.T__38)
                self.state = 363
                localctx.s2 = self.setlxSum(localctx.enableIgnore)
                localctx.c = Equal(localctx.s1.s,localctx.s2.s) 
                pass
            elif token in [SetlXgrammarParser.T__39]:
                self.state = 366
                self.match(SetlXgrammarParser.T__39)
                self.state = 367
                localctx.s2 = self.setlxSum(localctx.enableIgnore)
                localctx.c = NotEqual(localctx.s1.s,localctx.s2.s) 
                pass
            elif token in [SetlXgrammarParser.T__40]:
                self.state = 370
                self.match(SetlXgrammarParser.T__40)
                self.state = 371
                localctx.s2 = self.setlxSum(localctx.enableIgnore)
                localctx.c = LessThan(localctx.s1.s,localctx.s2.s) 
                pass
            elif token in [SetlXgrammarParser.T__41]:
                self.state = 374
                self.match(SetlXgrammarParser.T__41)
                self.state = 375
                localctx.s2 = self.setlxSum(localctx.enableIgnore)
                localctx.c = LessOrEqual(localctx.s1.s,localctx.s2.s) 
                pass
            elif token in [SetlXgrammarParser.T__42]:
                self.state = 378
                self.match(SetlXgrammarParser.T__42)
                self.state = 379
                localctx.s2 = self.setlxSum(localctx.enableIgnore)
                localctx.c = GreaterThan(localctx.s1.s,localctx.s2.s) 
                pass
            elif token in [SetlXgrammarParser.T__43]:
                self.state = 382
                self.match(SetlXgrammarParser.T__43)
                self.state = 383
                localctx.s2 = self.setlxSum(localctx.enableIgnore)
                localctx.c = GreaterOrEqual(localctx.s1.s,localctx.s2.s) 
                pass
            elif token in [SetlXgrammarParser.T__44]:
                self.state = 386
                self.match(SetlXgrammarParser.T__44)
                self.state = 387
                localctx.s2 = self.setlxSum(localctx.enableIgnore)
                localctx.c = In(localctx.s1.s,localctx.s2.s) 
                pass
            elif token in [SetlXgrammarParser.T__45]:
                self.state = 390
                self.match(SetlXgrammarParser.T__45)
                self.state = 391
                localctx.s2 = self.setlxSum(localctx.enableIgnore)
                localctx.c = NotIn(localctx.s1.s,localctx.s2.s) 
                pass
            elif token in [SetlXgrammarParser.T__2, SetlXgrammarParser.T__4, SetlXgrammarParser.T__8, SetlXgrammarParser.T__11, SetlXgrammarParser.T__14, SetlXgrammarParser.T__29, SetlXgrammarParser.T__31, SetlXgrammarParser.T__32, SetlXgrammarParser.T__33, SetlXgrammarParser.T__35, SetlXgrammarParser.T__36, SetlXgrammarParser.T__37, SetlXgrammarParser.RANGE_SIGN]:
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
            self.state = 396
            localctx.p1 = self.product(localctx.enableIgnore)
            localctx.s = localctx.p1.p
            self.state = 408
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==SetlXgrammarParser.T__46 or _la==SetlXgrammarParser.T__47:
                self.state = 406
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [SetlXgrammarParser.T__46]:
                    self.state = 398
                    self.match(SetlXgrammarParser.T__46)
                    self.state = 399
                    localctx.p2 = self.product(localctx.enableIgnore)
                    localctx.s = Sum(localctx.p1.p,localctx.p2.p) 
                    pass
                elif token in [SetlXgrammarParser.T__47]:
                    self.state = 402
                    self.match(SetlXgrammarParser.T__47)
                    self.state = 403
                    localctx.p2 = self.product(localctx.enableIgnore)
                    localctx.s = Difference(localctx.p1.p,localctx.p2.p) 
                    pass
                else:
                    raise NoViableAltException(self)

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
            self.state = 411
            localctx.r1 = self.setlxReduce(localctx.enableIgnore)
            localctx.p = localctx.r1.r
            self.state = 435
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << SetlXgrammarParser.T__48) | (1 << SetlXgrammarParser.T__49) | (1 << SetlXgrammarParser.T__50) | (1 << SetlXgrammarParser.T__51) | (1 << SetlXgrammarParser.T__52))) != 0):
                self.state = 433
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [SetlXgrammarParser.T__48]:
                    self.state = 413
                    self.match(SetlXgrammarParser.T__48)
                    self.state = 414
                    localctx.r2 = self.setlxReduce(localctx.enableIgnore)
                    localctx.p = Product(localctx.p,localctx.r2.r) 
                    pass
                elif token in [SetlXgrammarParser.T__49]:
                    self.state = 417
                    self.match(SetlXgrammarParser.T__49)
                    self.state = 418
                    localctx.r2 = self.setlxReduce(localctx.enableIgnore)
                    localctx.p = Quotient(localctx.p,localctx.r2.r) 
                    pass
                elif token in [SetlXgrammarParser.T__50]:
                    self.state = 421
                    self.match(SetlXgrammarParser.T__50)
                    self.state = 422
                    localctx.r2 = self.setlxReduce(localctx.enableIgnore)
                    localctx.p = IntegerDivision(localctx.p,localctx.r2.r) 
                    pass
                elif token in [SetlXgrammarParser.T__51]:
                    self.state = 425
                    self.match(SetlXgrammarParser.T__51)
                    self.state = 426
                    localctx.r2 = self.setlxReduce(localctx.enableIgnore)
                    localctx.p = Modulo(localctx.p,localctx.r2.r) 
                    pass
                elif token in [SetlXgrammarParser.T__52]:
                    self.state = 429
                    self.match(SetlXgrammarParser.T__52)
                    self.state = 430
                    localctx.r2 = self.setlxReduce(localctx.enableIgnore)
                    localctx.p = CartesianProduct(localctx.p,localctx.r2.r) 
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 437
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
            self.state = 438
            localctx.p1 = self.prefixOperation(localctx.enableIgnore)
            localctx.r = localctx.p1.p
            self.state = 450
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==SetlXgrammarParser.T__53 or _la==SetlXgrammarParser.T__54:
                self.state = 448
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [SetlXgrammarParser.T__53]:
                    self.state = 440
                    self.match(SetlXgrammarParser.T__53)
                    self.state = 441
                    localctx.p2 = self.prefixOperation(localctx.enableIgnore)
                    localctx.r = SumOfMembersBinary(localctx.r,localctx.p2.p) 
                    pass
                elif token in [SetlXgrammarParser.T__54]:
                    self.state = 444
                    self.match(SetlXgrammarParser.T__54)
                    self.state = 445
                    localctx.p2 = self.prefixOperation(localctx.enableIgnore)
                    localctx.r = ProductOfMembersBinary(localctx.r,localctx.p2.p) 
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 452
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
            self.state = 477
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,31,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 453
                localctx._factor = self.factor(localctx.enableIgnore)
                localctx.p = localctx._factor.f
                self.state = 459
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==SetlXgrammarParser.T__55:
                    self.state = 455
                    self.match(SetlXgrammarParser.T__55)
                    self.state = 456
                    localctx._prefixOperation = self.prefixOperation(localctx.enableIgnore)
                    localctx.p = Power(localctx.p,localctx._prefixOperation.p) 


                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 461
                self.match(SetlXgrammarParser.T__53)
                self.state = 462
                localctx._prefixOperation = self.prefixOperation(localctx.enableIgnore)
                localctx.p = SumOfMembers(localctx._prefixOperation.p) 
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 465
                self.match(SetlXgrammarParser.T__54)
                self.state = 466
                localctx._prefixOperation = self.prefixOperation(localctx.enableIgnore)
                localctx.p = ProductOfMembers(localctx._prefixOperation.p) 
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 469
                self.match(SetlXgrammarParser.T__56)
                self.state = 470
                localctx._prefixOperation = self.prefixOperation(localctx.enableIgnore)
                localctx.p = Cardinality(localctx._prefixOperation.p) 
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 473
                self.match(SetlXgrammarParser.T__47)
                self.state = 474
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
            self.state = 534
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,37,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 479
                self.match(SetlXgrammarParser.T__57)
                self.state = 480
                localctx._factor = self.factor(localctx.enableIgnore)
                localctx.f = Not(localctx._factor.f) 
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 483
                self.match(SetlXgrammarParser.T__58)
                self.state = 484
                self.match(SetlXgrammarParser.T__1)
                self.state = 485
                localctx._iteratorChain = self.iteratorChain(localctx.enableIgnore)
                self.state = 486
                self.match(SetlXgrammarParser.T__11)
                self.state = 487
                localctx._condition = self.condition()
                self.state = 488
                self.match(SetlXgrammarParser.T__2)
                localctx.f = Forall(localctx._iteratorChain.ic,localctx._condition.cnd)
                		
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 491
                self.match(SetlXgrammarParser.T__59)
                self.state = 492
                self.match(SetlXgrammarParser.T__1)
                self.state = 493
                localctx._iteratorChain = self.iteratorChain(localctx.enableIgnore)
                self.state = 494
                self.match(SetlXgrammarParser.T__11)
                self.state = 495
                localctx._condition = self.condition()
                self.state = 496
                self.match(SetlXgrammarParser.T__2)
                localctx.f = Exists(localctx._iteratorChain.ic,localctx._condition.cnd)
                		
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 510
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [SetlXgrammarParser.T__1]:
                    self.state = 499
                    self.match(SetlXgrammarParser.T__1)
                    self.state = 500
                    localctx._exprContent = self.exprContent(localctx.enableIgnore)
                    self.state = 501
                    self.match(SetlXgrammarParser.T__2)
                    localctx.f = localctx._exprContent.ex 
                    pass
                elif token in [SetlXgrammarParser.T__60, SetlXgrammarParser.T__61, SetlXgrammarParser.T__62]:
                    self.state = 504
                    localctx._procedure = self.procedure()
                    localctx.f = localctx._procedure.pd 
                    pass
                elif token in [SetlXgrammarParser.ID]:
                    self.state = 507
                    localctx._variable = self.variable()
                    localctx.f = localctx._variable.v 
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 521
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << SetlXgrammarParser.T__1) | (1 << SetlXgrammarParser.T__27) | (1 << SetlXgrammarParser.T__28))) != 0):
                    self.state = 519
                    self._errHandler.sync(self)
                    token = self._input.LA(1)
                    if token in [SetlXgrammarParser.T__27]:
                        self.state = 512
                        self.match(SetlXgrammarParser.T__27)
                        self.state = 513
                        localctx._variable = self.variable()
                        localctx.f = MemberAccess(localctx.f,localctx._variable.v) 
                        pass
                    elif token in [SetlXgrammarParser.T__1, SetlXgrammarParser.T__28]:
                        self.state = 516
                        localctx._call = self.call(localctx.enableIgnore)

                        localctx._call.c.callable = localctx.f
                        localctx.f = localctx._call.c
                                
                        pass
                    else:
                        raise NoViableAltException(self)

                    self.state = 523
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 526
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==SetlXgrammarParser.T__57:
                    self.state = 524
                    self.match(SetlXgrammarParser.T__57)
                    localctx.f = Factorial(localctx.f) 


                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 528
                localctx._value = self.value(localctx.enableIgnore)
                localctx.f = localctx._value.v 
                self.state = 532
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==SetlXgrammarParser.T__57:
                    self.state = 530
                    self.match(SetlXgrammarParser.T__57)
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
            self.state = 563
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [SetlXgrammarParser.T__60]:
                self.enterOuterAlt(localctx, 1)
                self.state = 536
                self.match(SetlXgrammarParser.T__60)
                self.state = 537
                self.match(SetlXgrammarParser.T__1)
                self.state = 538
                localctx._procedureParameters = self.procedureParameters(True)
                self.state = 539
                self.match(SetlXgrammarParser.T__2)
                self.state = 540
                self.match(SetlXgrammarParser.T__3)
                self.state = 541
                localctx._block = self.block()
                self.state = 542
                self.match(SetlXgrammarParser.T__4)
                localctx.pd = Procedure(localctx._procedureParameters.paramList, localctx._block.blk) 
                		
                pass
            elif token in [SetlXgrammarParser.T__61]:
                self.enterOuterAlt(localctx, 2)
                self.state = 545
                self.match(SetlXgrammarParser.T__61)
                self.state = 546
                self.match(SetlXgrammarParser.T__1)
                self.state = 547
                localctx._procedureParameters = self.procedureParameters(False)
                self.state = 548
                self.match(SetlXgrammarParser.T__2)
                self.state = 549
                self.match(SetlXgrammarParser.T__3)
                self.state = 550
                localctx._block = self.block()
                self.state = 551
                self.match(SetlXgrammarParser.T__4)
                localctx.pd = CachedProcedure(localctx._procedureParameters.paramList, localctx._block.blk) 
                		
                pass
            elif token in [SetlXgrammarParser.T__62]:
                self.enterOuterAlt(localctx, 3)
                self.state = 554
                self.match(SetlXgrammarParser.T__62)
                self.state = 555
                self.match(SetlXgrammarParser.T__1)
                self.state = 556
                localctx._procedureParameters = self.procedureParameters(True)
                self.state = 557
                self.match(SetlXgrammarParser.T__2)
                self.state = 558
                self.match(SetlXgrammarParser.T__3)
                self.state = 559
                localctx._block = self.block()
                self.state = 560
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
            self.state = 597
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,42,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 565
                localctx.pp1 = self.procedureParameter(localctx.enableRw)
                localctx.paramList.append(localctx.pp1.param) 
                self.state = 573
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,39,self._ctx)
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1:
                        self.state = 567
                        self.match(SetlXgrammarParser.T__31)
                        self.state = 568
                        localctx.pp2 = self.procedureParameter(localctx.enableRw)
                        localctx.paramList.append(localctx.pp2.param)  
                    self.state = 575
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,39,self._ctx)

                self.state = 582
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==SetlXgrammarParser.T__31:
                    self.state = 576
                    self.match(SetlXgrammarParser.T__31)
                    self.state = 577
                    localctx.dp1 = self.procedureDefaultParameter()
                    localctx.paramList.append(localctx.dp1.param) 
                    self.state = 584
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 585
                localctx.dp2 = self.procedureDefaultParameter()
                localctx.paramList.append(localctx.dp2.param) 
                self.state = 593
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==SetlXgrammarParser.T__31:
                    self.state = 587
                    self.match(SetlXgrammarParser.T__31)
                    self.state = 588
                    localctx.dp3 = self.procedureDefaultParameter()
                    localctx.paramList.append(localctx.dp3.param) 
                    self.state = 595
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
            self.state = 607
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,43,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 599
                if not localctx.enableRw:
                    from antlr4.error.Errors import FailedPredicateException
                    raise FailedPredicateException(self, "$enableRw")
                self.state = 600
                self.match(SetlXgrammarParser.T__63)
                self.state = 601
                localctx._assignableVariable = self.assignableVariable()
                localctx.param = ReadWriteParameter(localctx._assignableVariable.v.id) 
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 604
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
            self.state = 609
            localctx._assignableVariable = self.assignableVariable()
            self.state = 610
            self.match(SetlXgrammarParser.T__26)
            self.state = 611
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
            self.state = 624
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [SetlXgrammarParser.T__1]:
                self.enterOuterAlt(localctx, 1)
                self.state = 614
                self.match(SetlXgrammarParser.T__1)
                self.state = 615
                localctx._callParameters = self.callParameters(localctx.enableIgnore)
                self.state = 616
                self.match(SetlXgrammarParser.T__2)
                localctx.c = FunctionCall(localctx._callParameters.params, localctx._callParameters.ex) 
                		
                pass
            elif token in [SetlXgrammarParser.T__28]:
                self.enterOuterAlt(localctx, 2)
                self.state = 619
                self.match(SetlXgrammarParser.T__28)
                self.state = 620
                localctx._collectionAccessParams = self.collectionAccessParams(localctx.enableIgnore)
                self.state = 621
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
        self.enterRule(localctx, 50, self.RULE_collectionAccessParams)

        params = []
            
        self._la = 0 # Token type
        try:
            self.state = 651
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,48,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 626
                localctx.e1 = self.expr(localctx.enableIgnore)
                self.state = 645
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [SetlXgrammarParser.RANGE_SIGN]:
                    self.state = 627
                    self.match(SetlXgrammarParser.RANGE_SIGN)
                    self.state = 632
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,45,self._ctx)
                    if la_ == 1:
                        self.state = 628
                        localctx.e2 = self.expr(localctx.enableIgnore)
                        localctx.p = ListRange(localctx.e1.ex,localctx.e2.ex) 
                        pass

                    elif la_ == 2:
                        localctx.p = ListRange(localctx.e1.ex,None) 
                        pass


                    pass
                elif token in [SetlXgrammarParser.T__31]:
                    self.state = 638 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    while True:
                        self.state = 634
                        self.match(SetlXgrammarParser.T__31)
                        self.state = 635
                        localctx.e3 = self.expr(False)
                        params.append(localctx.e3.ex) 
                        self.state = 640 
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
                self.state = 647
                self.match(SetlXgrammarParser.RANGE_SIGN)
                self.state = 648
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
            self.state = 657
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,49,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 653
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
            self.state = 685
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,52,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 659
                self.match(SetlXgrammarParser.T__28)
                self.state = 663
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,50,self._ctx)
                if la_ == 1:
                    self.state = 660
                    localctx._collectionBuilder = self.collectionBuilder(localctx.enableIgnore)
                    cb = localctx._collectionBuilder.cb; 


                self.state = 665
                self.match(SetlXgrammarParser.T__29)
                localctx.v = SetlXList(cb) 
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 667
                self.match(SetlXgrammarParser.T__3)
                self.state = 671
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,51,self._ctx)
                if la_ == 1:
                    self.state = 668
                    localctx._collectionBuilder = self.collectionBuilder(localctx.enableIgnore)
                    cb = localctx._collectionBuilder.cb; 


                self.state = 673
                self.match(SetlXgrammarParser.T__4)
                localctx.v = SetListConstructor(cb) 
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 675
                localctx._STRING = self.match(SetlXgrammarParser.STRING)
                localctx.v = SetlXString((None if localctx._STRING is None else localctx._STRING.text)) 
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 677
                localctx._LITERAL = self.match(SetlXgrammarParser.LITERAL)
                localctx.v = SetlXLiteral((None if localctx._LITERAL is None else localctx._LITERAL.text)) 
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 679
                localctx._atomicValue = self.atomicValue()
                localctx.v = localctx._atomicValue.av 
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 682
                if not localctx.enableIgnore:
                    from antlr4.error.Errors import FailedPredicateException
                    raise FailedPredicateException(self, "$enableIgnore")
                self.state = 683
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
        self.enterRule(localctx, 56, self.RULE_collectionBuilder)

        exprs = []
            
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 687
            localctx.e1 = self.expr(localctx.enableIgnore)
            self.state = 734
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [SetlXgrammarParser.T__31]:
                self.state = 688
                self.match(SetlXgrammarParser.T__31)
                self.state = 689
                localctx.e2 = self.expr(localctx.enableIgnore)
                self.state = 711
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [SetlXgrammarParser.RANGE_SIGN]:
                    self.state = 690
                    self.match(SetlXgrammarParser.RANGE_SIGN)
                    self.state = 691
                    localctx.e3 = self.expr(localctx.enableIgnore)
                    localctx.cb = Range(localctx.e1.ex, localctx.e2.ex, localctx.e3.ex) 
                    pass
                elif token in [SetlXgrammarParser.T__4, SetlXgrammarParser.T__11, SetlXgrammarParser.T__29, SetlXgrammarParser.T__31]:
                    exprs.append(localctx.e1.ex); exprs.append(localctx.e2.ex) 
                    self.state = 701
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    while _la==SetlXgrammarParser.T__31:
                        self.state = 695
                        self.match(SetlXgrammarParser.T__31)
                        self.state = 696
                        localctx.e3 = self.expr(localctx.enableIgnore)
                        exprs.append(localctx.e3.ex) 
                        self.state = 703
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)

                    self.state = 709
                    self._errHandler.sync(self)
                    token = self._input.LA(1)
                    if token in [SetlXgrammarParser.T__11]:
                        self.state = 704
                        self.match(SetlXgrammarParser.T__11)
                        self.state = 705
                        localctx.e4 = self.expr(False)
                        localctx.cb = ExplicitListWithRest(exprs, localctx.e4.ex) 
                        pass
                    elif token in [SetlXgrammarParser.T__4, SetlXgrammarParser.T__29]:
                        localctx.cb = ExplicitList(exprs)         
                        pass
                    else:
                        raise NoViableAltException(self)

                    pass
                else:
                    raise NoViableAltException(self)

                pass
            elif token in [SetlXgrammarParser.RANGE_SIGN]:
                self.state = 713
                self.match(SetlXgrammarParser.RANGE_SIGN)
                self.state = 714
                localctx.e3 = self.expr(localctx.enableIgnore)
                localctx.cb = Range(localctx.e1.ex, None, localctx.e3.ex) 
                pass
            elif token in [SetlXgrammarParser.T__4, SetlXgrammarParser.T__11, SetlXgrammarParser.T__29]:
                exprs.append(localctx.e1.ex) 
                self.state = 723
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [SetlXgrammarParser.T__11]:
                    self.state = 718
                    self.match(SetlXgrammarParser.T__11)
                    self.state = 719
                    localctx.e2 = self.expr(False)
                    localctx.cb = ExplicitListWithRest(exprs, localctx.e2.ex) 
                    pass
                elif token in [SetlXgrammarParser.T__4, SetlXgrammarParser.T__29]:
                    localctx.cb = ExplicitList(exprs)         
                    pass
                else:
                    raise NoViableAltException(self)

                pass
            elif token in [SetlXgrammarParser.T__8]:
                self.state = 725
                self.match(SetlXgrammarParser.T__8)
                self.state = 726
                localctx._iteratorChain = self.iteratorChain(localctx.enableIgnore)
                self.state = 732
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [SetlXgrammarParser.T__11]:
                    self.state = 727
                    self.match(SetlXgrammarParser.T__11)
                    self.state = 728
                    localctx.c1 = self.condition()
                    localctx.cb = SetlIteration(localctx.e1.ex, localctx._iteratorChain.ic, localctx.c1.cnd) 
                    pass
                elif token in [SetlXgrammarParser.T__4, SetlXgrammarParser.T__29]:
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
            self.state = 736
            localctx.i1 = self.iterator(localctx.enableIgnore)
            localctx.ic.append(localctx.i1.iter)
            self.state = 744
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==SetlXgrammarParser.T__31:
                self.state = 738
                self.match(SetlXgrammarParser.T__31)
                self.state = 739
                localctx.i2 = self.iterator(localctx.enableIgnore)
                localctx.ic.append(localctx.i2.iter) 
                self.state = 746
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
            self.state = 747
            localctx._assignable = self.assignable(True)
            self.state = 748
            self.match(SetlXgrammarParser.T__44)
            self.state = 749
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
            self.state = 762
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [SetlXgrammarParser.NUMBER]:
                self.enterOuterAlt(localctx, 1)
                self.state = 752
                localctx._NUMBER = self.match(SetlXgrammarParser.NUMBER)
                localctx.av = SetlXFraction((None if localctx._NUMBER is None else localctx._NUMBER.text)) 
                pass
            elif token in [SetlXgrammarParser.DOUBLE]:
                self.enterOuterAlt(localctx, 2)
                self.state = 754
                localctx._DOUBLE = self.match(SetlXgrammarParser.DOUBLE)
                localctx.av = float((None if localctx._DOUBLE is None else localctx._DOUBLE.text)) 
                pass
            elif token in [SetlXgrammarParser.T__64]:
                self.enterOuterAlt(localctx, 3)
                self.state = 756
                self.match(SetlXgrammarParser.T__64)
                localctx.av = SetlXOm() 
                pass
            elif token in [SetlXgrammarParser.T__65]:
                self.enterOuterAlt(localctx, 4)
                self.state = 758
                self.match(SetlXgrammarParser.T__65)
                localctx.av = SetlXTrue() 
                pass
            elif token in [SetlXgrammarParser.T__66]:
                self.enterOuterAlt(localctx, 5)
                self.state = 760
                self.match(SetlXgrammarParser.T__66)
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
            self.state = 764
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
            self.state = 767
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
            self.state = 770
            localctx.a1 = self.assignable(True)
            localctx.al.append(localctx.a1.a) 
            self.state = 778
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==SetlXgrammarParser.T__31:
                self.state = 772
                self.match(SetlXgrammarParser.T__31)
                self.state = 773
                localctx.a2 = self.assignable(True)
                localctx.al.append(localctx.a2.a) 
                self.state = 780
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
         




