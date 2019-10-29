<template functional>
  <div class="my-4">
    <p class="text-xl font-bold">Légende</p>
    <div class="mt-2 mb-4">
      <label class="mb-2 block">Nombre de dons :</label>
      <p class="flex align-center">
        <strong class="mr-4">Faible</strong>
        <span class="w-4 h-4 block bg-blue-200" />
        <span class="w-4 h-4 block bg-blue-300" />
        <span class="w-4 h-4 block bg-blue-400" />
        <span class="w-4 h-4 block bg-blue-500" />
        <span class="w-4 h-4 block bg-blue-600" />
        <strong class="ml-4">Fort</strong>
      </p>
    </div>
    <div class="mt-2 mb-4">
      <p class="mb-2 flex items-center">
        <span>Émmetteurs :</span>
        <span class="ml-4 marker emmitters block" />
      </p>
      <p class="mb-2 flex items-center">
        <span>Receveurs :</span>
        <span class="ml-4 marker receivers block" />
      </p>
    </div>
  </div>
</template>


<script lang="ts">
import { Component, Vue } from 'vue-property-decorator'

@Component
export default class PanelLegend extends Vue {}
</script>