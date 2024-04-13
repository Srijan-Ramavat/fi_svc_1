<template>
  <div class="graph-container">
    <GChart type="BarChart" :data="chartData" :options="chartOptions" />
  </div>
</template>

<script>
import { GChart } from "vue-google-charts";

export default {
  name: "BarChart",
  props: ["chartData"],
  components: { GChart },
  data() {
    return {
      chartOptions: {
        title: "Day-wise Spend",
        chartArea: { width: "50%" },
        hAxis: {
          title: "Category",
        },
        vAxis: {
          title: "Amount Spend",
          minValue: 0,
        },
      },
    };
  },
};
</script>

<style scoped>
.graph-container {
  display: flex;
  justify-content: center;
  width: 100%;
}
</style>
