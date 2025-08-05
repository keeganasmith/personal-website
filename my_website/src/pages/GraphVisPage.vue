<template>
  <div class="bridge-visualizer">
    <div ref="network" class="network"></div>
    <div class="controls">
      <button @click="onBack" :disabled="frameIdx === 0">Back</button>
      <span>Iteration {{ frameIdx + 1 }} / {{ snapshots.length }}</span>
      <button @click="onNext" :disabled="frameIdx === snapshots.length - 1">Next</button>
    </div>
  </div>
</template>

<script>
import { Network, DataSet } from 'vis-network/standalone';

// Basic Union-Find implementation in JS
class UnionFind {
  constructor(n) {
    this.parent = Array.from({ length: n }, (_, i) => i);
    this.rank = Array(n).fill(0);
  }
  find(x) {
    if (this.parent[x] !== x) {
      this.parent[x] = this.find(this.parent[x]);
    }
    return this.parent[x];
  }
  merge(x, y) {
    let rx = this.find(x);
    let ry = this.find(y);
    if (rx === ry) return false;
    if (this.rank[rx] < this.rank[ry]) [rx, ry] = [ry, rx];
    this.parent[ry] = rx;
    if (this.rank[rx] === this.rank[ry]) this.rank[rx]++;
    return true;
  }
}

export default {
  name: 'BridgeVisualizer',
  props: {
    numVertices: { type: Number, default: 10 },
    avgDegree: { type: Number, default: 2 }
  },
  data() {
    return {
      edges: [],            // raw edge list
      snapshots: [],        // [ [notBridges, maybeBridges], ... ]
      frameIdx: 0,          // current snapshot index
      network: null,        // vis-network instance
      nodesData: null,      // DataSet for nodes
      edgesData: null       // DataSet for edges
    };
  },
  mounted() {
    this.edges = this.generateEdgeList(this.numVertices, this.avgDegree);
    this.snapshots = this.findBridgesVisual(this.edges, this.numVertices);
    this.initNetwork();
    this.updatePlot();
  },
  methods: {
    generateEdgeList(n, avgDeg) {
      const edgeSet = new Set();
      const numEdges = Math.floor(n * avgDeg / 2);
      while (edgeSet.size < numEdges) {
        let u = Math.floor(Math.random() * n);
        let v = Math.floor(Math.random() * n);
        if (u === v) continue;
        const [a, b] = u < v ? [u, v] : [v, u];
        edgeSet.add(`${a},${b}`);
      }
      return Array.from(edgeSet).map(s => s.split(',').map(Number));
    },
    findBridgesVisual(edges, n) {
      const notBridges = [];
      let maybeBridges = edges.slice();
      const snaps = [];
      snaps.push([ [...notBridges], [...maybeBridges] ]);
      // Use a for(;;) loop to satisfy lint (no-constant-condition)
      for (;;) {
        const uf = new UnionFind(n);
        notBridges.forEach(([u, v]) => uf.merge(u, v));
        const newMaybe = [];
        maybeBridges.forEach(([u, v]) => {
          if (uf.merge(u, v)) newMaybe.push([u, v]);
          else notBridges.push([u, v]);
        });
        snaps.push([ [...notBridges], [...maybeBridges] ]);
        if (newMaybe.length === maybeBridges.length) break;
        maybeBridges = newMaybe;
      }
      snaps.push([ notBridges, maybeBridges ]);
      return snaps;
    },
    initNetwork() {
      const nodes = Array.from({ length: this.numVertices }, (_, id) => ({ id, label: String(id) }));
      this.nodesData = new DataSet(nodes);
      const edgesVis = this.edges.map(([u, v], idx) => ({ id: idx, from: u, to: v, color: { color: 'gray' } }));
      this.edgesData = new DataSet(edgesVis);
      const container = this.$refs.network;
      const data = { nodes: this.nodesData, edges: this.edgesData };
      const options = { physics: { stabilization: false }, edges: { smooth: false } };
      this.network = new Network(container, data, options);
    },
    updatePlot() {
      const [notBr, maybeBr] = this.snapshots[this.frameIdx];
      this.edges.forEach(([u, v], idx) => {
        const matches = ([x, y]) => x === u && y === v;
        const inNot = notBr.some(matches);
        const inMaybe = maybeBr.some(matches);
        let color = 'gray';
        if (inNot) color = 'red';
        else if (inMaybe) color = this.frameIdx === this.snapshots.length - 1 ? 'yellow' : 'yellow';
        this.edgesData.update({ id: idx, color: { color } });
      });
    },
    onNext() {
      if (this.frameIdx < this.snapshots.length - 1) {
        this.frameIdx++;
        this.updatePlot();
      }
    },
    onBack() {
      if (this.frameIdx > 0) {
        this.frameIdx--;
        this.updatePlot();
      }
    }
  }
};
</script>

<style scoped>
.bridge-visualizer {
  display: flex;
  flex-direction: column;
  align-items: center;
}
.network {
  width: 600px;
  height: 400px;
  border: 1px solid #ccc;
}
.controls {
  margin-top: 10px;
  display: flex;
  align-items: center;
}
.controls button {
  margin: 0 5px;
  padding: 5px 10px;
}
.controls span {
  font-weight: bold;
}
</style>
