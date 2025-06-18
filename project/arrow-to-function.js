// arrow-to-function.js
module.exports = function () {
    return {
        visitor: {
            ArrowFunctionExpression(path) {
                const t = require('@babel/types');

                const { params, body, async } = path.node;

                // 如果箭头函数体是表达式（如 `x => x * 2`），转换为 return 语句
                const functionBody = t.isBlockStatement(body)
                    ? body
                    : t.blockStatement([t.returnStatement(body)]);

                // 构建新的普通函数表达式
                const func = t.functionExpression(
                    null, // 匿名函数
                    params,
                    functionBody,
                    false, // generator
                    async
                );

                path.replaceWith(func);
            }
        }
    };
};
