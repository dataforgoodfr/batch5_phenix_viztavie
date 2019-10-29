<template>
  <l-geo-json
    :geojson="layer.json"
    :options="{ onEachFeature }"
    ref="geoJson"
  />
</template>

<script lang="ts">
import { Component, Vue, Prop, Watch, Ref } from 'vue-property-decorator'
import { LMap, LGeoJson } from 'vue2-leaflet'
import { Map } from 'leaflet'

@Component({
  components: { LGeoJson }
})
export default class GeographyGeoJson extends Vue {
  @Ref() public geoJson: LGeoJson

  /**
   * Get selected item.
   */
  get selected() {
    return this.$store.state.geography.selectedItem
  }

  /**
   * get layer.
   */
  get layer() {
    return this.$store.state.geography.layer
  }

  /**
   * Get selected layer
   */
  get selectedLayer() {
    return this.geoJson.mapObject
      .getLayers()
      .find((layer: any) => layer.feature === this.selected)
  }

  /**
   * On each feature.
   */
  public onEachFeature(feature, layer) {
    layer.on('click', () => {
      if (this.selected !== feature) {
        this.$store.dispatch('geography/select', feature)
      } else {
        this.$store.dispatch('geography/select', null)
      }
    })
  }

  /**
   * Move map to feature.
   */
  @Watch('selected')
  public moveMapToSelected(selected) {
    if (selected) {
      //@ts-ignore
      const map: Map = this.geoJson.mapObject._map
      //@ts-ignore
      map.fitBounds(this.selectedLayer.getBounds())
    } else {
      this.$emit('reset')
    }
  }
}
</script>