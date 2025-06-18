const fs = require("fs");
const parser = require("@babel/parser");
const traverse = require("@babel/traverse").default;
const t = require("@babel/types");
const generate = require("@babel/generator").default;

// 读取源码
const inputPath = './input.js';
if (!fs.existsSync(inputPath)) {
    console.error(`输入文件 ${inputPath} 不存在`);
    process.exit(1);
}
const code = fs.readFileSync(inputPath, 'utf-8');

// 解析 AST
const ast = parser.parse(code, { sourceType: "module" });

// 变量重命名映射表
const nameMap = {};
let counter = 1;

// 遍历 AST
traverse(ast, {
    Identifier(path) {
        const oldName = path.node.name;
        if (/^_0x[a-fA-F0-9]+$/.test(oldName)) {
            if (!nameMap[oldName]) {
                nameMap[oldName] = `renamedVar${counter++}`;
            }
            path.node.name = nameMap[oldName];
        }
    },
    CallExpression(path) {
        const callee = path.node.callee;
        if (
            t.isMemberExpression(callee) &&
            t.isIdentifier(callee.object, { name: "console" }) &&
            t.isIdentifier(callee.property, { name: "log" })
        ) {
            const firstArg = path.node.arguments[0];
            if (t.isStringLiteral(firstArg) && firstArg.value.startsWith("[test]")) {
                firstArg.value = firstArg.value.replace("[test]", "[TEST]");
                console.log("changed test to TEST");
            }
            else if (t.isStringLiteral(firstArg) && !firstArg.value.startsWith("[TEST]")) {
                firstArg.value = "[TEST] " + firstArg.value;
            }
        }
    }
});

// 生成代码
const output = generate(ast, { comments: false, compact: false }, code);
fs.writeFileSync("./output.js", output.code);
console.log("✅ AST 转换完成，已写入 output.js");
