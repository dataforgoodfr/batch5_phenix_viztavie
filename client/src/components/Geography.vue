<template>
  <div class="bg-gray-400">
    <l-map
      :center="center"
      :zoom="zoom"
      ref="map"
    >
      <l-tile-layer :url="layerUrl" />
      <geography-markers type="emmitters" />
      <geography-markers type="receivers" />
      <geography-geo-json @reset="reset" />
    </l-map>
  </div>
</template>

<script lang="ts">
import { Component, Vue, Prop, Watch, Ref } from 'vue-property-decorator'
import { LMap, LTileLayer } from 'vue2-leaflet'
import { Emmitter } from '../../@types/Emmitter'
import { Receiver } from '../../@types/Receiver'
import GeographyMarkers from './GeographyMarkers.vue'
import GeographyGeoJson from './GeographyGeoJson.vue'
import { LatLng } from 'leaflet'

@Component({
  components: {
    LMap,
    LTileLayer,
    GeographyGeoJson,
    GeographyMarkers
  }
})
export default class Geography extends Vue {
  @Ref() public map: LMap

  /**
   * Zoom.
   */
  public zoom: number = 6

  /**
   * Map center.
   */
  public center = [46.7984947, 1.9593638]

  /**
   * Layer url.
   */
  public layerUrl: string = 'http://{s}.tile.osm.org/{z}/{x}/{y}.png'

  /**
   * Reset the map.
   */
  public reset() {
    this.map.mapObject.flyTo(
      new LatLng(this.center[0], this.center[1]),
      this.zoom
    )
  }
}
</script>

<style lang="sass">
@import '~leaflet/dist/leaflet.css'
@import '~leaflet.markercluster/dist/MarkerCluster.css'
@import '~leaflet.markercluster/dist/MarkerCluster.Default.css'

.leaflet-popup-content-wrapper
  @apply shadow-lg rounded select-none text-base text-center
</style>