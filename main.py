import antlr4 as ant
from Protobuf3Lexer import Protobuf3Lexer
from Protobuf3Parser import Protobuf3Parser
from Protobuf3Visitor import Protobuf3Visitor


def log(*args, **kwargs):
    print(*args, **kwargs, flush=True)


class EvalVisitor(Protobuf3Visitor):
    def visitMessageName(self, ctx: Protobuf3Parser.MessageNameContext):
        log(ctx.getText())
        return self.visitChildren(ctx)

    def visitFieldName(self, ctx:Protobuf3Parser.FieldNameContext):
        log(ctx.getText())
        return self.visitChildren(ctx)


def __main():
    path = 'main.proto'
    fs = ant.FileStream(path, encoding='utf-8')
    lexer = Protobuf3Lexer(fs)
    tokens = ant.CommonTokenStream(lexer)
    ast = Protobuf3Parser(tokens).proto()
    visitor = EvalVisitor()
    visitor.visit(ast)


if __name__ == '__main__':
    __main()
