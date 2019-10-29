<template>
  <div class="my-4">
    <p class="text-xl font-bold">Géographie</p>
    <div class="mb-4">
      <label class="mb-2 block">Trier par :</label>
      <select-input
        :options="layers"
        label-key="label"
        v-model="layeringType"
        value-key="type"
      />
    </div>
    <div class="mb-4">
      <label class="mb-2 block">Zone géographique :</label>
      <select-input
        :options="layer.json.features"
        label-key="properties.nom"
        null-label="France"
        v-model="selected"
      />
    </div>
  </div>
</template>

<script lang="ts">
import { Component, Vue, Prop } from 'vue-property-decorator'
import SelectInput from '@/components/Inputs/Select.vue'
import { GeoJsonProperties } from 'geojson'

@Component({
  components: { SelectInput }
})
export default class PanelGeography extends Vue {
  /**
   * Get geo layering.
   */
  get layer() {
    return this.$store.state.geography.layer
  }

  /**
   * Get selected geo item.
   */
  get selected() {
    return this.$store.state.geography.selectedItem
  }

  /**
   * Set selected geo item.
   */
  set selected(value: GeoJsonProperties) {
    this.$store.dispatch('geography/select', value)
  }

  /**
   * Get layering type.
   */
  get layeringType() {
    return this.$store.state.geography.layeringType
  }

  /**
   * Set layering type.
   */
  set layeringType(value: string) {
    this.$store.dispatch('geography/setLayeringType', value)
  }

  /**
   * Get layers.
   */
  get layers() {
    return this.$store.state.geography.layers
  }
}
</script>