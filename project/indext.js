const fs = require("fs");
const parser = require("@babel/parser");
const traverse = require("@babel/traverse").default;
const t = require("@babel/types");
const generate = require("@babel/generator").default;

// 读取 JS 源码
const inputPath = './input.js';
if (!fs.existsSync(inputPath)) {
    console.error(`输入文件 ${inputPath} 不存在`);
    process.exit(1);
}

const code = fs.readFileSync(inputPath, "utf-8");

// 生成 AST
const ast = parser.parse(code, { sourceType: "module" });

// 遍历修改 AST
traverse(ast, {
    // 修改函数名
    FunctionDeclaration(path) {
        const functionName = path.node.id.name;
        if (functionName === 'sayHello') {
            path.node.id = t.identifier('logHello');  // 替换函数名为 logHello
        }
    },

    // 在所有函数体开始插入 console.log
    FunctionExpression(path) {
        const functionBody = path.node.body;

        // 创建 console.log 语句
        const logStatement = t.expressionStatement(
            t.callExpression(
                t.memberExpression(t.identifier("console"), t.identifier("log")),
                [t.stringLiteral("entry function")]
            )
        );

        // 将 console.log 插入函数体的开始
        functionBody.body.unshift(logStatement);  // 在函数体开头插入
    },

    ArrowFunctionExpression(path) {
        const functionBody = path.node.body;

        // 创建 console.log 语句
        const logStatement = t.expressionStatement(
            t.callExpression(
                t.memberExpression(t.identifier("console"), t.identifier("log")),
                [t.stringLiteral("enter function")]
            )
        );

        // 将 console.log 插入函数体的开始
        if (t.isBlockStatement(functionBody)) {
            functionBody.body.unshift(logStatement);  // 在函数体开头插入
        }
    }
});

// 生成新代码
const output = generate(ast, { comments: false, compact: false }, code);
fs.writeFileSync("./output.js", output.code);

console.log("✅ 函数名修改和插入日志完成，输出已写入 output.js");
