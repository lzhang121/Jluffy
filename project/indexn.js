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
    BinaryExpression(path) {
        if (path.node.operator === "+") {
            const left = path.get("left");
            const right = path.get("right");

            if (
                (t.isNumericLiteral(left.node) || t.isStringLiteral(left.node)) &&
                (t.isNumericLiteral(right.node) || t.isStringLiteral(right.node))
            ) {
                const newValue = left.node.value + right.node.value;
                path.replaceWith(
                    typeof newValue === "number"
                        ? t.numericLiteral(newValue)
                        : t.stringLiteral(newValue)
                );
            }
        }
    }
};

traverse(ast, visitor);

const output = generate(ast, { comments: false, compact: false }, code);
fs.writeFileSync("./output.js", output.code);

console.log("✅ AST 转换完成，输出已写入 output.js");
