<template>
  <div>
    <el-table
      ref="multipleTable"
      :data="tableData"
      style="width: 100%"
      @selection-change="handleSelectionChange"
    >
      <el-table-column type="selection" width="55"> </el-table-column>
      <el-table-column property="name" label="Product"> </el-table-column>
      <el-table-column property="subcategory.name" label="Subcategory">
      </el-table-column>
      <el-table-column property="subcategory.category.name" label="Category">
      </el-table-column>
    </el-table>
    <div style="margin-top: 20px">
      <el-button @click="toggleSelection([tableData[1], tableData[2]])"
        >Toggle selection status of second and third rows</el-button
      >
      <el-button @click="toggleSelection()">Clear selection</el-button>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      tableData: [],
      multipleSelection: []
    };
  },
  methods: {
    toggleSelection(rows) {
      if (rows) {
        rows.forEach(row => {
          this.$refs.multipleTable.toggleRowSelection(row);
        });
      } else {
        this.$refs.multipleTable.clearSelection();
      }
    },
    handleSelectionChange(val) {
      this.multipleSelection = val;
    },
    getProducts() {
      var api = "http://127.0.0.1:8000/api/store/products/";
      this.axios.get(api).then(response => {
        this.tableData = response.data.results;
      });
    }
  },
  mounted() {
    this.getProducts();
  }
};
</script>
