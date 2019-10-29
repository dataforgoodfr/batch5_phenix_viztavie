<template>
  <div class="my-4">
    <p class="text-xl font-bold">Partenaires</p>
    <div class="my-2">
      <p>Émmetteurs : {{emmitters.length.toLocaleString()}}</p>
    </div>
    <div class="my-2">
      <p>Receveurs : {{receivers.length.toLocaleString()}}</p>
    </div>
  </div>
</template>

<script lang="ts">
import { Component, Vue, Prop } from 'vue-property-decorator'

@Component
export default class PanelPartners extends Vue {
  /**
   * Get filtered emmitters.
   */
  get emmitters() {
    return this.$store.getters.emmitters
  }

  /**
   * Get filtered receivers.
   */
  get receivers() {
    return this.$store.getters.receivers
  }
}
</script>