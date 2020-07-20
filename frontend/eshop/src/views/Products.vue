<template>
  <div>
    <el-table
      ref="multipleTable"
      :data="tableData"
      style="width: 100%"
      @selection-change="handleSelectionChange"
    >
      <el-table-column type="selection" width="100"> </el-table-column>
      <el-table-column property="name" label="Product" sortable>
      </el-table-column>
      <el-table-column
        property="subcategory.category.name"
        label="Category"
        sortable
      >
      </el-table-column>
      <el-table-column property="subcategory.name" label="Subcategory" sortable>
      </el-table-column>
    </el-table>
    <div class="new-product">
      <el-input
        placeholder="Product name"
        v-model="productName"
        style="max-width: 15em; margin-left: -17em;"
      ></el-input>

      <el-select
        v-model="categoryValue"
        clearable
        placeholder="Select category"
        @change="changeCategory"
        @clear="clearCategory"
        style="margin-left: 6em;"
      >
        <el-option
          v-for="item in categoryOptions"
          :key="item.uid"
          :label="item.name"
          :value="item.uid"
        >
        </el-option>
      </el-select>

      <el-select
        v-model="subCategoryValue"
        clearable
        placeholder="Select subcategory"
        :disabled="!categoryValue"
      >
        <el-option
          v-for="item in subCategoryOptions"
          :key="item.uid"
          :label="item.name"
          :value="item.uid"
        >
        </el-option>
      </el-select>
      <el-button
        type="primary"
        style="margin-left: -21em;"
        @click="createProduct"
        :disabled="!subCategoryValue || !productName"
        >Save</el-button
      >
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      tableData: [],
      multipleSelection: [],
      categoryOptions: [],
      categoryValue: "",
      initialSubCategoryOptions: [],
      subCategoryOptions: [],
      subCategoryValue: "",
      productName: ""
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
      var api = "http://127.0.0.1:8000/api/store/products/?limit=100";
      this.axios.get(api).then(response => {
        this.tableData = response.data.results;
      });
    },
    getCategories() {
      var api = "http://127.0.0.1:8000/api/store/categories/?limit=100";
      this.axios.get(api).then(response => {
        this.categoryOptions = response.data.results;
      });
    },
    getSubCategories() {
      var api = "http://127.0.0.1:8000/api/store/subcategories/?limit=100";
      this.axios.get(api).then(response => {
        this.subCategoryOptions = response.data.results;
        this.initialSubCategoryOptions = response.data.results;
      });
    },
    changeCategory(val) {
      this.subCategoryOptions = this.initialSubCategoryOptions.filter(
        x => x.category.uid == val
      );
    },
    clearCategory() {
      this.subCategoryOptions = this.initialSubCategoryOptions;
    },
    createProduct() {
      var data = {
        name: this.productName,
        subcategory_uid: this.subCategoryValue
      };
      var api = "http://127.0.0.1:8000/api/store/products/?limit=100";
      this.axios.post(api, data).then(response => {
        this.tableData.push(response.data);
      });
    }
  },
  mounted() {
    this.getProducts();
    this.getCategories();
    this.getSubCategories();
  }
};
</script>
<style>
.new-product {
  margin-top: 2em;
  display: flex;
  justify-content: space-evenly;
}
</style>
