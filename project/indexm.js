const fs = require("fs");
const parser = require("@babel/parser");
const traverse = require("@babel/traverse").default;
const t = require("@babel/types");
const generate = require("@babel/generator").default;

const code = `var arr = '3,4,0,4,1'['split'](',');`;

const ast = parser.parse(code, { sourceType: "module" });

traverse(ast, {
    VariableDeclarator(path) {
        const init = path.node.init;

        // 检查是否为 str['split'](',') 这种形式
        if (
            t.isCallExpression(init) &&
            t.isMemberExpression(init.callee) &&
            t.isStringLiteral(init.callee.object) &&
            t.isStringLiteral(init.callee.property, { value: "split" }) &&
            init.arguments.length === 1 &&
            t.isStringLiteral(init.arguments[0])
        ) {
            const strValue = init.callee.object.value;
            const splitArg = init.arguments[0].value;

            const resultArray = strValue.split(splitArg);
            const newArrayNode = t.arrayExpression(
                resultArray.map((val) => t.stringLiteral(val))
            );

            path.node.init = newArrayNode;
        }
    },
});

const output = generate(ast, { compact: false }).code;
console.log(output);
