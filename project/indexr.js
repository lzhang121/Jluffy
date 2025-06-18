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
// 名称映射表和计数器
const nameMap = {};
let counter = 1;

// 生成 AST
const ast = parser.parse(code, { sourceType: "module" });

// 遍历修改 AST
traverse(ast, {
    Identifier(path) {
        const oldName = path.node.name;
        // 匹配以 _0x 开头的变量名
        if (/^_0x[a-fA-F0-9]+$/.test(oldName)) {
            if (!nameMap[oldName]) {
                nameMap[oldName] = `renamedVar${counter++}`;
            }
            path.node.name = nameMap[oldName];
        }
    },
    ExpressionStatement(path) {
        const expr = path.node.expression;
        // 匹配 console.log(...)
        if (
            t.isCallExpression(expr) &&
            t.isMemberExpression(expr.callee) &&
            t.isIdentifier(expr.callee.object, { name: "console" }) &&
            t.isIdentifier(expr.callee.property, { name: "log" })
        ) {
            path.remove(); // 删除整条语句
        }
    }

});



// 生成新代码
const output = generate(ast, { comments: false, compact: false }, code);
fs.writeFileSync("./output.js", output.code);

console.log("✅ AST 转换完成，输出已写入 output.js");
