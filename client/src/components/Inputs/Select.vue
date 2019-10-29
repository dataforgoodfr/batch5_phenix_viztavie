<template>
  <div class="relative cursor-pointer">
    <select
      :value="getValueIndex(value)"
      @input="update($event.target.value)"
      class="block appearance-none w-full bg-gray-300 border border-gray-300 text-gray-700 py-3 px-4 pr-8 rounded leading-tight focus:outline-none focus:bg-white focus:border-gray-500"
    >
      <option
        v-if="nullLabel"
        value
      >{{nullLabel}}</option>
      <option
        :key="index"
        :value="index"
        v-for="(option, index) in options"
      >{{getOptionLabel(option)}}</option>
    </select>
    <div
      class="pointer-events-none absolute inset-y-0 right-0 flex items-center px-2 text-gray-700"
    >
      <svg
        class="fill-current h-4 w-4"
        viewBox="0 0 20 20"
        xmlns="http://www.w3.org/2000/svg"
      >
        <path d="M9.293 12.95l.707.707L15.657 8l-1.414-1.414L10 10.828 5.757 6.586 4.343 8z" />
      </svg>
    </div>
  </div>
</template>

<script lang="ts">
import { Component, Vue, Model, Prop } from 'vue-property-decorator'

@Component
export default class Select extends Vue {
  @Model('input') public value!: any
  @Prop() public options!: any[]
  @Prop() public labelKey?: string
  @Prop() public valueKey?: string
  @Prop() public nullLabel?: string

  /**
   * Get option value.
   */
  public getOptionValue(item: any) {
    return this.valueKey
      ? this.valueKey.split('.').reduce((a, c) => a[c], item)
      : item
  }

  /**
   * Get option label.
   */
  public getOptionLabel(item: any) {
    return this.labelKey
      ? this.labelKey.split('.').reduce((a, c) => a[c], item)
      : item
  }

  /**
   * Update the value.
   */
  public update(index: number) {
    this.$emit(
      'input',
      index === null ? null : this.getOptionValue(this.options[index])
    )
  }

  /**
   * Get value index.
   */
  public getValueIndex(value: any) {
    const index = this.options.findIndex(
      option => this.getOptionValue(option) === value
    )

    return index > -1 ? index : null
  }
}
</script>