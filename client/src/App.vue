<template>
  <div
    class="h-screen w-screen overflow-hidden flex"
    id="app"
  >
    <template v-if="loading">
      <div class="flex flex-col items-center justify-center h-full w-full">
        <div class="border-4 rounded-full border-blue-400 border-t-transparent loading h-12 w-12" />
        <p class="mt-8 text-xl">Chargement des données...</p>
      </div>
    </template>

    <template v-else>
      <panel class="w-1/6" />
      <geography class="flex-1" />
      <div class="flex flex-col w-2/6">
        <categories class="flex-1" />
        <calendar class="flex-1" />
      </div>
    </template>
  </div>
</template>

<script lang="ts">
import { Component, Vue, Watch, Mixins } from 'vue-property-decorator'
import Panel from '@/components/Panel.vue'
import Categories from '@/components/Categories.vue'
import Calendar from '@/components/Calendar.vue'
import Geography from '@/components/Geography.vue'

@Component({
  components: { Panel, Categories, Calendar, Geography }
})
export default class App extends Vue {
  /**
   * Loading state.
   */
  public loading: boolean = false

  /**
   * On creation.
   */
  public async created() {
    this.loading = true
    await this.$store.dispatch('fetch')
    this.loading = false
  }
}
</script>

<style lang="sass">
@tailwind base
@tailwind components
@tailwind utilities

@keyframes loading
  to
    transform: rotate(360deg)

.loading
  animation: loading infinite linear 2s
  border-top-color: transparent
</style>