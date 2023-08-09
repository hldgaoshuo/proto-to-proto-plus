import antlr4 as ant
from Protobuf3Lexer import Protobuf3Lexer
from Protobuf3Parser import Protobuf3Parser
from Protobuf3Visitor import Protobuf3Visitor


def log(*args, **kwargs):
    print(*args, **kwargs, flush=True)


def proto_type_trans(name):
    d = {
        'string': 'proto.STRING',
        'int32': 'proto.INT32',
    }
    r = d.get(name, name)
    return r


class EvalVisitor(Protobuf3Visitor):
    def __init__(self):
        self.index = 0
        self.result = 'import proto\n\n'
        self.field_type = ''
        self.field_name = ''

    def add(self, content):
        space = self.index * 4 * ' '
        self.result = self.result + space + content

    def visitMessageDef(self, ctx: Protobuf3Parser.MessageDefContext):
        self.add('class ')
        self.visitChildren(ctx)

    def visitMessageName(self, ctx: Protobuf3Parser.MessageNameContext):
        name = ctx.getText()
        self.add(f'{name}(proto.Message):\n')
        self.visitChildren(ctx)

    def visitMessageBody(self, ctx: Protobuf3Parser.MessageBodyContext):
        self.index += 1
        self.visitChildren(ctx)
        self.index -= 1

    def visitType_(self, ctx: Protobuf3Parser.Type_Context):
        name = ctx.getText()
        name_ = proto_type_trans(name)
        self.field_type = name_

    def visitFieldName(self, ctx: Protobuf3Parser.FieldNameContext):
        name = ctx.getText()
        self.field_name = name

    def visitFieldNumber(self, ctx: Protobuf3Parser.FieldNumberContext):
        name = ctx.getText()
        self.add(f'{self.field_name} = proto.Field({self.field_type}, number={name})\n')


def __main():
    path = 'main.proto'
    fs = ant.FileStream(path, encoding='utf-8')
    lexer = Protobuf3Lexer(fs)
    tokens = ant.CommonTokenStream(lexer)
    ast = Protobuf3Parser(tokens).proto()
    visitor = EvalVisitor()
    visitor.visit(ast)
    log(visitor.result)


if __name__ == '__main__':
    __main()
