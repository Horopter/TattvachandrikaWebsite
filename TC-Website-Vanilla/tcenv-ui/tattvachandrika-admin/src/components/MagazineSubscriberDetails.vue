<template>
  <div class="container mt-5">
    <nav aria-label="breadcrumb">
      <ol class="breadcrumb">
        <li class="breadcrumb-item"><router-link to="/">Home</router-link></li>
        <li class="breadcrumb-item"><router-link to="/subscribers">Subscribers</router-link></li>
        <li class="breadcrumb-item active" aria-current="page">{{ subscriber.name }}</li>
      </ol>
    </nav>
    <h2>{{ subscriber.name }}</h2>
    <div class="details">
      <p><strong>Registration Number:</strong> {{ subscriber.registration_number }}</p>
      <p><strong>Address:</strong> {{ subscriber.address }}</p>
      <p><strong>City/Town:</strong> {{ subscriber.city_town }}</p>
      <p><strong>State:</strong> {{ subscriber.state }}</p>
      <p><strong>Pincode:</strong> {{ subscriber.pincode }}</p>
      <p><strong>Phone:</strong> {{ subscriber.phone }}</p>
      <p><strong>Email:</strong> {{ subscriber.email }}</p>
      <p><strong>Category:</strong> {{ getCategoryName(subscriber.category) }}</p>
      <p><strong>Type:</strong> {{ getTypeName(subscriber.stype) }}</p>
      <p><strong>Notes:</strong> {{ subscriber.notes }}</p>
    </div>
    <button class="btn btn-primary mb-3" @click="openAddSubscriptionModal">Add Subscription</button>

    <!-- Tabs for Active and Inactive Subscriptions -->
    <ul class="nav nav-tabs" id="subscriptionTab" role="tablist">
      <li class="nav-item" role="presentation">
        <button class="nav-link active" id="active-tab" data-bs-toggle="tab" data-bs-target="#active" type="button" role="tab" aria-controls="active" aria-selected="true">Active Subscriptions</button>
      </li>
      <li class="nav-item" role="presentation">
        <button class="nav-link" id="inactive-tab" data-bs-toggle="tab" data-bs-target="#inactive" type="button" role="tab" aria-controls="inactive" aria-selected="false">Inactive Subscriptions</button>
      </li>
    </ul>
    <div class="tab-content" id="subscriptionTabContent">
      <!-- Active Subscriptions Tab -->
      <div class="tab-pane fade show active" id="active" role="tabpanel" aria-labelledby="active-tab">
        <table class="table table-striped mt-3">
          <thead>
            <tr>
              <th>Start Date</th>
              <th>End Date</th>
              <th>Subscription Plan</th>
              <th>Payment Status</th>
              <th>Payment Mode</th>
              <th>Payment Date</th>
              <th>Actions</th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="subscription in activeSubscriptions" :key="subscription._id">
              <td>{{ formatDate(subscription.start_date) }}</td>
              <td>{{ formatDate(subscription.end_date) }}</td>
              <td>{{ getPlanName(subscription.subscription_plan) }}</td>
              <td>{{ subscription.payment_status }}</td>
              <td>{{ getPaymentModeName(subscription.payment_mode) }}</td>
              <td>{{ formatDate(subscription.payment_date) }}</td>
              <td>
                <button class="btn btn-secondary btn-sm" @click="openEditSubscriptionModal(subscription)">Edit</button>
              </td>
            </tr>
          </tbody>
        </table>
      </div>
      <!-- Inactive Subscriptions Tab -->
      <div class="tab-pane fade" id="inactive" role="tabpanel" aria-labelledby="inactive-tab">
        <table class="table table-striped mt-3">
          <thead>
            <tr>
              <th>Start Date</th>
              <th>End Date</th>
              <th>Subscription Plan</th>
              <th>Payment Status</th>
              <th>Payment Mode</th>
              <th>Payment Date</th>
              <th>Actions</th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="subscription in inactiveSubscriptions" :key="subscription._id">
              <td>{{ formatDate(subscription.start_date) }}</td>
              <td>{{ formatDate(subscription.end_date) }}</td>
              <td>{{ getPlanName(subscription.subscription_plan) }}</td>
              <td>{{ subscription.payment_status }}</td>
              <td>{{ getPaymentModeName(subscription.payment_mode) }}</td>
              <td>{{ formatDate(subscription.payment_date) }}</td>
              <td>
                <button class="btn btn-secondary btn-sm" @click="openEditSubscriptionModal(subscription)">Edit</button>
              </td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>

    <!-- Add/Edit Subscription Modal -->
    <add-edit-subscription-modal
      :show="showAddEditSubscriptionModal"
      :subscription="currentSubscription"
      :subscription-plans="subscriptionPlans"
      :payment-modes="paymentModes"
      @close="closeAddEditSubscriptionModal"
      @save="saveSubscription"
    />
    <!-- Toast Notification -->
    <toast-notification ref="toast" />
  </div>
</template>

<script>
import addEditSubscriptionModal from './AddEditSubscriptionModal.vue';
import magazineSubscriberService from '../services/magazineSubscriberService';
import subscriptionPlanService from '../services/subscriptionPlanService';
import paymentModeService from '../services/paymentModeService';
import subscriptionService from '../services/subscriptionService';
import ToastNotification from './ToastNotification.vue';

export default {
  components: {
    addEditSubscriptionModal,
    ToastNotification
  },
  data() {
    return {
      subscriber: {},
      activeSubscriptions: [],
      inactiveSubscriptions: [],
      subscriptionPlans: [],
      paymentModes: [],
      categories: [],
      types: [],
      showAddEditSubscriptionModal: false,
      currentSubscription: null
    };
  },
  created() {
    this.loadSubscriber();
    this.loadSubscriptionPlans();
    this.loadPaymentModes();
    this.loadCategories();
    this.loadTypes();
  },
  methods: {
    loadSubscriber() {
      const subscriberId = this.$route.params.id;
      magazineSubscriberService.getMagazineSubscriberById(subscriberId).then(response => {
        this.subscriber = response.data;
        this.loadSubscriptions(subscriberId);
      }).catch(error => {
        this.$refs.toast.showToast('Error retrieving subscribers', 'Error', 'danger');
        console.error("There was an error retrieving the subscriber details!", error);
      });
    },
    loadSubscriptions(subscriberId) {
      subscriptionService.getSubscriptionsBySubscriber(subscriberId).then(response => {
        this.activeSubscriptions = response.data.filter(sub => sub.active);
        this.inactiveSubscriptions = response.data.filter(sub => !sub.active);
      }).catch(error => {
        this.$refs.toast.showToast('Error retrieving subscriptions', 'Error', 'danger');
        console.error("There was an error retrieving the subscriptions!", error);
      });
    },
    loadSubscriptionPlans() {
      subscriptionPlanService.getPlans().then(response => {
        this.subscriptionPlans = response.data;
      }).catch(error => {
        this.$refs.toast.showToast('Error retrieving subscription plans', 'Error', 'danger');
        console.error("There was an error retrieving the subscription plans!", error);
      });
    },
    loadPaymentModes() {
      paymentModeService.getPaymentModes().then(response => {
        this.paymentModes = response.data;
      }).catch(error => {
        this.$refs.toast.showToast('Error retrieving subscriptions', 'Error', 'danger');
        console.error("There was an error retrieving the payment modes!", error);
      });
    },
    loadCategories() {
      magazineSubscriberService.getCategories().then(response => {
        this.categories = response.data;
      }).catch(error => {
        this.$refs.toast.showToast('Error retrieving categories', 'Error', 'danger');
        console.error("There was an error retrieving the categories!", error);
      });
    },
    loadTypes() {
      magazineSubscriberService.getTypes().then(response => {
        this.types = response.data;
      }).catch(error => {
        this.$refs.toast.showToast('Error retrieving types', 'Error', 'danger');
        console.error("There was an error retrieving the types!", error);
      });
    },
    openAddSubscriptionModal() {
      this.currentSubscription = {
        subscriber: this.subscriber._id,
        subscription_plan: '',
        payment_status: 'Pending',
        payment_mode: this.paymentModes[0].name,
        payment_date: ''
      };
      this.showAddEditSubscriptionModal = true;
    },
    openEditSubscriptionModal(subscription) {
      this.currentSubscription = { ...subscription };
      this.showAddEditSubscriptionModal = true;
    },
    closeAddEditSubscriptionModal() {
      this.showAddEditSubscriptionModal = false;
    },
    saveSubscription(subscription) {
      if (subscription._id) {
        subscriptionService.updateSubscription(subscription._id, subscription).then(() => {
          this.loadSubscriptions(this.subscriber._id);
          this.showAddEditSubscriptionModal = false;
        }).catch(error => {
          console.error("There was an error updating the subscription!", error);
        });
      } else {
        subscriptionService.createSubscription(subscription).then(() => {
          this.loadSubscriptions(this.subscriber._id);
          this.showAddEditSubscriptionModal = false;
        }).catch(error => {
          console.error("There was an error creating the subscription!", error);
        });
      }
    },
    formatDate(date) {
      const options = { year: 'numeric', month: '2-digit', day: '2-digit' };
      return new Date(date).toLocaleDateString(undefined, options);
    },
    getPlanName(planId) {
      const plan = this.subscriptionPlans.find(plan => plan._id === planId);
      return plan ? plan.name : '';
    },
    getPaymentModeName(modeId) {
      const mode = this.paymentModes.find(mode => mode._id === modeId);
      return mode ? mode.name : '';
    },
    getCategoryName(categoryId) {
      const category = this.categories.find(cat => cat._id === categoryId);
      return category ? category.name : '';
    },
    getTypeName(typeId) {
      const type = this.types.find(type => type._id === typeId);
      return type ? type.name : '';
    }
  }
};
</script>

<style scoped>
.table {
  margin-top: 20px;
}
</style>
