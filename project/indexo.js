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

const visitor = {
    VariableDeclarator(path) {
        if (path.node.init) {
            path.node.init = t.numericLiteral(123); // 将初始值设为 123
        }
    },
    NumberLiteral(path) {
        if (path.node.value === 123) {
            path.replaceWith(t.valueToNode("456")); // 替换节点
        }
    },
    // NumberLiteral(path) {
    //     if (path.node.value === 123) {
    //         path.replaceWithSourceString("function add(a,b){return a+b}"); // 替换节点
    //     }
    // }
};

traverse(ast, visitor);

const output = generate(ast, { comments: false, compact: false }, code);
fs.writeFileSync("./output.js", output.code);

console.log("✅ AST 转换完成，输出已写入 output.js");
