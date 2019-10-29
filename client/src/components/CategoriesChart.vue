<script lang="ts">
import { Component, Vue, Mixins, Watch } from 'vue-property-decorator'
import { Doughnut, mixins } from 'vue-chartjs'

@Component
export default class CategoriesChart extends Mixins(
  Doughnut,
  mixins.reactiveData
)<{ chartData: any }> {
  /**
   * Chart options.
   */
  public readonly options = {
    responsive: true,
    maintainAspectRatio: true,
    circumference: Math.PI,
    rotation: Math.PI,
    legend: {
      display: true,
      position: 'top'
    },
    onClick: this.onCategoryClick.bind(this),
    tooltips: {
      callbacks: {
        label: this.labelContent.bind(this)
      }
    }
  }

  /**
   * Selected category.
   */
  get selected() {
    return this.$store.state.categories.selectedItem
  }

  /**
   * Get the categories.
   */
  get categories() {
    return this.$store.state.foodgroups
  }

  /**
   * Get the optimal repartition.
   */
  get optimalRepartition() {
    return this.$store.state.categories.optimalRepartition
  }

  /**
   * Get the list of colors.
   */
  get colors() {
    const list = this.$store.state.categories.colors

    return this.selected
      ? this.categories.map((v, i) => (v === this.selected ? list[v] : 'grey'))
      : this.orderValues(list)
  }
  /**
   * Get the list of all commands.
   */
  get commands() {
    return this.$store.getters.commands
  }

  /**
   * Get current repartition.
   */
  get repartition() {
    return this.commands.reduce((all, command) => {
      command.details.map(detail => {
        const name = this.categories[detail[0]]
        all[name] = all[name] || 0
        all[name] += detail[1]
      })

      return all
    }, {})
  }

  /**
   * Get chart data.
   */
  @Watch('commands', { immediate: true })
  public setChartData() {
    this.chartData = {
      labels: this.categories,
      datasets: [
        {
          label: 'Répartition actuelle',
          data: this.orderValues(this.repartition),
          backgroundColor: this.colors
        },
        {
          label: 'Répartition optimale',
          borderWidth: 5,
          data: this.orderValues(this.optimalRepartition),
          backgroundColor: this.colors
        }
      ]
    }
  }

  /**
   * Order values by category name.
   */
  public orderValues(object: any) {
    return this.categories.map(name => {
      return object[name]
    })
  }

  /**
   * On category click.
   */
  public onCategoryClick(event, [data]) {
    if (data) {
      const category = data._chart.data.labels[data._index]
      if (this.selected === category) {
        this.$store.dispatch('categories/select', null)
      } else {
        this.$store.dispatch('categories/select', category)
      }
    }
  }

  /**
   * Label content.
   */
  public labelContent({ datasetIndex, index }, { datasets, labels }) {
    const total = datasets[datasetIndex].data.reduce(
      (total, current) => total + current,
      0
    )
    const current = datasets[datasetIndex].data[index]

    return `${labels[index]} : ${current / 1000}kg (${(
      (current / total) *
      100
    ).toFixed(2)}%)`
  }

  /**
   * Mounted.
   */
  public mounted() {
    this.renderChart(this.chartData, this.options)
  }
}
</script>