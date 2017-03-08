var postcss = require("postcss")
var parser = require("postcss-value-parser")
var colorFn = require("css-color-function")
var helpers = require("postcss-message-helpers")
var customProperties = require('postcss-custom-properties')

fs.readFile('/etc/hosts', 'utf-8', function (err, data) {
  if (err) {
    return console.log(err);
  }

  var plugin = customProperties()
  plugin.setVariables(variables)
  var result = postcss()
    .use(plugin)
    .process(input)

  const style = postcss.parse(result)
  style.walkDecls(function(decl) {
    if (!decl.value || decl.value.indexOf("color(") === -1) {
      return
    }
    console.log(transformColor(decl.value))
  }
})

/**
 * Transform color() to rgb()
 *
 * @param  {String} string declaration value
 * @return {String}        converted declaration value to rgba()
 */
function transformColor(string) {
  return parser(string).walk(function(node) {
    if (node.type !== "function" || node.value !== "color") {
      return
    }
    node.value = colorFn.convert(parser.stringify(node))
    node.type = "word"
  }).toString()
}
