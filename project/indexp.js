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

const updateParametor = {
    Identifier(path) {
        if (path.node.name === this.paramName) {
            console.log("参数名被替换为:", this.newName);
            path.node.name = this.newName;  // 替换参数名
        }
    }
}

const visitor = {
    FunctionDeclaration(path) {
        const paramName = path.node.params[0].name;  // 获取第一个参数名
        path.traverse(updateParametor, {
            paramName: paramName,
            newName: "x"  // 新参数名
        });
    }
}

traverse(ast, visitor);

const output = generate(ast, { comments: false, compact: false }, code);
fs.writeFileSync("./output.js", output.code);

console.log("✅ AST 转换完成，输出已写入 output.js");