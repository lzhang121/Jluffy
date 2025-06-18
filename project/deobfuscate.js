const fs = require("fs");
const parser = require("@babel/parser");
const traverse = require("@babel/traverse").default;
const t = require("@babel/types");
const generate = require("@babel/generator").default;

// 加载 JS 文件内容
const code = fs.readFileSync("./input.js", "utf-8");

// 解析为 AST
const ast = parser.parse(code, {
    sourceType: "module",
});

// 记录替换名映射表
const nameMap = {};
let counter = 1;

// 遍历 AST
traverse(ast, {
    Identifier(path) {
        const oldName = path.node.name;
        // 只重命名类似 _0x 开头的变量
        if (/^_0x[a-f0-9]+$/i.test(oldName)) {
            if (!nameMap[oldName]) {
                nameMap[oldName] = `renamedVar${counter++}`;
            }
            path.node.name = nameMap[oldName];
        }
    }
});

// 生成新的代码
const output = generate(ast, {}, code);
fs.writeFileSync("./output.js", output.code);

console.log("变量名替换完成，已输出到 output.js");
