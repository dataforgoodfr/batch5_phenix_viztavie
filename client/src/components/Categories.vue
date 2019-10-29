<template>
  <div class="bg-gray-300 p-8">
    <categories-chart />
  </div>
</template>

<script lang="ts">
import { Component, Vue } from 'vue-property-decorator'
import CategoriesChart from './CategoriesChart.vue'

@Component({
  components: { CategoriesChart }
})
export default class Categories extends Vue {}
</script>