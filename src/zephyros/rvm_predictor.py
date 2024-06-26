"""
Module for using relevance vector machine to predict the estimated power
output of a wind turbine.
"""
# Copyright (C) 2024  Keno Krieger <kriegerk@uni-bremen.de>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.
from sklearn_rvm import EMRVR


def learn_and_predict(learn_data, predict_data, features, target):
    """
    Given learn data and predict data, learn a relevance vector machine and use
    it on the predict data. Return the predicted values.

    Args:
        learn_data(pandas.DataFrame): Data to use for learning the machine.
        predict_data(pandas.DataFrame: Data to use for the prediction.
        features(list): The features to use for the learning and predicting.
        target(list): The target of the learning and predicting.

    Returns:
        numpy.ndarray: The predicted values and their standard deviation.

    """
    x_in = learn_data[features].to_numpy()
    y_in = learn_data[target].to_numpy().ravel()
    x_pred = predict_data[features].to_numpy()
    model = learn(x_in, y_in)
    return predict(model, x_pred)


def predict(model, x_pred):
    """
    Predict values given a learned model and features *x_pred*.
    Args:
        model(sklearn_rvm.EMRVR): The learned model.
        x_pred(numpy.ndarray): Feature values to use for the prediction.

    Returns:
        np.ndarray: The predicted values and their standard deviation.
    """
    return model.predict(x_pred, return_std=True)


def learn(x_in, y_in):
    """
    Learn a relevance vector machine given feature values *x_in* and
    target values *y_in*. Return the learned model.

    Args:
        x_in(np.ndarray): Feature values to use for learning the model.
        y_in(np.ndarray: Target value for the learning process.

    Returns:
        sklearn_rvm.EMRVR: The learned model.
    """
    model = EMRVR(kernel="rbf")
    model.fit(x_in, y_in)
    return model
