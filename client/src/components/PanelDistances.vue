<template>
  <div class="my-4">
    <p class="text-xl font-bold">Distances</p>
    <div class="my-2">
      <p>Totale : {{toKm(totalDistance).toLocaleString()}}km</p>
    </div>
    <div class="my-2">
      <p>Moyenne : {{toKm(avgDistance).toLocaleString()}}km</p>
    </div>
    <div class="my-2">
      <p>Maximale : {{toKm(maxDistance).toLocaleString()}}km</p>
    </div>
    <div class="my-2">
      <p>Minimale : {{toKm(minDistance).toLocaleString()}}km</p>
    </div>
  </div>
</template>

<script lang="ts">
import { Component, Vue, Prop } from 'vue-property-decorator'
import { Map } from 'leaflet'
import { Emmitter } from '../../@types/Emmitter'
import { Receiver } from '../../@types/Receiver'

@Component
export default class PanelDistances extends Vue {
  /**
   * Get filtered commands.
   */
  get commands() {
    return this.$store.getters.commands
  }

  /**
   * Get all distances.
   */
  get distances() {
    return this.commands.map(command => {
      return Map.prototype.distance(
        this.emmittersCoords[command.ec_id],
        this.receiversCoords[command.rc_id]
      )
    })
  }

  /**
   * Get total distance (meters).
   */
  get totalDistance() {
    return this.distances.reduce((total, distance) => {
      return total + distance
    }, 0)
  }

  /**
   * Get average distance (meters).
   */
  get avgDistance() {
    return this.totalDistance / this.commands.length
  }

  /**
   * Get maximum distance (meters).
   */
  get maxDistance() {
    return Math.max(...this.distances)
  }

  /**
   * Get minimum distance (meters).
   */
  get minDistance() {
    return Math.min(...this.distances)
  }

  /**
   * Get coordinates of emmitters by id.
   */
  get emmittersCoords() {
    return this.$store.state.emmitters.reduce((all, emmitter) => {
      all[emmitter.id] = emmitter.coordinates
      return all
    }, {})
  }

  /**
   * Get coordinates of receivers by id.
   */
  get receiversCoords() {
    return this.$store.state.receivers.reduce((all, receiver) => {
      all[receiver.id] = receiver.coordinates
      return all
    }, {})
  }

  /**
   * Distance to kilometers.
   */
  public toKm(distance: number) {
    return Math.round((distance / 1000) * 100) / 100
  }
}
</script>