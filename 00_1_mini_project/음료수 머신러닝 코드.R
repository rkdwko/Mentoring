library(caret)
library(dplyr)

df <- read.csv('c:/Users/Q/Downloads/3조_sales_김상규.csv', header = T)
df <- df %>% select(4:7, 9)

idx <- sample(1:nrow(df), size = nrow(df) * 0.7, replace = F)
df_train <- df[idx, ]
df_test <- df[-idx, ]

lm_fit <- lm(QTY~., df_train)
summary(lm_fit)
lm_yhat <- predict(lm_fit, df_test)
sqrt(mean((lm_yhat - df_test$QTY)^2))
#317.9

library(tree)
tree_fit <- tree(QTY~., df_train)
summary(tree_fit)
plot(tree_fit)
text(tree_fit, pretty = 0)

tree_yhat <- predict(tree_fit, df_test)
sqrt(mean((tree_yhat - df_test$QTY)^2))
#315.4

library(rpart)
library(rpart.plot)
rpart_fit <- rpart(QTY ~ PRICE + MAXTEMP + SALEDAY + HOLIDAY, df_train)
summary(rpart_fit)
rpart.plot(rpart_fit)
rpart.plot(rpart_fit, digits = 3, type = 0, extra = 1, fallen.leaves = F, cex = 1)

rpart_yhat <- predict(rpart_fit, df_test)
sqrt(mean((rpart_yhat - df_test$QTY)^2))
#459.4

library(randomForest)
rf_fit <- randomForest(QTY~., df_train, mtry = 4, importance = T)

rf_yhat <- predict(rf_fit, df_test)
sqrt(mean((rf_yhat - df_test$QTY)^2))
#228.1