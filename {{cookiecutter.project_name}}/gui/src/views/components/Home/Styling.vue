<template>
  <div>
    <h3>Flex row</h3>
    <div class="d-flex flex-row  ">
      <ComponentNonUnique />
      <ComponentNonUnique />
      <ComponentNonUnique />
    </div>
  </div>
</template>

<script>
import ComponentNonUnique from "@/components/ComponentNonUnique";

export default {
  components: { ComponentNonUnique },
};
</script>
