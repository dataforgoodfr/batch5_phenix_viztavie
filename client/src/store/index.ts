import Vue from 'vue'
import Vuex from 'vuex'
import { Data } from './../../@types/Data'
import axios from 'axios'
import geography from './geography'
import categories from './categories'

Vue.use(Vuex)

const state: Data = {
  aggregated_orders: [],
  emmitters: [],
  receivers: [],
  foodgroups: [],
  commands: []
}

const mutations = {
  /**
   * Set all data.
   */
  set(state, data: Data) {
    for (let i in data) {
      state[i] = Object.freeze(data[i])
    }
  }
}

const actions = {
  /**
   * Fetch the data.
   */
  async fetch({ commit }) {
    try {
      const { data } = await axios.get('api/viztavie')
      commit('set', data)
      return data
    } catch (error) {
      console.error(error)
    }
  }
}

const getters = {
  emmitters(state) {
    const { selectedItem, bounds } = state.geography
    return state.emmitters.filter(subject => {
      return (
        subject.coordinates.every(p => p !== null) &&
        (selectedItem ? bounds[selectedItem.properties.nom].contains(subject.coordinates) : true)
      )
    })
  },
  receivers(state) {
    const { selectedItem, bounds } = state.geography
    return state.receivers.filter(subject => {
      return (
        subject.coordinates.every(p => p !== null) &&
        (selectedItem ? bounds[selectedItem.properties.nom].contains(subject.coordinates) : true)
      )
    })
  },
  foodgroups(state) {
    return state.foodgroups
  },
  commands(state, getters) {
    const emmiterIds = getters.emmitters.map(e => e.id)
    const categoryIndex = state.foodgroups.indexOf(state.categories.selectedItem)
    return state.commands.filter(command => {
      return (
        emmiterIds.includes(command.ec_id) &&
        (categoryIndex > -1 ? command.details.some(d => d[0] === categoryIndex) : true)
      )
    })
  }
}

export default new Vuex.Store({
  modules: {
    geography,
    categories
  },
  state,
  mutations,
  actions,
  getters
})
