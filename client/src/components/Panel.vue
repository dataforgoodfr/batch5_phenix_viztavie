<template>
  <aside class="bg-gray-200 rounded p-4 overflow-auto">
    <panel-geography />
    <panel-products />
    <panel-partners />
    <panel-distances />
    <panel-legend />
    <panel-explanation />
  </aside>
</template>

<script lang="ts">
import { Component, Vue, Prop } from 'vue-property-decorator'
import PanelDistances from './PanelDistances.vue'
import PanelPartners from './PanelPartners.vue'
import PanelProducts from './PanelProducts.vue'
import PanelGeography from './PanelGeography.vue'
import PanelExplanation from './PanelExplanation.vue'
import PanelLegend from './PanelLegend.vue'

@Component({
  components: {
    PanelDistances,
    PanelPartners,
    PanelProducts,
    PanelGeography,
    PanelExplanation,
    PanelLegend
  }
})
export default class Panel extends Vue {}
</script>