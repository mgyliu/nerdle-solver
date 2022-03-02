def evaluateExpression(expr):
    if "+" in expr:
        parts = expr.rsplit("+", 1)
        return evaluateExpression(parts[0]) + evaluateExpression(parts[1])
    elif "-" in expr:
        parts = expr.rsplit("-", 1)
        return evaluateExpression(parts[0]) - evaluateExpression(parts[1])
    elif "*" in expr:
        parts = expr.rsplit("*", 1)
        return evaluateExpression(parts[0]) * evaluateExpression(parts[1])
    elif "/" in expr:
        parts = expr.rsplit("/", 1)
        return evaluateExpression(parts[0]) * 1.0 / evaluateExpression(parts[1])
    else:
        return int(expr)
