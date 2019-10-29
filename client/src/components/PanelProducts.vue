<template>
  <div class="my-4">
    <p class="text-xl font-bold">Produits</p>
    <div class="my-2">
      <p>Nombre de produits : {{nbProducts.toLocaleString()}}</p>
    </div>
    <div class="my-2">
      <p>
        Qualité des dons
        <sup>**</sup>
        : {{ratio.toFixed(2)}}%
      </p>
    </div>
  </div>
</template>

<script lang="ts">
import { Component, Vue, Prop } from 'vue-property-decorator'

@Component
export default class PanelProducts extends Vue {
  /**
   * Get filtered commands.
   */
  get commands() {
    return this.$store.getters.commands
  }

  /**
   * Number of products.
   */
  get nbProducts() {
    return this.commands.reduce((total, command) => {
      return total + command.details.length
    }, 0)
  }

  /**
   * Get optimal repartition.
   */
  get optimalRepartition() {
    return this.$store.state.categories.optimalRepartition
  }

  /**
   * Get categories.
   */
  get categories() {
    return this.$store.state.foodgroups
  }

  /**
   * Get ratio of given products' categories
   * compared to the optimal repartition.
   */
  get ratio() {
    return this.commands.reduce((total, command) => {
      const quantity = command.details.reduce(
        (total, detail) => total + detail[1],
        0
      )
      const gap = command.details.reduce((total, detail) => {
        const name = this.categories[detail[0]]
        const ratioQuantity = detail[1] / quantity
        const optimalQuantity = this.optimalRepartition[name] / 1000
        return (Math.abs(ratioQuantity - optimalQuantity) || 0) * 100
      }, 0)

      return total - gap / this.commands.length
    }, 100)
  }
}
</script>