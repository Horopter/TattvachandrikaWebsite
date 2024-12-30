<template>
  <div class="container mt-5">
    <h2>Subscriber Categories</h2>
    <nav aria-label="breadcrumb">
      <ol class="breadcrumb">
        <li class="breadcrumb-item"><router-link to="/">Home</router-link></li>
        <li class="breadcrumb-item active" aria-current="page">Subscriber Categories</li>
      </ol>
    </nav>

    <table class="table table-striped mt-4">
      <thead>
        <tr>
          <th>Name</th>
          <th>Actions</th>
        </tr>
      </thead>
      <tbody>
        <tr v-if="addingNew">
          <td><input type="text" v-model="newSubscriberCategory.name" class="form-control" /></td>
          <td>
            <button class="btn btn-primary btn-sm" @click="saveNewSubscriberCategory">Save</button>
            <button class="btn btn-secondary btn-sm" @click="cancelNewSubscriberCategory">Cancel</button>
          </td>
        </tr>
        <tr v-for="category in subscriberCategories" :key="category._id">
          <template v-if="editMode === category._id">
            <td><input type="text" v-model="editSubscriberCategory.name" class="form-control" /></td>
            <td>
              <button class="btn btn-primary btn-sm" @click="updateSubscriberCategory(category._id)">Save</button>
              <button class="btn btn-secondary btn-sm" @click="cancelEdit">Cancel</button>
            </td>
          </template>
          <template v-else>
            <td>{{ category.name }}</td>
            <td>
              <button class="btn btn-warning btn-sm" @click="editSubscriberCategoryFunc(category)">Edit</button>
              <button class="btn btn-danger btn-sm" @click="showDeleteModal(category._id)">Delete</button>
            </td>
          </template>
        </tr>
      </tbody>
    </table>
    <button class="btn btn-success mt-3" @click="startAddingNew">Add New Category</button>

    <confirmation-modal
      v-if="showConfirmationModal"
      :show="showConfirmationModal"
      title="Confirm Delete"
      message="Are you sure you want to delete this subscriber category?"
      @close="hideDeleteModal"
      @confirm="deleteSubscriberCategory"
    />
  </div>
</template>

<script>
import subscriberCategoryService from '../services/subscriberCategoryService';
import ConfirmationModal from './ConfirmationModal.vue';

export default {
  components: {
    ConfirmationModal
  },
  data() {
    return {
      subscriberCategories: [],
      addingNew: false,
      editMode: null,
      showConfirmationModal: false,
      categoryToDelete: null,
      newSubscriberCategory: {
        name: ''
      },
      editSubscriberCategory: {
        name: ''
      }
    };
  },
  created() {
    this.loadSubscriberCategories();
  },
  methods: {
    loadSubscriberCategories() {
      subscriberCategoryService.getSubscriberCategories().then(response => {
        this.subscriberCategories = response.data;
      }).catch(error => {
        console.error("There was an error retrieving the subscriber categories!", error);
      });
    },
    startAddingNew() {
      this.addingNew = true;
      this.resetNewSubscriberCategory();
    },
    cancelNewSubscriberCategory() {
      this.addingNew = false;
    },
    resetNewSubscriberCategory() {
      this.newSubscriberCategory = {
        name: ''
      };
    },
    saveNewSubscriberCategory() {
      subscriberCategoryService.createSubscriberCategory(this.newSubscriberCategory).then(() => {
        this.loadSubscriberCategories();
        this.addingNew = false;
      }).catch(error => {
        console.error("There was an error saving the subscriber category!", error);
      });
    },
    editSubscriberCategoryFunc(category) {
      this.editMode = category._id;
      this.editSubscriberCategory = { ...category };
    },
    cancelEdit() {
      this.editMode = null;
    },
    updateSubscriberCategory(id) {
      subscriberCategoryService.updateSubscriberCategory(id, this.editSubscriberCategory).then(() => {
        this.loadSubscriberCategories();
        this.editMode = null;
      }).catch(error => {
        console.error("There was an error updating the subscriber category!", error);
      });
    },
    showDeleteModal(id) {
      this.categoryToDelete = id;
      this.showConfirmationModal = true;
    },
    hideDeleteModal() {
      this.showConfirmationModal = false;
      this.categoryToDelete = null;
    },
    deleteSubscriberCategory() {
      subscriberCategoryService.deleteSubscriberCategory(this.categoryToDelete).then(() => {
        this.loadSubscriberCategories();
        this.hideDeleteModal();
      }).catch(error => {
        console.error("There was an error deleting the subscriber category!", error);
      });
    }
  }
};
</script>

<style scoped>
/* Add your styles here */
</style>
