<template functional>
  <div class="my-4 text-sm">
    <p>
      <sup>
        <strong>**</strong>
      </sup> Etant donnés
      <span style="font-family: STIXGeneral; font-style: italic;">x</span> l'ensemble des répartitions optimales par catégorie et
      <span
        style="font-family: STIXGeneral; font-style: italic;"
      >y</span> l'ensemble des répartitions actuelles par catégorie, cet index est calculé selon :
    </p>

    <!-- START OF THE FUNCTION -->
    <div
      class="text-center"
      tabindex="0"
    >
      <nobr>
        <span
          role="math"
          style="width: 9.589em; display: inline-block;"
        >
          <span
            style="display: inline-block; position: relative; width: 7.596em; height: 0px; font-size: 126%;"
          >
            <span
              style="position: absolute; clip: rect(0.852em, 1007.6em, 3.464em, -1000em); top: -2.608em; left: 0em;"
            >
              <span>
                <span style="font-family: STIXGeneral;">1</span>
                <span style="font-family: STIXGeneral; padding-left: 0.25em;">−</span>
                <span style="padding-left: 0.25em;">
                  <span
                    style="display: inline-block; position: relative; width: 5.662em; height: 0px; margin-right: 0.12em; margin-left: 0.12em;"
                  >
                    <span
                      style="position: absolute; clip: rect(3.055em, 1005.48em, 4.499em, -1000em); top: -4.811em; left: 50%; margin-left: -2.771em;"
                    >
                      <span>
                        <span>
                          <span
                            style="display: inline-block; position: relative; width: 2.023em; height: 0px;"
                          >
                            <span
                              style="position: absolute; clip: rect(3.094em, 1000.86em, 4.456em, -1000em); top: -4.025em; left: 0em;"
                            >
                              <span style="font-family: STIXGeneral; vertical-align: -0.002em;">∑</span>
                              <span style="display: inline-block; width: 0px; height: 4.025em;"></span>
                            </span>
                            <span
                              style="position: absolute; clip: rect(3.543em, 1000.59em, 4.201em, -1000em); top: -4.513em; left: 0.914em;"
                            >
                              <span>
                                <span>
                                  <span
                                    style="font-size: 70.7%; font-family: STIXGeneral; font-style: italic;"
                                  >m</span>
                                </span>
                              </span>
                              <span style="display: inline-block; width: 0px; height: 4.025em;"></span>
                            </span>
                            <span
                              style="position: absolute; clip: rect(3.392em, 1001.11em, 4.203em, -1000em); top: -3.729em; left: 0.914em;"
                            >
                              <span>
                                <span>
                                  <span
                                    style="font-size: 70.7%; font-family: STIXGeneral; font-style: italic;"
                                  >i</span>
                                  <span style="font-size: 70.7%; font-family: STIXGeneral;">=</span>
                                  <span
                                    style="font-size: 70.7%; font-family: STIXGeneral; font-style: italic;"
                                  >n</span>
                                </span>
                              </span>
                              <span style="display: inline-block; width: 0px; height: 4.025em;"></span>
                            </span>
                          </span>
                        </span>
                        <span style="padding-left: 0.488em;">
                          <span>
                            <span>
                              <span>
                                <span style="font-family: STIXGeneral;">|</span>
                              </span>
                            </span>
                            <span>
                              <span
                                style="display: inline-block; position: relative; width: 0.873em; height: 0px;"
                              >
                                <span
                                  style="position: absolute; clip: rect(3.414em, 1000.45em, 4.206em, -1000em); top: -4.025em; left: 0em;"
                                >
                                  <span style="font-family: STIXGeneral; font-style: italic;">
                                    x
                                    <span
                                      style="display: inline-block; overflow: hidden; height: 1px; width: 0.003em;"
                                    ></span>
                                  </span>
                                  <span style="display: inline-block; width: 0px; height: 4.025em;"></span>
                                </span>
                                <span style="position: absolute; top: -3.875em; left: 0.444em;">
                                  <span
                                    style="font-size: 70.7%; font-family: STIXGeneral; font-style: italic;"
                                  >n</span>
                                  <span style="display: inline-block; width: 0px; height: 4.025em;"></span>
                                </span>
                              </span>
                            </span>
                            <span style="font-family: STIXGeneral; padding-left: 0.25em;">−</span>
                            <span style="padding-left: 0.25em;">
                              <span
                                style="display: inline-block; position: relative; width: 0.873em; height: 0px;"
                              >
                                <span
                                  style="position: absolute; clip: rect(3.414em, 1000.43em, 4.401em, -1000em); top: -4.025em; left: 0em;"
                                >
                                  <span style="font-family: STIXGeneral; font-style: italic;">y</span>
                                  <span style="display: inline-block; width: 0px; height: 4.025em;"></span>
                                </span>
                                <span style="position: absolute; top: -3.875em; left: 0.444em;">
                                  <span
                                    style="font-size: 70.7%; font-family: STIXGeneral; font-style: italic;"
                                  >n</span>
                                  <span style="display: inline-block; width: 0px; height: 4.025em;"></span>
                                </span>
                              </span>
                            </span>
                            <span>
                              <span>
                                <span style="font-family: STIXGeneral;">|</span>
                              </span>
                            </span>
                          </span>
                        </span>
                      </span>
                      <span style="display: inline-block; width: 0px; height: 4.025em;"></span>
                    </span>
                    <span
                      style="position: absolute; clip: rect(3.179em, 1000.47em, 4.195em, -1000em); top: -3.339em; left: 50%; margin-left: -0.25em;"
                    >
                      <span style="font-family: STIXGeneral;">2</span>
                      <span style="display: inline-block; width: 0px; height: 4.025em;"></span>
                    </span>
                    <span
                      style="position: absolute; clip: rect(0.836em, 1005.66em, 1.247em, -1000em); top: -1.297em; left: 0em;"
                    >
                      <span
                        style="display: inline-block; overflow: hidden; vertical-align: 0em; border-top: 1.3px solid; width: 5.662em; height: 0px;"
                      ></span>
                      <span style="display: inline-block; width: 0px; height: 1.077em;"></span>
                    </span>
                  </span>
                </span>
              </span>
              <span style="display: inline-block; width: 0px; height: 2.608em;"></span>
            </span>
          </span>
          <span
            style="display: inline-block; overflow: hidden; vertical-align: -0.936em; border-left: 0px solid; width: 0px; height: 3.005em;"
          ></span>
        </span>
      </nobr>
    </div>
    <!-- END OF THE FUNCTION  -->
  </div>
</template>

<script lang="ts">
import { Component, Vue } from 'vue-property-decorator'

@Component
export default class PanelExplanation extends Vue {}
</script>