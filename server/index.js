const app = require('express')()
const fs = require('fs')
const path = require('path')
const port = process.env.PORT || 4000

/**
 * Get the table content.
 *
 * TODO: modify this method to fetch result from the database.
 */
function get(table) {
  return JSON.parse(fs.readFileSync(path.resolve(__dirname, `scripts/json/${table}.json`), 'utf-8'))
}

/**
 * Return proper JSON file on GET request (/viztavie).
 */
app.get('/viztavie', (req, res) => {
  const tables = ['emmitters', 'receivers', 'aggregated_orders', 'commands', 'foodgroups']
  const result = tables.reduce((a, c) => ({ ...a, [c]: get(c) }), {})
  res.send(result)
})

/**
 * LIsten to the app on given port.
 */
app.listen(port, () => console.log(`Server launched on port: ${port}.`))
