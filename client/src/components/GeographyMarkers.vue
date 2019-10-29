<template>
  <l-marker-cluster>
    <l-marker
      :key="`partner-${index}`"
      :lat-lng="coordinates"
      v-for="({ coordinates, name }, index) in partners"
    >
      <l-icon>
        <div :class="`marker ${type}`" />
      </l-icon>
      <l-popup :content="name" />
    </l-marker>
  </l-marker-cluster>
</template>

<script lang="ts">
import { Component, Vue, Prop } from 'vue-property-decorator'
import { LMarker, LPopup, LIcon } from 'vue2-leaflet'

import LMarkerCluster from 'vue2-leaflet-markercluster'
import { Emmitter } from '../../@types/Emmitter'
import { Receiver } from '../../@types/Receiver'

@Component({
  components: { LMarker, LPopup, LIcon, LMarkerCluster }
})
export default class GeographyMarkers extends Vue {
  @Prop() public type: 'emmitters' | 'receivers'

  /**
   * Get partners.
   */
  get partners() {
    return this.$store.state[this.type].filter(subject =>
      subject.coordinates.every(p => p !== null)
    )
  }
}
</script>


<style lang="sass">
.marker
  @apply border rounded-full h-4 w-4
  &.emmitters
    @apply bg-green-400 border-green-500
  &.receivers
    @apply bg-blue-400 border-blue-500
</style>